from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        user1 = User.objects.create(username='user1')
        user2 = User.objects.create(username='user2')
        user3 = User.objects.create(username='user3')
        book_1 = Book.objects.create(name="Test_11", price=25,
                                     author_name='Author 1')
        book_2 = Book.objects.create(name="Test_2", price=55,
                                     author_name='Author 2')

        
        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': "Test_1",
                'price': '25.00',
                'author_name': 'Author 1',
                'likes_count': 0
            },
            {
                'id': book_2.id,
                'name': "Test_2",
                'price': '55.00',
                'author_name': 'Author 2',
                'likes_count': 0
            },
        ]
        self.assertEqual(expected_data, data)

