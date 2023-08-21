from django.urls import path
from . import views
from .views import (
    PostListView,
    TableCreateView,
)
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('table/new/', TableCreateView.as_view(), name='table-create'),
    path('table/<int:pk>/', views.table_detail, name='table-detail'),
]
