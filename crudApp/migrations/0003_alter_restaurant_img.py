# Generated by Django 4.2.2 on 2023-07-27 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0002_restaurant_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
