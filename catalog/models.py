from django.db import migrations, models
import datetime
from uuid import uuid4

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,AbstractUser
)
from django import db

class CustomUser(AbstractUser):
   
    status = (
        ('e', 'kid customer'),
        ('a', 'adult customer'),
        ('b', 'admin'),
        
    )
    position = models.CharField(
        max_length=1,
        choices=status,
        blank=False,
        default='e',
        help_text='Position Type',
    )
    
    profile_image = models.ImageField(default="default-profile.jpeg", null=True, blank=True)

# Create your models here.
class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)


    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.CharField(max_length=200)
    status = (
        ('e', 'under-eighteen'),
        ('a', 'adult'),
        
    )
    age_group = models.CharField(
        max_length=1,
        choices=status,
        blank=False,
        default='e',
        help_text='Book availability',
    )
    book_cover_image = models.ImageField(default="default-profile.jpeg", null=True, blank=True)

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """String for representing the Model object."""
        return self.title


