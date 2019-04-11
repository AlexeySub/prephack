from django.db import models
from datetime import datetime


class User(models.Model):
    id = models.AutoField(primary_key=True, null=None, unique=True)
    name = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=32, unique=True)
    password = models.CharField(max_length=100)

    STUDENT = 'ST'
    TEACHER = 'TC'
    USER_TYPE = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    )
    userType = models.CharField(
        max_length=2,
        choices=USER_TYPE,
        null=None
    )


class UserAuthen(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, primary_key=True, null=None, unique=True)
    token = models.CharField(max_length=300)
    is_authenticated = models.BooleanField(default=False)


class Message(models.Model):
    id = models.AutoField(primary_key=True, null=None, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=None)
    date = models.DateTimeField(auto_now=True)
    text = models.TextField()
