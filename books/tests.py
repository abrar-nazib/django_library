# Importing necessary modules for testing
from django.test import TestCase
from django.urls import reverse
from .models import Book  # Importing the Book model from the current module

# Create your tests here.
class BookTests(TestCase):  # Creating a test class that inherits from Django's TestCase class

    @classmethod
    def setUpTestData(cls) -> None:  # Method to set up test data before running the tests
        cls.book = Book.objects.create(  # Creating a Book object for testing purposes
            title="A book title",
            subtitle="A subtitle",
            author="The author",
            isbn="1234567890123"
        )

    def test_book_content(self):  # Test method to check the content of the Book object
        self.assertEqual(self.book.title, "A book title")  # Asserting that the title matches
        self.assertEqual(self.book.subtitle, "A subtitle")  # Asserting that the subtitle matches
        self.assertEqual(self.book.author, "The author")  # Asserting that the author matches
        self.assertEqual(self.book.isbn, "1234567890123")  # Asserting that the ISBN matches
    
    def test_book_listview(self):  # Test method to check the book list view
        response = self.client.get(reverse("home"))  # Getting the response from the "home" URL
        self.assertEqual(response.status_code, 200)  # Asserting that the status code is 200 (OK)
        self.assertContains(response, "A subtitle")  # Asserting that the response contains the subtitle
        self.assertTemplateUsed(response, "books/book_list.html")  # Asserting that the correct template is used
