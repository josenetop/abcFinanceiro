from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.utils.translation import ugettext_lazy as _
import re
from django.utils import timezone
# Create your models here.

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('O nome de usuário fornecido deve ser definido'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None,password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(username, email, password, **extra_fields):
        user=self._create_user(username, email, password, True, True, **extra_fields)
        user.is_staff=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(_('username'), max_length=45, unique=True)
    first_name = models.CharField(_('first name'), max_length=45, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=45, null=True, blank=True)
    email = models.CharField(_('email'), max_length=75, unique=True)
    is_staff  = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    is_trusty = models.BooleanField(_('trusty'), default=False, help_text=_('Designa se este usuário confirmou sua conta.'))
    
    USERNAME_FIELD = 'email'
    #USERNAME_FIELD: essa variável recebe o campo do model que será utilizado pelo Django para autenticação. 
    #É aqui que ao invés de username do model default, eu coloco email para fazer o login pelo email do usuário.

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    #REQUIRED_FIELDS: os campos que são obrigatórios desse model. 

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.last_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])