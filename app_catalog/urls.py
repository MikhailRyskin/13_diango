from django.urls import path, include
from app_catalog.api import AuthorList, BookList, AuthorDetail, BookDetail

urlpatterns = [
        path('authors/', AuthorList.as_view(), name='authors'),
        path('authors/<int:pk>', AuthorDetail.as_view(), name='author_detail'),
        path('books/', BookList.as_view(), name='books'),
        path('books/<int:pk>', BookDetail.as_view(), name='book_detail'),
]