# Generated by Django 4.2.3 on 2023-07-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0006_alter_restaurant_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='restaurant_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]