from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,AbstractUser
)


class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    mailing_address = models.CharField(max_length=200, blank=True)
    

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
    image = models.CharField('image', max_length=13, unique=True,
                             help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """String for representing the Model object."""
        return self.title

