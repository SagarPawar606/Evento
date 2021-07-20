from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [   
    #user/<urlpath>
    path('registration/', views.register, name='user-register'),
    path('my-profile/', views.own_profile, name='user-profile'),
    path('profile/<int:pk>/', views.others_profile, name='others-profile'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]

"""
To redirect user to home page add
LOGIN_REDIRECT_URL = 'home-page'
in settings.py file
"""