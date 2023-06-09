# Generated by Django 4.2.1 on 2023-06-02 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='dest',
        ),
        migrations.RemoveField(
            model_name='book',
            name='nos',
        ),
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.RemoveField(
            model_name='book',
            name='source',
        ),
        migrations.RemoveField(
            model_name='book',
            name='time',
        ),
        migrations.AddField(
            model_name='book',
            name='form_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='venueid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.venue'),
        ),
    ]
