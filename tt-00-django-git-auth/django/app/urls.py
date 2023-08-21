from django.contrib.auth import views as auth_views
from django.urls import path
from .views import Home
from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('sign-up/', views.signup, name='sign-up'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='app/logout.html'),
         name='logout'),
]
