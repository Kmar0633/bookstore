from django.db import migrations, models
import datetime
from uuid import uuid4

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,AbstractUser
)
from django import db

class CustomUser(AbstractUser):
    
    """
    Stores a single user for the bookstore with attributes such as their role position and profile image 
    """

    status = (
        ('e', 'kid customer'),
        ('a', 'adult customer'),
        ('b', 'admin'),
        
    )

    # the role position attribute which allows users to select from 3 different options: kid customer, adult customer and admin. 
    position = models.CharField(
        max_length=1,
        choices=status,
        blank=False,
        default='e',
        help_text='Position Type',
    )
    
     # profile image attribute allows the user to upload a profile picture in the web app 
    profile_image = models.ImageField(default="default-profile.jpeg", null=True, blank=True)

    


class Book(models.Model):
    
    """
    Stores a single book for the bookstore with attributes such as their title, author, age group and booc cover image
    """
      # book title attribute 
    title = models.CharField(max_length=200)


    
    # book author attribute 
    author = models.CharField(max_length=200)
    status = (
        ('e', 'under-eighteen'),
        ('a', 'adult'),
        
    )
      # age group attribute which determines the age group suited to read the book- has 2 fixed choices:an under-eighteen book
      # or adult book
    age_group = models.CharField(
        max_length=1,
        choices=status,
        blank=False,
        default='e',
        help_text='Book availability',
    )

    # book cover image attribute which consists of an image of the book cover
    book_cover_image = models.ImageField(default="default-profile.jpeg", null=True, blank=True)

  

    def __str__(self):
        """String for representing the Model object."""
        return self.title


