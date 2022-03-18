from django.shortcuts import render
from django.views.generic.base import View
from .models import Event
from django.views.generic import (ListView, DetailView, 
                                  CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import EventForm
from users.models import Pocket
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PocketListSerializer
from .filters import EventFilter
# Create your views here.


class ListViewEvent(ListView):
    '''homepage content'''
    model = Event
    template_name = 'events/newHome.html'
    context_object_name = 'events'

    def get_queryset(self):
        queryset = super().get_queryset()

        '''modifies the queryset to filter event accroding EventFilter'''
        print(self.request)
        filter = EventFilter(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super(ListViewEvent, self).get_context_data(**kwargs)
        context['featured_event'] = Event.objects.filter(featured=True).all()

        '''Filter form to filter the event according to city and catergories'''
        filter_form = EventFilter(self.request.GET, Event.objects.all())
        context['filter_form'] = filter_form
        return context

class CarouselList(ListView):
    '''Featured content'''
    model = Event
    template_name = 'events/carousel.html'
    context_object_name = 'events'

    def get_queryset(self, **kwargs):
        return Event.objects.filter(featured=True).all()


class MyEventList(LoginRequiredMixin, ListView):
    '''user specific event content'''
    model = Event
    template_name = 'events/my_events.html'
    context_object_name = 'events'
 
    def get_queryset(self):
        return Event.objects.filter(publisher=self.request.user).all()


class CategoricalEventList(ListView):
    '''list of specific category events'''
    model = Event
    template_name = 'events/categorical_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        print(self.kwargs)
        return Event.objects.filter(event_category = self.kwargs['category']).all()

class DetailViewEvent(DetailView):
    model = Event
    template_name = 'events/detail.html'
    context_object_name = 'event'

    ##########need to work on this############
    # def get_context_data(self, **kwargs):
    #     context = super(DetailViewEvent, self).get_context_data(**kwargs)
    #     date_added = Event.objects.filter(id=self.kwargs['pk']).values('date_added').first()
    #     added_ago = datetime.now().date() - date_added['date_added']
    #     context['added_ago'] = str(added_ago).split(",")[0]
    #     return context



class CreateViewEvent(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = EventForm
    model = Event
    #template name format -> 'app_name/modelname_form.html'
    context_object_name = 'event'
    success_message = "Event added successfully!"

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

# CreateView and UpdateView shares the common template
class UpdateViewEvent(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_message = "Event updated successfully!"

    def test_func(self):
        event = self.get_object()
        return event.publisher == self.request.user

class DeleteViewEvent(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    context_object_name = 'event'

    def test_func(self):
        event = self.get_object()
        print(event)
        return event.publisher == self.request.user


class PocketEventList(LoginRequiredMixin, ListView):
    '''events saved by specific user in pocket'''
    model = Pocket
    template_name = 'events/pocket.html'
    context_object_name = 'pocket'

    def get_queryset(self):
        return Pocket.objects.filter(user = self.request.user)

class DeletePocketEvent(LoginRequiredMixin, DeleteView):
    '''delete saved event from pocket'''
    model = Pocket
    context_object_name = 'event'
    template_name = 'events/pocket_confirm_delete.html'
    


class Search(View):
    '''search for event or user'''
    template_name = 'events/search_data.html'
    def get(self, request, *args, **kwargs):
        searched_for = request.GET.get('search') # 'search' -> name of searchfield
        q_data = Event.objects.filter(Q(title__icontains = searched_for) | Q(description__icontains = searched_for) | Q(keywords__icontains = searched_for))
        u_data = User.objects.filter(username__icontains = searched_for)
        print(q_data, u_data)
        return render(request, self.template_name, {'searched_for':searched_for, 'e_data':q_data, 'u_data':u_data})

    
#######---------api--------#######
@api_view(['GET'])
def testapi(request):
    return Response('hello world')

@api_view(['GET'])
def pocket_items(request, pk):
    pocket_events = Pocket.objects.filter(user=pk)
    serializer = PocketListSerializer(pocket_events, many=True)
    print(serializer.data)
    return Response(serializer.data)

