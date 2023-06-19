from django.shortcuts import render
from .models import Author, Publisher, Library, Book, User, Review

def create_authors():
    authors = [
        {
            'first_name': 'Dorothy',
            'last_name': 'L. Sayers',
            'date_of_birth': '1893-06-13',
            'date_of_death': '1957-12-17'
        },
        {
            'first_name': 'Raymond',
            'last_name': 'Chandler',
            'date_of_birth': '1888-07-23',
            'date_of_death': '1959-03-26'
        },
        # добавьте больше записей
    ]

    for author in authors:
        author_obj = Author(**author)
        author_obj.save()

def create_publishers():
    publishers = [
        {
            'name': 'Vintage',
            'city': 'London',
            'website': 'https://www.vintage-books.co.uk/'
        },
        {
            'name': 'Penguin Random House',
            'city': 'New York',
            'website': 'https://www.penguinrandomhouse.com/'
        },
        # добавьте больше записей
    ]

    for publisher in publishers:
        publisher_obj = Publisher(**publisher)
        publisher_obj.save()

def create_libraries():
    libraries = [
        {
            'name': 'British Library',
            'address': '96 Euston Rd, London',
            'phone': '+44 20 7412 7676'
        },
        {
            'name': 'Library of Congress',
            'address': '101 Independence Ave SE, Washington',
            'phone': '+44 20 7412 7676'
        },
        # добавьте больше записей
    ]

    for library in libraries:
        library_obj = Library(**library)
        library_obj.save()

def create_books():
    books = [
        {
            'title': 'Murder Must Advertise',
            'author': Author.objects.get(last_name='Sayers'),
            'publisher': Publisher.objects.get(name='Vintage'),
            'isbn': '9780099573626',
            'summary': 'A classic mystery novel featuring Lord Peter Wimsey.',
            'language': Language.objects.get(name='English'),
            'available_copies': 5,
            'library': Library.objects.get(name='British Library')
        },
        {
            'title': 'The Big Sleep',
            'author': Author.objects.get(last_name='Chandler'),
            'publisher': Publisher.objects.get(name='Penguin Random House'),
            'isbn': '9780394758282',
            'summary': 'A classic detective novel featuring Philip Marlowe.',
            'language': Language.objects.get(name='English'),
            'available_copies': 3,
            'library': Library.objects.get(name='Library of Congress')
        },
        # добавьте больше записей
    ]

    for book in books:
        book_obj = Book(**book)
        book_obj.save()

def create_users():
    users = [
        {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'date_of_birth': '1990-01-01'
        },
        {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane.doe@example.com',
            'date_of_birth': '1992-06-21'
        },
        # добавьте больше записей
        ]

    for user in users:
        user_obj = User(**user)
        user_obj.save()

def create_reviews():
    reviews = [
        {
            'user': User.objects.get(email='john.doe@example.com'),
            'book': Book.objects.get(title='Murder Must Advertise'),
            'rating': 4,
            'comment': 'Great book!'
        },
        {
            'user': User.objects.get(email='jane.doe@example.com'),
            'book': Book.objects.get(title='The Big Sleep'),
            'rating': 5,
            'comment': 'Awesome book!'
        },
        # добавьте больше записей
    ]

    for review in reviews:
        review_obj = Review(**review)
        review_obj.save()