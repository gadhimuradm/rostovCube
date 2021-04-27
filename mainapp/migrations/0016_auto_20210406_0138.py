# Generated by Django 3.1.7 on 2021-04-05 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0015_productfeatures_productfeaturesvalidator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productfeaturesvalidator',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productfeaturesvalidator',
            name='feature',
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.DeleteModel(
            name='ProductFeatures',
        ),
        migrations.DeleteModel(
            name='ProductFeaturesValidator',
        ),
    ]
