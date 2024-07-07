from django.urls import path
from knox import views as knox_views
from .views import AuthorList, AuthorDetail, RegisterAPI, LoginAPI

urlpatterns = [
    path('', AuthorList.as_view(), name='author-list'),
    path('<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]


# When you define a URL pattern for a CBV in urlpatterns, you use .as_view() to convert the class-based view into a callable view function that Django's URL resolver can understand.
#This method is necessary because Django's URL resolver expects a callable (a function or a class-based view that behaves like a function) to handle requests.
