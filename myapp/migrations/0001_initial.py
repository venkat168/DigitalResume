# Generated by Django 4.1.2 on 2023-02-11 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('school', models.CharField(max_length=500)),
                ('diploma', models.CharField(max_length=500)),
                ('degree', models.CharField(max_length=500)),
                ('skill', models.TextField(max_length=200)),
                ('about_you', models.TextField(max_length=300)),
            ],
        ),
    ]
