

from django.urls import path
from library import views

urlpatterns = [
    path("", views.index, name='home')
]