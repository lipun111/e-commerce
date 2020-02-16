# Generated by Django 3.0 on 2020-01-14 07:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200113_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]