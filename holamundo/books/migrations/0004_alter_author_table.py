# Generated by Django 4.0.3 on 2022-03-07 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_author_alter_author_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='author',
            table='authors',
        ),
    ]
