from rest_framework import generics # generics: This module from DRF provides a set of reusable generic views for common CRUD operations.
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer
from knox.models import AuthToken
from django.contrib.auth import login 
from .serializers import RegisterSerializer, LoginSerializer


class AuthorList(generics.ListCreateAPIView): #provides a view for listing a queryset or creating a model instance.
    queryset = Author.objects.all() # Retrieves all Author objects from the database.
    serializer_class = AuthorSerializer #  Specifies the serializer class (AuthorSerializer) to use for serializing and deserializing Author instances.


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView): # provides a view for retrieving, updating, or deleting a single model instance.
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class RegisterAPI(generics.GenericAPIView): # GenericAPIView provides base functionality for API views.
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs): #  handles POST requests. 
        serializer = self.get_serializer(data=request.data) # Instantiates the serializer with the request data.
        # self.get_serializer() is a method provided by GenericAPIView.
        # the data of request is getting serialized and stored in the serializer
        serializer.is_valid(raise_exception=True) # If the data is invalid, it raises an exception.
        user = serializer.save()
        return Response({ # returns an HTTP response
            "user": RegisterSerializer(user, context=self.get_serializer_context()).data, 
            "token": AuthToken.objects.create(user)[1] # creates an authentication token for the user and includes it in the response.
        })
    # Returns a JSON response containing the serialized user data (user) and an authentication token (token).
    


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response({
            "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# context is an optional argument that can be passed to the serializer. 
# is used to generate a dictionary that contains any context data you want to pass to the serializer. By default, it includes:
# request: The current request object.
# format: The format suffix (if any).
# view: The view instance that is calling the serializer.
# .data attribute contains the serialized representation of the object, which is typically a dictionary that can be easily converted to JSON.

