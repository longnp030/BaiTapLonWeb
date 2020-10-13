# Generated by Django 3.1.1 on 2020-10-13 08:00

import datetime
from django.db import migrations, models
import lms.models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0008_auto_20201012_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('finished', models.BooleanField(blank=True, db_column='finished', default=False, null=True)),
                ('starttime', models.DateTimeField(db_column='startTime', default=datetime.datetime.now)),
                ('endtime', models.DateTimeField(db_column='endTime')),
                ('grade', models.IntegerField(db_column='grade', default=0)),
            ],
            options={
                'db_table': 'assignment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Learn',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('finished', models.BooleanField(blank=True, db_column='finished', default=False, null=True)),
            ],
            options={
                'db_table': 'learn',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('notes', models.TextField(blank=True, db_column='notes', null=True)),
                ('slide', models.FileField(blank=True, db_column='slide', upload_to=lms.models.upload_location_for_file)),
            ],
            options={
                'db_table': 'unit',
                'managed': False,
            },
        ),
    ]
