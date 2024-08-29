
from library import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='home'),
    path('author/<slug:author_slug>/', views.show_author, name='author'),
    
] 