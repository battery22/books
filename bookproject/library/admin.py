from django.contrib import admin

from .models import BookName, BookAuthor, BookRating, BookGenre


@admin.register(BookName)
class BookNameAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "year", "rate", "get_genres")
    list_editable = ("author", "year", "rate")
    list_display_links = ("title",)
    ordering = ("author__name",)
    list_per_page = 50
    search_fields = ["title", "author__name"]
    list_filter = ["author__surname"]
    filter_horizontal = ["genre"]

    def get_genres(self, bookname: BookName):
        return "\n".join([p.book_genre for p in bookname.genre.all()])
    get_genres.short_description = "Жанры"  # name in admin


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "middle_name")


@admin.register(BookRating)
class BookRatingAdmin(admin.ModelAdmin):
    list_display = ("rating",)


@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "book_genre",
    )
