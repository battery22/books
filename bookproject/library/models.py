from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import io
from PIL import Image
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

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
        # related_name="author",
        related_name="books",
    )
    rate = models.ForeignKey(
        "BookRating",
        on_delete=models.PROTECT,
        null=True,
        related_name="books",
        blank=True,
    )
    #  many to many
    genre = models.ManyToManyField("BookGenre", related_name="books", blank=True) 

    def __str__(self):
        return self.title
    
    def get_genres_display(self):
        genres = self.genre.all()
        return '\n'.join(genre.book_genre for genre in genres)
       # {{ book.get_genres_display|linebreaksbr }} in HTML

    class Meta:
        verbose_name_plural = "Книги" # for adm-pan


class BookAuthor(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    photo = ProcessedImageField(upload_to='authors/', 
                              processors=[ResizeToFill(300, 300)],
                              format='JPEG',
                              options={'quality': 70},
                              blank=True, 
                              null=True, 
                              default=None, 
                              verbose_name='Фото JPEG'
                              )
    photo_webp = ProcessedImageField(
        upload_to='authors/',
        processors=[ResizeToFill(300, 300)],
        format='WEBP',
        options={'quality': 70},
        blank=True,
        null=True,
        verbose_name='Фото (WebP)'
    )
    biography = models.TextField(blank=True, verbose_name='Биография')
    
    def get_absolute_url(self):
     return reverse('author', kwargs={'author_slug': self.slug})

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name_plural = "Автор"
    
    def save(self, *args, **kwargs):
        if self.photo:
            # save original
            img = Image.open(self.photo)
            # img = img.convert('RGB')
         
            # # create img WebP
            webp_image = io.BytesIO()
            img.save(webp_image, format='WEBP', quality=75)
            webp_image.seek(0)
            
            # save WebP
            self.photo_webp.save(f'{self.photo.name.split(".")[0]}.webp', 
                                 content=webp_image, 
                                 save=False)
        super(BookAuthor, self).save(*args, **kwargs)

class BookRating(models.Model):
    rating = models.PositiveIntegerField(blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])

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

class BookQuote(models.Model):
    text = models.CharField(max_length=255, blank=True, verbose_name='Цитата')
    
    book = models.ForeignKey(
        "BookName",
        on_delete=models.PROTECT,
        null=True,
        related_name='quotes'
    )
    
    def __str__(self):
        return self.text
    
    class Meta: 
        verbose_name = 'Цитата из книги' # adm-pan
        verbose_name_plural = 'Цитаты из книг'
        
            