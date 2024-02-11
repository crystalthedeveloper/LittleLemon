from django.contrib import admin 
from django.urls import path 
from . import views
from rest_framework.routers import DefaultRouter
from .views import MenuItemView, BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [ 
   #path('', sayHello, name='sayHello'), 
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    
]