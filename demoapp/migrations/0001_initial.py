# Generated by Django 5.0.3 on 2024-03-14 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('location', models.CharField(max_length=125)),
                ('employee_count', models.IntegerField(default=0)),
                ('office_count', models.IntegerField(default=0)),
                ('turnover', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('age', models.IntegerField(default=18)),
                ('house_name', models.CharField(max_length=225)),
                ('street', models.CharField(max_length=225)),
                ('city', models.CharField(max_length=225)),
                ('state', models.CharField(max_length=225)),
                ('pincode', models.CharField(max_length=225)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demoapp.company')),
            ],
        ),
    ]
