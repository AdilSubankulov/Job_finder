# Generated by Django 5.0.4 on 2024-04-19 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('company', models.CharField(max_length=50)),
                ('posted_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=20)),
                ('Firstname', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]
