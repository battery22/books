# Generated by Django 4.2.1 on 2024-08-19 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BookAuthor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("surname", models.CharField(max_length=255)),
                ("middle_name", models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="BookGenre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("book_genre", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="BookRating",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rating", models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="BookName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("link", models.URLField(blank=True)),
                ("year", models.CharField(blank=True, max_length=255)),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="author",
                        to="library.bookauthor",
                    ),
                ),
                (
                    "genre",
                    models.ManyToManyField(
                        blank=True, related_name="genre", to="library.bookgenre"
                    ),
                ),
                (
                    "rate",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="rate",
                        to="library.bookrating",
                    ),
                ),
            ],
        ),
    ]
