# Generated by Django 3.1.7 on 2021-04-03 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20210404_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.cart', verbose_name='Корзина'),
        ),
    ]
