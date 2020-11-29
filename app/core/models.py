from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# passing arg to class extends class passed as arg


class UserManager(BaseUserManager):
  # password=None is default arg in case when we want to create anonim
  # **extra_fields is like ...rest in js
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError('no email provided')
    user = self.model(email=self.normalize_email(email), **extra_fields)
    user.set_password(password)
    user.save(using=self._db)

    return user

  def create_superuser(self, email, password):
    user = self.create_user(email, password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)

    return user
# user model333


class User(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  # donno for what are these below
  objects = UserManager()
  USERNAME_FIELD = 'email'
