from rest_framework import serializers
from .models import Author
from django.contrib.auth import get_user_model, authenticate
# get_user_model fetches the currently active user model as defined in the Django settings.
# authenticate is used to authenticate a user based on provided credentials.

User = get_user_model() # get the current user  

class AuthorSerializer(serializers.ModelSerializer): 
    # AuthorSerializer is a Django REST Framework serializer class that maps the Author model fields to JSON data.
    # serializers.ModelSerializer is a class provided by Django REST Framework (DRF) that serves as a base class for creating serializers
    # Serializer: A serializer is a mechanism for "serializing" (converting) complex data types (like Django model instances) into native Python data types (like JSON) that can be easily rendered into HTTP responses.
    # ModelSerializer: ModelSerializer is a specialized serializer class in DRF designed to work with Django models. It automatically generates a set of fields for the serializer based on the model fields.

    class Meta: # inner class specifies metadata for the serializer.
        model = Author # specifies that this serializer is for the Author model.
        fields = ['id', 'username', 'email', 'bio', 'created_at'] # lists the fields from Author model that should be serialized.


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}} # specifies that the password field should be write-only (not serialized back in responses).


# create method overrides the default create behavior of the serializer. It creates a new user using User.objects.create_user with validated data (username, email, password).
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
# User.objects:
# User is typically the Django model representing the user in a Django project.
# objects is a manager provided by Django for interacting with the database.


# .create_user(...):
# method provided by Django's default UserManager (django.contrib.auth.models.UserManager).
# This method is used specifically for creating a new user instance and saving it to the database.

# self refers to the current instance of a class.
# special parameter that refers to the instance of a class. It's a convention in Python to use self as the first parameter in instance methods of a class
# It allows instance methods to access and manipulate instance attributes and methods.
# it clearly indicates that the method operates on the instance itself.


# serializers.ModelSerializer
# Purpose:

# serializers.ModelSerializer is a specialized serializer class provided by DRF that automatically generates serializer fields based on a Django model.
# It's used when you want to create serializers that directly map to and interact with Django models.
# Usage:

# Use serializers.ModelSerializer when you want to perform CRUD (Create, Read, Update, Delete) operations on Django models via RESTful APIs.
# It simplifies the process of defining serializers for Django models by automatically determining fields and validation rules based on the model definition.

class LoginSerializer(serializers.Serializer):
    # inherits from serializers.Serializer.
# serializers.Serializer
# Purpose:

# serializers.Serializer is a base class provided by DRF for defining custom serializers.
# It is used when you need to define a serializer that does not necessarily map directly to a Django model.
# Usage:

# Use serializers.Serializer when you want full control over how data is validated and serialized/deserialized.
# You explicitly define each field and its validation logic within the serializer class.
    username = serializers.CharField()
    password = serializers.CharField()

# username and password fields are defined using serializers.CharField().

    def validate(self, data): # validate method is overridden
        # data typically represents the dictionary of validated data passed to the serializer.
        user = authenticate(**data)
        # **data is Python syntax that unpacks the dictionary data into keyword arguments.
        if user and user.is_active: # In Django's User model (or a model that inherits from AbstractUser), is_active is a boolean field.
        # When is_active is True, it means the user account is active and operational.
        # When is_active is False, it typically means the user account has been deactivated or suspended, often by an administrator or through an automated process.
            return user
        raise serializers.ValidationError("Invalid username or password")
# raise is used to handle exceptional situations where normal execution cannot proceed.
# Typically used in conjunction with try and except blocks to catch and handle exceptions gracefully.




