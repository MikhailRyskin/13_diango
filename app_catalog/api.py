from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app_catalog.models import Author, Book
from app_catalog.serializers import AuthorSerializer, BookSerializer


class AuthorList(ListCreateAPIView):
    """Представление для получения списка авторов и создания нового автора.
       Возможна фильтрация по имени автора."""
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        first_name = self.request.query_params.get('first_name')
        if first_name:
            queryset = queryset.filter(first_name=first_name)
        return queryset


class AuthorDetail(RetrieveUpdateDestroyAPIView):
    """Представление для получения детальной информации об авторе,
         а также для редактирования и удаления"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookList(ListCreateAPIView):
    """Представление для получения списка книг и создания новой книги.
        Возможна фильтрация по фамилии автора и названию книги,
        по количеству страниц(меньше, равно, больше"""
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        if self.request.query_params:
            author = self.request.query_params.get('author')
            if author:
                if Author.objects.filter(last_name=author).exists():
                    book_author = Author.objects.get(last_name=author)
                    queryset = queryset.filter(author=book_author)
            title = self.request.query_params.get('title')
            if title:
                queryset = queryset.filter(title=title)
            operation = self.request.query_params.get('operation')
            page = self.request.query_params.get('page')
            if operation in ['exact', 'gt', 'lt'] and page:
                numbers_pages_filters = {f'number_of_pages__{operation}': page}
                queryset = queryset.filter(**numbers_pages_filters)
        return queryset


class BookDetail(RetrieveUpdateDestroyAPIView):
    """Представление для получения детальной информации о книге,
             а также для редактирования и удаления"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
