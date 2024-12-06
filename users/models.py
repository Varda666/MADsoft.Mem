
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class MyUserManager(UserManager):
    def create_user(self, email, name, password):
        if not email:
            raise ValueError('email не должен быть пустым')
        if not name:
            raise ValueError('name не должен быть пустым')
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email')
    name = models.CharField(max_length=150, verbose_name='имя')

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




