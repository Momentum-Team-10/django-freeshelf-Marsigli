# Generated by Django 3.2.9 on 2021-11-09 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='url',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='author_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
