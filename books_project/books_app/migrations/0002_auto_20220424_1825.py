# Generated by Django 2.2.4 on 2022-04-24 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Publisher',
            new_name='Author',
        ),
    ]