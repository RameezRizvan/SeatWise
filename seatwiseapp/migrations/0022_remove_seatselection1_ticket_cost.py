# Generated by Django 4.2.4 on 2023-11-01 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seatwiseapp', '0021_seatselection1_delete_seatselection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seatselection1',
            name='ticket_cost',
        ),
    ]