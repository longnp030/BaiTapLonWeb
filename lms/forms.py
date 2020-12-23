from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.forms.widgets import URLInput
from django.utils.translation import gettext_lazy as _
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', ]


class StudentInfoForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput, required=False)
    facebook = forms.URLField(widget=forms.URLInput, required=False)
    twitter = forms.URLField(widget=forms.URLInput, required=False)
    website = forms.URLField(widget=forms.URLInput, required=False)

    class Meta:
        model = Student
        fields = ['image', 'facebook', 'twitter', 'website', ]


class AddTeacherForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    class Meta:
        model = Teach
        fields = ['teacher', 'course',]


'''class TeachForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())

    class Meta:
        model = Teach
        fields = ['teacher', 'course',]'''


class TeacherInfoForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput, required=False, localize=True)
    facebook = forms.URLField(widget=forms.URLInput, required=False)
    twitter = forms.URLField(widget=forms.URLInput, required=False)
    website = forms.URLField(widget=forms.URLInput, required=False)

    class Meta:
        model = Teacher
        fields = ['image', 'facebook', 'twitter', 'website', ]


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        queryset = User.objects.filter(email=email)
        if queryset.exists():
            raise forms.ValidationError("Email existed")
        return email
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', ]


class TeacherRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    staff = forms.BooleanField(label='I agree to the Terms and Conditions.', initial=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'staff', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        queryset = User.objects.filter(email=email)
        if queryset.exists():
            raise forms.ValidationError("Email existed")
        return email
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(TeacherRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class CourseCreateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput, required=False)
    
    class Meta:
        model = Course
        fields = ['id', 'image', 'name', 'description', ]


class LectureCreateForm(forms.ModelForm):
    notes = forms.TextInput()
    slide = forms.FileField(widget=forms.FileInput, required=False)
    video = forms.URLField(widget=forms.URLInput, required=False)
    reading = forms.TextInput()

    class Meta:
        model = Lecture
        fields = ['course', 'name', 'notes', 'slide', 'video', 'reading', ]


class AssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['student', 'finished', ]


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enroll
        fields = ['student', 'course',]
