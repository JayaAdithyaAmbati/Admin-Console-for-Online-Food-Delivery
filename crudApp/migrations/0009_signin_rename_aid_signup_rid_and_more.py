# Generated by Django 4.2.3 on 2023-07-29 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0008_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aid', models.CharField(max_length=50)),
                ('Apswd', models.CharField(max_length=35)),
            ],
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='Aid',
            new_name='Rid',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='Apswd',
            new_name='Rpswd',
        ),
    ]
