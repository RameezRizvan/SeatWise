# Generated by Django 4.2.4 on 2023-08-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatwiseapp', '0002_cardmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardmodel',
            name='image',
            field=models.FileField(upload_to='seatwiseapp/static'),
        ),
    ]