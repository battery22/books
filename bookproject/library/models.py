from django.db import models



class BookName(models.Model):
  title = models.CharField(max_length=255, verbose_name="Название")
  description = models.TextField(blank=True)
  link = models.URLField(blank=True)
  year = models.CharField(max_length=255, blank=True)
  
      # one to many
  author = models.ForeignKey(
    "BookAuthor", 
     on_delete=models.PROTECT, 
     null=True, 
     related_name="author",
  )
  rate = models.ForeignKey(
    "BookRating",
    on_delete=models.PROTECT,
    null=True,
    related_name="rate",
    blank=True,
  )
   # доп. таблицы many to many
  genre = models.ManyToManyField(
    "BookGenre", 
    related_name="genre", 
    blank=True
  )

  def __str__(self):
    return self.title

  class Meta:
    verbose_name_plural = "Книги"  


class BookAuthor(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
      return f"{self.name} {self.surname} {self.middle_name}"

    class Meta:
     verbose_name_plural = "Автор"   
    
class BookRating(models.Model):
    # objects = None
    rating = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.rating   

    class Meta:
     verbose_name_plural = "Рейтинг"      
    
class BookGenre(models.Model):
    # objects = None
    book_genre = models.CharField(max_length=255)

    def __str__(self):
        return self.book_genre    

    class Meta:
      verbose_name_plural = "Жанр"     