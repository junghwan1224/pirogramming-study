# Generated by Django 2.0.1 on 2018-02-02 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180202_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_day',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]