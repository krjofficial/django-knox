from django.contrib.auth.models import AbstractUser
# Abstractuser is Django-provided abstract base class that provides the core implementation of a user model, including fields like username, email, password, etc.
from django.db import models
# models is imported from django.db, which allows defining Django models

class Author(AbstractUser): # Author is defined as a subclass of AbstractUser. inherits all the fields and methods of AbstractUser, such as username, email, password, etc. This approach is used to create a custom user model with additional fields or behavior beyond what is provided by AbstractUser.
    bio = models.TextField(blank=True, null=True) # allows for a longer text field to store
    created_at = models.DateTimeField(auto_now_add=True) # automatically sets the current date and time when an instance of Author is created 

def __str__(self): # method is used by Django admin and other places where string representation of objects is needed.
    return self.username


