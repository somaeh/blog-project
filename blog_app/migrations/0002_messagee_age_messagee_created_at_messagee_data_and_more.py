# Generated by Django 4.2.5 on 2024-04-01 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagee',
            name='age',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='messagee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='messagee',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 1, 16, 55, 34, 375497, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_data',
            field=models.DateField(default=datetime.datetime(2024, 4, 1, 16, 55, 34, 359867, tzinfo=datetime.timezone.utc)),
        ),
    ]
