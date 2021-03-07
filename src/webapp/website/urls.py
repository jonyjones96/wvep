
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('item/<id>', views.getItem, name='website-item'),
    path('basket', views.getBasket, name='website-basket'),
    path('track', views.getTracking, name='website-tracker'),
]
