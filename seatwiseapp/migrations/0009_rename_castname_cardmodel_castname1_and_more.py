# Generated by Django 4.2.4 on 2023-09-06 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatwiseapp', '0008_rename_castimg_cardmodel_castimg1_cardmodel_castimg2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardmodel',
            old_name='castname',
            new_name='castname1',
        ),
        migrations.AddField(
            model_name='cardmodel',
            name='castname2',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cardmodel',
            name='castname3',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cardmodel',
            name='castname4',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cardmodel',
            name='castname5',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]