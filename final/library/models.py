from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True) 

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    genre = models.ManyToManyField('Genre', help_text='Select a genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    available_copies = models.PositiveIntegerField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE, null=True)

    def count_available_copies(self):
        return self.available_copies

    def __str__(self):
        return self.title

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    date_of_birth = models.DateField()
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.user} - {self.book.title}'
