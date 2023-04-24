from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):

    def test_create_post_in_blog(self):
        b = Blog('Test', 'TestAuthor')
        b.create_post('Test Post','Test Content')
        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title,'Test Post')
        self.assertEqual(b.posts[0].content,'Test Content')

    def test_json_no_posts(self):
        b = Blog('Test', 'TestAuthor')
        expected = {'title': 'Test',
                    'author': 'TestAuthor',
                    'posts': []
                    }
        self.assertDictEqual(expected,b.json())

    def test_json(self):
        b = Blog('Test', 'TestAuthor')
        b.create_post('Test Post', 'Test Content')
        expected={'title': 'Test',
                  'author':'TestAuthor',
                  'posts': [{'title': 'Test Post',
                                  'content': 'Test Content'}]
        }

        self.assertDictEqual(expected,b.json())


