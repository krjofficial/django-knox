from django.apps import AppConfig
# AppConfig is a base class Django provides to define configuration for a Django application.


class AuthorsConfig(AppConfig): # AuthorsConfig inherits from AppConfig
    default_auto_field = 'django.db.models.BigAutoField'
     # specifies the default primary key field type for models within the authors app. In this case, it's set to BigAutoField, which is a 64-bit integer primary key field that automatically increments. 
    name = 'authors'
    # the name of the app. It's used to identify the app in Django's URL configuration and database migrations.
