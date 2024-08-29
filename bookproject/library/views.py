from django.shortcuts import get_object_or_404, render

from library.models import BookName, BookAuthor


def index(request):
 booknames = BookName.objects.select_related('author', 'rate').prefetch_related('genre', 'quotes').all()
 
 # Add the range calculation for star ratings
 for book in booknames: # fix it 
   if book.rate:
     book.stars = range(book.rate.rating)
   else:
     book.stars = range(0)  # Or use an empty range
 data = {"title": "Главная", "booknames": booknames}
 return render(request, "index.html", context=data)


def show_author(request, author_slug):
  # author = get_object_or_404(BookAuthor, slug=author_slug)
  author = get_object_or_404(BookAuthor.objects.prefetch_related('books'), slug=author_slug)
  data = {"title": "Биография одного автора",
          'author': author,
         }
  
  
  return render(request, "author.html", context=data)