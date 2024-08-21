from modeltranslation.translator import register, TranslationOptions
from .models import BookName, BookAuthor, BookGenre

@register(BookName)
class BookNameTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    
@register(BookAuthor)
class BookAuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'middle_name')

@register(BookGenre)
class BookGenreTranslationOptions(TranslationOptions):
    fields = ('book_genre',)    