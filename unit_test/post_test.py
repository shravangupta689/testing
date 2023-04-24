from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_create_post(self):
        p=Post('Test','TestContent')

        self.assertEqual('Test',p.title)
        self.assertEqual('TestContent',p.content)

    def test_json(self):
        p = Post('Test', 'TestContent')
        expected = {'title': 'Test', 'content':"TestContent"}

        self.assertDictEqual(expected,p.json())