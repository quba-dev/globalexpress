from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    patronymic = models.CharField(_('patronymic name'), max_length=150, blank=True, null=True)

    phone_message = 'Phone number must be entered in the format: 996 999 999 999'
    phone_regex = RegexValidator(
        regex=r'^(996)\d{9}$',
        message=phone_message
    )
    phone = models.CharField(validators=[phone_regex], max_length=12)

    telegram = models.CharField(
        _('Telegram'),
        max_length=150,
        blank=True,
        null=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    apartment = models.CharField(max_length=60)

    index_message = 'Index must be entered in the format: XX XX XX'
    index_regex = RegexValidator(
        regex=r'^\d{6}$',
        message=index_message
    )
    postcode = models.CharField(validators=[index_regex], max_length=6)

    scan_out = models.ImageField(upload_to='scan_out')
    scan_in = models.ImageField(upload_to='scan_in')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
