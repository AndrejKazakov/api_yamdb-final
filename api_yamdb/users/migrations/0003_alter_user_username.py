# Generated by Django 3.2 on 2023-03-29 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230329_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=149, unique=True, verbose_name='Имя пользователя'),
        ),
    ]
