# Generated by Django 3.1.1 on 2020-10-12 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_auto_20201012_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='id',
            field=models.IntegerField(db_column='id', primary_key=True, serialize=False, unique=True),
        ),
    ]
