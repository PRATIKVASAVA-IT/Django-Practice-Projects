# Generated by Django 5.1 on 2024-12-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='customer_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
