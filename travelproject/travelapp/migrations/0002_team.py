# Generated by Django 4.2.3 on 2023-07-12 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='tpics')),
                ('t_name', models.CharField(max_length=250)),
                ('about', models.TextField()),
            ],
        ),
    ]