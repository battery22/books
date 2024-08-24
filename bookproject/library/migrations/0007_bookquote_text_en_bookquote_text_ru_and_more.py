# Generated by Django 5.1 on 2024-08-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0006_alter_bookname_author_alter_bookname_genre_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookquote",
            name="text_en",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Цитата"
            ),
        ),
        migrations.AddField(
            model_name="bookquote",
            name="text_ru",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Цитата"
            ),
        ),
        migrations.AddField(
            model_name="bookquote",
            name="text_uk",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Цитата"
            ),
        ),
    ]
