# Generated by Django 5.0.7 on 2024-10-12 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='ReviewImage',
            field=models.ImageField(upload_to='tmp/static'),
        ),
    ]
