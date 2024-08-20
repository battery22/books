from django.shortcuts import render
from library.models import BookName

menu = ['about', 'contacts']

def index(request):
  ff = BookName.objects.all()
  data = {
    'title': 'Главная',
    'menu': menu,
    'ff': ff,
  }
  return render(request,'index.html', context=data)