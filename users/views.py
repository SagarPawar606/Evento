from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UpdateUserForm, UpdateProfileForm
from .models import Profile
from events.models import Event
from django.shortcuts import get_object_or_404

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Successfully created account for {username}')

            #log in user & redirect to homepage
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('home-page')
    else:       
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {'form':form})
 
@login_required
def own_profile(request):
    if request.method== 'POST':
        u_form = UpdateUserForm(request.POST, instance = request.user)
        #request.FILES if form is handeling images, files etc.
        p_form = UpdateProfileForm(request.POST, request.FILES, 
                                    instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile Update Successfully !')
            return redirect('user-profile')
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)
    
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/my_profile.html', context)

def others_profile(request, pk):
    user = get_object_or_404(User ,id=pk)
    events = Event.objects.filter(publisher=user).all()
    return render(request, 'users/profile.html', {'user':user, 'events':events})