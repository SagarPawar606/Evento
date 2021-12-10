from django.urls import path, reverse_lazy
from . import views
from .views import (ListViewEvent, DetailViewEvent, 
                    CreateViewEvent, UpdateViewEvent, 
                    DeleteViewEvent, MyEventList,
                    CategoricalEventList, PocketEventList,
                    Search, DeletePocketEvent,
                    CarouselList)


urlpatterns = [   
    path('', ListViewEvent.as_view(), name='home-page'),
    path('carousel/', CarouselList.as_view(), name='carousel'),
    path('pocket/', PocketEventList.as_view(), name='pocket'),
    path('pocket/<int:pk>/delete/', DeletePocketEvent.as_view(success_url=reverse_lazy('pocket')), name='pocket-delete'),
    path('search/', Search.as_view(), name='search-field'),
    path('myevent/', MyEventList.as_view(), name='myevent-page'),
    path('event/create/', CreateViewEvent.as_view(), name='event-create'),
    path('event/<int:pk>/', DetailViewEvent.as_view(), name='event-detail'),
    path('event/<int:pk>/update/', UpdateViewEvent.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', DeleteViewEvent.as_view(success_url=reverse_lazy('myevent-page')), name='event-delete'),
    path('event/<str:category>/', CategoricalEventList.as_view(), name='categorical-event'),
    
    path('api/', views.testapi, name='api-test'),
    path('api/pocketlist/<int:pk>/', views.pocket_items, name='api-pocket-list')
]
