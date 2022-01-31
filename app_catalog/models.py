from django.db import models


class Author(models.Model):
    """Модель автора."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Book(models.Model):
    """Модель книги."""
    title = models.CharField(max_length=200)
    isbn = models.CharField('ISBN', max_length=13)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    published_year = models.IntegerField(blank=True, null=True)
    number_of_pages = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
