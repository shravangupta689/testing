import builtins

from unittest import TestCase
from unittest.mock import patch
import app

from blog import Blog
from post import Post


class AppTest(TestCase):
    def setUp(self) :
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}


    def test_show_menu(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.show_menu()
            mocked_input.assert_called_with(app.MENU)

    def test_menu_calls_print_blog(self):
        with patch('app.print_blog') as mocked_print_blog:
            with patch('builtins.input', return_value='q'):
                app.show_menu()
                mocked_print_blog.assert_called()

    def test_print_blog(self):

        with patch('builtins.print') as mocked_print:
            app.print_blog()
            mocked_print.assert_called_with(' - Test by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', "Test Author")
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):

        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(app.blogs['Test'])

    def test_print_posts(self):
        blog = app.blogs['Test']
        blog.create_post('Test post', 'Test Content')

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('post title', 'post content')

        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(app.POST_TEMPLATE.format(post.title,post.content))

    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test','Test Title','TestContent')
            app.ask_create_post()

            self.assertEqual(app.blogs['Test'].posts[0].title, 'Test Title')
            self.assertEqual(app.blogs['Test'].posts[0].content, 'TestContent')

    def test_greet(self):
        with patch('builtins.print') as mocked_print:
            app.greet()
            mocked_print.assert_called_with('Hello user')

