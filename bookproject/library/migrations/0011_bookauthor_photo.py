# Generated by Django 5.1 on 2024-08-25 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0010_bookauthor_biography_bookauthor_biography_en_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookauthor",
            name="photo",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                upload_to="authors/",
                verbose_name="Фото",
            ),
        ),
    ]
