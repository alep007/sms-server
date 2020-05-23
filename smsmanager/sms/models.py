from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.conf import settings


#TODO: verify on the django docs

class UserManager(BaseUserManager):

    def create_user(self, short_name, name, password=None, **extra_fields):

        if not short_name:
            raise ValueError('Users must have an email address')
        user = self.model(short_name=short_name, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, short_name, name, password):
        """Creates and saves a new superuser"""
        user = self.create_user(short_name, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Professor(AbstractBaseUser, PermissionsMixin):
    # overwriting user
    short_name = models.IntegerField
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # faculty etc,
    objects = UserManager()

    USERNAME_FIELD = 'short_name'


class Career(models.Model):
    short_name = models.CharField(max_length=200)  # mat101
    name = models.CharField(max_length=200)  # calculo I


class Subject(models.Model):
    short_name = models.CharField(max_length=200)  # mat101
    name = models.CharField(max_length=200)  # calculo I

    career = models.ForeignKey(
        'Career', on_delete=models.CASCADE
    )

    semester = models.IntegerField
    # add fk to professor.... should be many to many?


class ProfessorSubject(models.Model):

    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    subject = models.ForeignKey(
        'Subject', on_delete=models.CASCADE
    )


class Group(models.Model):
    short_name = models.CharField(max_length=200)  # mat101
    name = models.CharField(max_length=200)  # calculo I

    subject = models.ForeignKey(
        'Subject', on_delete=models.CASCADE
    )

    # TODO: probably add a schedule here


class Student(models.Model):
    short_name = models.CharField(max_length=15)  # 212072542
    name = models.CharField(max_length=200)  # alguien que tiene nombre
    # should add the country code
    phone_number = models.CharField(max_length=20)  # 59173496410
    email = models.CharField(max_length=100)

    career = models.ForeignKey(
        'Career', on_delete=models.CASCADE
    )


class StudentGroup(models.Model):
    group = models.ForeignKey(
        'Group', on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        'Student', on_delete=models.CASCADE
    )


class Message(models.Model):
    short_name = models.CharField(max_length=100)
    body = models.CharField(max_length=255)
    category = models.CharField(max_length=200)

    group = models.ForeignKey(
        'Group', on_delete=models.CASCADE
    )
    # example
    # subject.name : subject.short_name - Grupo subject.group
    # Estimados estudiantes, el examen sera el dia xxx
    # en el aula birhguwhuwefe

    # 1600 characters...


class MessageLog(models.Model):
    message = models.ForeignKey(
        'Message', on_delete=models.CASCADE
    )

    student = models.ForeignKey(
        'Student', on_delete=models.CASCADE
    )


# TODO: add timestamps for evertyhing createdOn, updatedOn
