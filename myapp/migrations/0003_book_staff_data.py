# Generated by Django 4.2.1 on 2023-06-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_book_date_remove_book_dest_remove_book_nos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='staff_data',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
