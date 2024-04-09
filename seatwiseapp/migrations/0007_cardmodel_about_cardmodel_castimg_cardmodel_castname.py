# Generated by Django 4.2.4 on 2023-09-06 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatwiseapp', '0006_cardmodel_duration_cardmodel_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardmodel',
            name='about',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cardmodel',
            name='castimg',
            field=models.FileField(default=1, upload_to='seatwiseapp/static'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cardmodel',
            name='castname',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
