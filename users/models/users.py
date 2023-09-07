from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = PhoneNumberField('Phone', null=True, blank=True, unique=True)

    # USERNAME_FIELD = ''
    # REQUIRED_FIELDS = []
    class Meta:
        # db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
