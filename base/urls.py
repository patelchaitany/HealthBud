from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('room/',views.rooms)
]