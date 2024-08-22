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
    #  many to many
    genre = models.ManyToManyField("BookGenre", related_name="genre", blank=True) 

    def __str__(self):
        return self.title
    
    def get_genres_display(self):
        genres = self.genre.all()
        return '\n'.join(genre.book_genre for genre in genres)
       # {{ book.get_genres_display|linebreaksbr }} in HTML

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
    rating = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return f"{self.rating}"

    class Meta:
        verbose_name_plural = "Рейтинг"


class BookGenre(models.Model):
    book_genre = models.CharField(max_length=255)

    def __str__(self):
        return self.book_genre

    class Meta:
        verbose_name_plural = "Жанр"
