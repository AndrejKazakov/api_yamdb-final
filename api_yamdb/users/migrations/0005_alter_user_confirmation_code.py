# Generated by Django 3.2 on 2023-04-06 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=36, null=True, verbose_name='Код подтверждения'),
        ),
    ]
