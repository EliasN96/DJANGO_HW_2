# Generated by Django 5.1 on 2024-09-09 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
