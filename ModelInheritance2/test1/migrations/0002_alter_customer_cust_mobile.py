# Generated by Django 5.1 on 2024-10-05 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cust_mobile',
            field=models.IntegerField(default=True, null=True),
        ),
    ]