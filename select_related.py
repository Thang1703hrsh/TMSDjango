from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    public_at = models.DateField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', related_name='books')

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=200)
    dob = models.DateField()

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    
def book_list():
    queryset = Book.objects.all()

    books = []
    for book in queryset:
        books.append({'name': book.name, 'author': book.author.full_name})

    return books

def book_list():
    queryset = Book.objects.select_related('author')

    books = []

    for book in queryset:
        books.append({'name': book.name, 'author': book.author.full_name})

    return books