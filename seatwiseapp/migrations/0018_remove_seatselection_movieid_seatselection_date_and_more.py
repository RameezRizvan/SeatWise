# Generated by Django 4.2.4 on 2023-10-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatwiseapp', '0017_remove_seatselection_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seatselection',
            name='movieid',
        ),
        migrations.AddField(
            model_name='seatselection',
            name='date',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seatselection',
            name='ticket_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='seatselection',
            name='time',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
