# Generated by Django 5.2.4 on 2025-08-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_unity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('TANGIBLE', "ushlab bo'ladigan"), ('INTANGIBLE', "ushlab bo'lmaydigan")], default='TANGIBLE', max_length=20),
        ),
    ]
