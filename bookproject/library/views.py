from django.shortcuts import render
from library.models import BookName
menu = ["about", "contacts"]


def index(request):
 booknames = BookName.objects.select_related('author', 'rate').prefetch_related('genre').all()
 # Add the range calculation for star ratings
 for book in booknames: # fix it 
   if book.rate:
     book.stars = range(book.rate.rating)
   else:
     book.stars = range(0)  # Or use an empty range
 data = {"title": "Главная", "booknames": booknames}
 return render(request, "index.html", context=data)
