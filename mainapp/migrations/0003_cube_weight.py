# Generated by Django 3.1.7 on 2021-03-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_cube_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='cube',
            name='weight',
            field=models.CharField(default=1, max_length=255, verbose_name='Вес'),
            preserve_default=False,
        ),
    ]
