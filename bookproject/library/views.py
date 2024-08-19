from django.shortcuts import render

menu = ['about', 'contacts']

def index(request):
  data = {
    'title': 'Главная',
    'menu': menu,
  }
  return render(request,'index.html', context=data)