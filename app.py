MENU = "\nEnter 'c' to create blog,\nEnter 'l' to list blogs \nEnter 'p' to create post \nEnter 'r' to read blog \nEnter 'q' to quit\n "
POST_TEMPLATE = '''
----{}----

{}

'''
from blog import Blog
blogs=dict()


def show_menu():
    selection=input(MENU)

    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blog()
        elif selection == 'p':
            ask_create_post()
        elif selection == 'r':
            ask_read_blog()
        selection = input(MENU)
    print_blog()

def print_blog():
    for key, blog in blogs.items():
        print(f' - {blog}')

def ask_create_post():
    blog = input("Enter blog title you want to create post in:")
    title = input("Enter your post title:")
    content = input("Enter your post content:")

    blogs[blog].create_post(title,content)

def ask_read_blog():
    title = input('Enter title of blog you want to read: ')

    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_blog():
    title= input("Enter the title of the blog: ")
    name=input("Enter the name of Author")
    blogs[title] =  Blog(title,name)

