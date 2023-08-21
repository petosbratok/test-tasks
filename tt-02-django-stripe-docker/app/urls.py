from django.urls import path
from . import views
from .views import (
    Buy,
)

urlpatterns = [
    path('item/<str:pk>/', views.item, name="item"),
    path('buy/<str:pk>/', Buy.as_view(), name='buy'),
]
