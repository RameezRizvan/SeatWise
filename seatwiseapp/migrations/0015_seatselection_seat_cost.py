# Generated by Django 4.2.4 on 2023-09-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatwiseapp', '0014_rename_selectedseats_seatselection_selectedseats_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seatselection',
            name='seat_cost',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
    ]