# Generated by Django 3.1 on 2020-10-22 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='editdate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date edited'),
        ),
    ]
