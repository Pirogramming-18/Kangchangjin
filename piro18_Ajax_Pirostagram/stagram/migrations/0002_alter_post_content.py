# Generated by Django 4.1.5 on 2023-01-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=500),
        ),
    ]
