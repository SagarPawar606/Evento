from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.payment, name='event-payment'),
    path('razorresponse/', views.razorresponse, name='razor-post-response'),
]