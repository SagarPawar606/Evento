from django.http import response
from django.http.response import Http404
from django.shortcuts import render
from .forms import BookingForm
from .models import Booking
from events.models import Event
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
import hmac
import hashlib



import razorpay
razorpay_client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))
razorpay_client.set_app_details({"title" : "Evento"})



# Create your views here.
@login_required
def payment(request, pk):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        try:
            event = Event.objects.get(id=pk)
            ticket_price = event.pricing
        except Event.DoesNotExist:
            raise Http404

        """Create a model instance for booking and save"""
        if form.is_valid():
            no_of_ticket = form.cleaned_data.get('no_of_ticket')
            total_amount = ticket_price * no_of_ticket
            try:
                booking = Booking.objects.create(event=event, 
                                                user=request.user, 
                                                no_of_ticket=no_of_ticket,
                                                total_amount=total_amount)
                booking.save()
            except Exception as e:
                return HttpResponse(f'[EXCEPTION] : {e}')
            
            """Razorpay Attributes"""
            DATA = {
                    "amount": total_amount*100,
                    "currency": "INR",
                    "receipt": booking.order_id,
                    "payment_capture": 0,  
                    "notes": {
                        "key1": f"Booking ticket for {booking.event}",
                    }
                }
            razor_order = razorpay_client.order.create(data=DATA)
            print(razor_order['id'])
            
            booking.razorpay_order_id = razor_order['id']
            booking.save()

            callback_url = 'http://'+ str(get_current_site(request))+"/booking/razorresponse/"
            
            context = {
                'booking' : booking,
                'razorpay_order_id' : booking.razorpay_order_id,
                'order_id' : booking.order_id,
                'total_amount' : booking.total_amount,
                'key_id' : settings.KEY_ID,
                'callback_url':callback_url
            }
            return render(request, 'payments/checkout.html', context= context)
    else:
        form =  BookingForm()
        try:
            event = Event.objects.get(id=pk)
        except Event.DoesNotExist:
            raise Http404
        return render(request, 'payments/payment.html', {'form':form, 'event':event})



@csrf_exempt
def razorresponse(request):
    """After payment razoarypay will respond with POST call
        save attribute of POST call (razorpay_payment_id, razoarpay_signature) on model instance
    """
    if request.method == 'POST':

        razorpay_order_id = request.POST['razorpay_order_id']
        razorpay_payment_id = request.POST['razorpay_payment_id']
        razorpay_signature = request.POST['razorpay_signature']
        booking = Booking.objects.get(razorpay_order_id = razorpay_order_id)
        try:
            """Use the SHA256 algorithm to construct a HMAC hex digest as to generate a signature"""
            ipt = booking.razorpay_order_id+"|"+razorpay_payment_id
            generated_signature = hmac.new(settings.KEY_SECRET.encode(), ipt.encode(), hashlib.sha256).hexdigest()
        except Exception as e :
            print(f'[EXCEPTION] : {e}')
            raise Http404

        if generated_signature == razorpay_signature:
            booking.razorpay_payment_id = razorpay_payment_id
            booking.razorpay_signature = razorpay_signature
            try:
                total_amount = booking.total_amount
                resp = razorpay_client.payment.capture(razorpay_payment_id, total_amount*100)
                if resp['status']=='captured':
                    booking.payment_status = 1
                    booking.save()
                    return render(request, 'payments/payment_success.html', {'order_id':booking.order_id})
                else:
                    booking.payment_status = 2
                    booking.save()
                    return render(request, 'payments/payment_failure.html', {'order_id':booking.order_id})
            except Exception as e:
                print(f"[Exception] - {e}")
                booking.payment_status = 2
                booking.save()
                return render(request, 'payments/payment_failure.html', {'order_id':booking.order_id})

        else:
            print('signature matching failed !')
            booking.payment_status = 2
            booking.save()
            return render(request, 'payments/payment_failure.html', {'order_id':booking.order_id})


        

