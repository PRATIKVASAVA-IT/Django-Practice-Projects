# Generated by Django 5.1 on 2024-10-31 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custuser', '0004_alter_trackermodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackermodel',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='trackermodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]