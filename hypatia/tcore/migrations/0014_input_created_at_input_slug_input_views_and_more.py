# Generated by Django 5.0.2 on 2024-05-15 20:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcore', '0013_alter_about_content_alter_about_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Oluşturulma Tarihi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='input',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='input',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Görüntülenme Sayısı'),
        ),
        migrations.AlterField(
            model_name='input',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Başlık'),
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
