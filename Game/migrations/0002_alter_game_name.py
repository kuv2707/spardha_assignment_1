# Generated by Django 4.2.4 on 2023-08-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
