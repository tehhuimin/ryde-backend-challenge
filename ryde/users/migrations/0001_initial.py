# Generated by Django 2.2.16 on 2021-11-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('zip_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('dob', models.DateField(null=True)),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]