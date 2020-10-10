# Generated by Django 3.1.1 on 2020-10-08 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('joindate', models.DateTimeField(db_column='joinDate')),
                ('useremail', models.CharField(db_column='userEmail', max_length=45, unique=True)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45, unique=True)),
                ('joindate', models.DateTimeField(db_column='joinDate')),
                ('currentdegree', models.CharField(blank=True, db_column='currentDegree', max_length=45, null=True)),
            ],
            options={
                'db_table': 'teacher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='lms.teacher')),
                ('name', models.CharField(max_length=45)),
                ('publishdate', models.DateTimeField(db_column='publishDate')),
                ('price', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=45, null=True)),
                ('teacherid', models.IntegerField(db_column='teacherID', unique=True)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('studentid', models.ManyToManyField(db_column='studentID', serialize=False, unique=False, to='lms.student')),
                ('courseid', models.ManyToManyField(db_column='courseID', serialize=False, unique=False, to='lms.course')),
                ('enrolldate', models.DateTimeField(db_column='enrollDate')),
                ('expiredate', models.DateTimeField(db_column='expireDate')),
            ],
            options={
                'db_table': 'enroll',
                'managed': False,
            },
        ),
    ]
