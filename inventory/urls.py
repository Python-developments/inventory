from django.urls import path
from .views import staff, home

urlpatterns = [
    path('', home),
    path('staff/', staff),
]
