# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, AbstractUser
)
import datetime as dt
from eLearning.settings import FILES_URL


def upload_location_for_user(instance, filename):
    return 'lms/images/users/%s.%s' % (instance.id, filename.split('.')[1])
def upload_location_for_course(instance, filename):
    return 'lms/images/courses/%s.%s' % (instance.id, filename.split('.')[1])
def upload_location_for_file(instance, filename):
    return 'lms/files/%s/%s/%s.%s' % (instance.lecture.course, instance.lecture, instance.name, filename.split('.')[1])


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Course(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(max_length=255, upload_to=upload_location_for_course, db_column='image')
    publishdate = models.DateField(db_column='publishDate', default=dt.date.today)  # Field name made lowercase.
    price = models.IntegerField()
    description = models.TextField(max_length=10000, blank=True, null=True)
    #teacher = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='teacher', unique=False)  # Field name made lowercase.


    '''Add more attributes to configure with enrolled students'''


    class Meta:
        managed = False
        db_table = 'course'

    def __str__(self):
        return self.name


class Lecture(models.Model):
    #id = models.AutoField(primary_key=True, unique=True, db_column='id')
    name = models.CharField(max_length=255, db_column='name')
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, db_column='course')
    
    ### Delete after Unit being created
    #notes = models.TextField(blank=True, null=True, db_column='notes')
    #slide = models.FileField(upload_to=upload_location_for_file, db_column='slide', blank=True)
    ### Done

    class Meta:
        managed = False
        db_table = 'lecture'
    
    def __str__(self):
        return self.name


### Add later
class Unit(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    name = models.CharField(max_length=255, db_column='name', null=False)
    notes = models.TextField(blank=True, null=True, db_column='notes')
    slide = models.FileField(upload_to=FILES_URL, db_column='slide', blank=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.DO_NOTHING, db_column='lecture')
    video = models.URLField(max_length=255, db_column='video', null=True, blank=True)
    reading = models.CharField(max_length=255, db_column='reading', null=True, blank=True)
    quiz = models.OneToOneField('Quiz', on_delete=models.DO_NOTHING, db_column='quiz')

    class Meta:
        managed = False
        db_table ='unit'

    def __str__(self):
        return self.name + '-' + self.notes
    
    @property
    def get_slide_name(self):
        return self.slide.name[10:]
### Done


### Add later
### 14/10 Delete after modify Assignment
'''class Learn(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', unique=True)
    student = models.ForeignKey('Student', on_delete=models.DO_NOTHING, db_column='student')
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, db_column='unit')
    finished = models.BooleanField(blank=True, null=True, default=False, db_column='finished')

    class Meta:
        managed = False
        db_table = 'learn'

    def __str__(self):
        return self.student.email + '-' + self.unit.lecture.course.name + '-' + self.unit.lecture.name + '-' + self.unit.name'''
### Done


### 14/10 10pm
class Quiz(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    question = models.TextField(null=False, db_column='question')
    answer = models.TextField(blank=True, db_column='answer')
    ### Delete these 2 temporarily
    #starttime = models.DateTimeField(null=False, default=dt.datetime.now, db_column='starttime')
    #endtime = models.DateTimeField(null=False, db_column='endtime')
    finished = models.BooleanField(default=False, db_column='finished')
    
    class Meta:
        managed = False
        db_table = 'quiz'

    def __str__(self):
        return self.question


### Add later
class Assignment(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    finished = models.BooleanField(default=False, db_column='finished')
    ### Delete these 2 temporarily
    #starttime = models.DateTimeField(db_column='startTime', default=dt.datetime.now, null=False)
    #endtime = models.DateTimeField(db_column='endTime', null=False)
    grade = models.IntegerField(db_column='grade', null=True, blank=True)
    student = models.ForeignKey('Student', on_delete=models.DO_NOTHING, db_column='student')
    unit = models.OneToOneField(Unit, on_delete=models.DO_NOTHING, db_column='unit')

    class Meta:
        managed = False
        db_table = 'assignment'

    def __str__(self):
        return self.student.email + '-' + self.unit
### Done


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Enroll(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', unique=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student')  # Field name made lowercase.
    course = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course')  # Field name made lowercase.
    enrolldate = models.DateTimeField(db_column='enrollDate', default=dt.datetime.now)  # Field name made lowercase.
    expiredate = models.DateTimeField(db_column='expireDate', default=dt.datetime.now()+dt.timedelta(days=+90))  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'enroll'

    def __str__(self):
        return self.student.email + '-' + self.course.name


### Added 12/11/2020 6p.m
class Teach(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', unique=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, db_column='teacher')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course')

    class Meta:
        managed = False
        db_table = 'teach'

    def __str__(self):
        return self.teacher.email + '-' + self.course.name
###


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.active = True
        user.staff = True
        user.admin = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.active = True
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class Student(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=45)
    image = models.ImageField(max_length=255, upload_to=upload_location_for_user, db_column='image')
    joindate = models.DateTimeField(db_column='joinDate', default=dt.datetime.now)  # Field name made lowercase.
    useremail = models.OneToOneField('User', models.DO_NOTHING, db_column='userEmail')  # Field name made lowercase.

    ## New
    facebook = models.CharField(max_length=255, db_column='facebook', null=True)
    twitter = models.CharField(max_length=255, db_column='twitter', null=True)
    website = models.CharField(max_length=255, db_column='website', null=True)

    class Meta:
        managed = False
        db_table = 'student'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=45)
    image = models.ImageField(max_length=255, upload_to=upload_location_for_user, db_column='image')
    joindate = models.DateTimeField(db_column='joinDate')  # Field name made lowercase.
    currentdegree = models.CharField(db_column='currentDegree', max_length=45, blank=True, null=True)  # Field name made lowercase.
    useremail = models.OneToOneField('User', models.DO_NOTHING, db_column='userEmail')

    ## New
    facebook = models.CharField(max_length=255, db_column='facebook', null=True)
    twitter = models.CharField(max_length=255, db_column='twitter', null=True)
    website = models.CharField(max_length=255, db_column='website', null=True)

    class Meta:
        managed = False
        db_table = 'teacher'

    def __str__(self):
        return self.name


class User(AbstractBaseUser):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def __str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    '''@property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active'''

    class Meta:
        managed = False
        db_table = 'user'
