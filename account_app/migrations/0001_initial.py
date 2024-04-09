# Generated by Django 4.2.5 on 2023-09-25 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password1', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]