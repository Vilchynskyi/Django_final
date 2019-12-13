from django.urls import path
from .views import (
    IndexView,
    BookDetailView,
    BookListView,
    CategoryView,
    CategoryListView,
)


app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug>/<pk>/', BookDetailView.as_view(), name='book'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<slug>,', CategoryView.as_view(), name='category'),
]
