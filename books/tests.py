from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(title='Harry Potter', author='JK Rowling', price='25.00')

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')
