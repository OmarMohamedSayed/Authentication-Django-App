from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class TimestampedModel(models.Model):
    """
    Abstract model to contain information about creation/update time.

    :created_at: date and time of record creation.
    :updated_at: date and time of any update happends for the record.
    """

    created_at = models.DateTimeField(
        verbose_name='Creation Date/Time', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Update Date/Time', auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']

class Profile(TimestampedModel):
    """
    Profile model to contain information about users.

    :first_name: char-field to store firstname of the user.
    :last_name: char-field to store lastname of the user.
    :country_code: char-field to store country code of the user. (eg:'EG')
    :phone_number: char-field to store phone number of the user. (unique) (eg:'0111111111')
    :gender: choice-field to store gender of the user.
    :birthdate: char-field to store birthdate of the user. (eg: '2000-01-01')
    :avatar: Image field to store avatar of the user and save it in media/images folder. (accept: jpg, png, jpeg)
    :email: char-field to store email of the user.
    """
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    country_code = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=11,unique=True, primary_key=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    gender = models.CharField(max_length=150, choices=GENDER_CHOICES, blank=True, null=True)
    birthdate = models.CharField(max_length=150, blank=True, null=True)
    avatar = models.ImageField(upload_to='images',blank=True, null=True)  
    email = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Profile'
    def __str__(self):
        return self.phone_number  
    