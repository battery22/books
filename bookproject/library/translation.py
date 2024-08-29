from modeltranslation.translator import register, TranslationOptions
from .models import BookName, BookAuthor, BookGenre, BookQuote

@register(BookName)
class BookNameTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    
@register(BookAuthor)
class BookAuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'middle_name', 'biography')

@register(BookGenre)
class BookGenreTranslationOptions(TranslationOptions):
    fields = ('book_genre',)    
    
@register(BookQuote)
class BookQuoteTranslationOptions(TranslationOptions):
    fields = ('text',)    