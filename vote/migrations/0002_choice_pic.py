# Generated by Django 4.1 on 2022-08-30 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='pic',
            field=models.ImageField(default='', upload_to='media/'),
        ),
    ]
