from django.test import TestCase
from .models import Location, Category, Post
import datetime

# Create your tests here.
class PostTests(TestCase):
    '''
    create an instance of the post class to enable testing
    '''

    def setUp(self):
        self.place = Location(image_location = "Nairobi")
        self.place.save()

        self.category = Category(image_category = "favourites")
        self.category.save()

        self.post = Post(title = 'A random title', image_description = "A random description",
                           image_location = self.place)
        self.post.save()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_method(self):
        self.post.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        Post.delete_post(self.post.id)
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 0)

    def test_get_photo_by_id(self):
        post = Post.get_photo_by_id(self.post.id)
        self.assertEqual(post, self.post)

    def test_search_post_by_category(self):
        post = Post.search_photo_by_category("favourites")
        self.assertFalse(len(post) > 0)

    def test_filter_by_location(self):
        post = Post.filter_by_location(self.post.id)
        self.assertTrue(len(post) > 0)


class LocationTest(TestCase):
    """
    Testing the Location model
    """
    def setUp(self):
        """
        Creating a new instance of the Location class
        """
        self.location = Location(image_location = "Nairobi")
        self.location.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)


class CategoryTest(TestCase):
    """
    Testing the Category class
    """
    def setUp(self):
        """
        Creating a new instance of the Category class
        """
        self.category = Category(image_category = "favourites")
        self.category.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)