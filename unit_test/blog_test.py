from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b=Blog('Test','TestAuthor')

        self.assertEqual('Test',b.title)
        self.assertEqual('TestAuthor',b.author)
        self.assertListEqual([],b.posts)

    def test_repr(self):
        b=Blog('Test','TestAuthor')
        b.posts=['test','ram']

        self.assertEqual(b.__repr__(),'Test by TestAuthor (2 posts)')

