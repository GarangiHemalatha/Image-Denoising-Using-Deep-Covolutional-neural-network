# Generated by Django 4.2.6 on 2023-12-28 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_oil_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oil',
            name='image',
            field=models.ImageField(upload_to='static/upload/'),
        ),
    ]
