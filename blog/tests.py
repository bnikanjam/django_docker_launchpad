from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post, Review


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        test_user_1 = get_user_model().objects.create_user(username='jennifer_post_author', password='abc123')
        test_user_1.save()
        test_user_2 = get_user_model().objects.create_user(username='raymond_post_reviewer', password='ABC123')
        test_user_2.save()

        # Create a blog post
        test_post = Post.objects.create(
            author=test_user_1,
            title='Blog title',
            slug='blog-title',
            content='Body content...',
        )
        test_post.save()

        # Create a review for above blog post
        test_review = Review.objects.create(
            author=test_user_2,
            review=test_post,
            content='This is an excellent blog post!',
        )

    def test_blog_content(self):
        post = Post.objects.get(slug='blog-title')
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.content}'
        self.assertEqual(expected_author, 'jennifer_post_author')
        self.assertEqual(expected_title, 'Blog title')
        self.assertEqual(expected_body, 'Body content...')

    def test_review(self):
        post = Post.objects.get(slug='blog-title')
        expected_reviewer = f'{post.review_set.first().author}'
        expected_review = f'{post.review_set.first().content}'
        self.assertEqual(expected_reviewer, 'raymond_post_reviewer')
        self.assertEqual(expected_review, 'This is an excellent blog post!')
