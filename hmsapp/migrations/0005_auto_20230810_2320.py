# Generated by Django 3.0 on 2023-08-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0004_auto_20230810_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='pfupd',
        ),
        migrations.AddField(
            model_name='user',
            name='pfupd',
            field=models.BooleanField(default=False),
        ),
    ]
