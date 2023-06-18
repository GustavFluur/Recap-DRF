from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListView(APITestCase):
    def setUp(self):
        User.objects.create_user(username='gustav', password='pass')

    def test_can_list_posts(self):
        gustav = User.objects.get(username='gustav')
        Post.objects.create(owner=gustav, title='My unique title!')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))
    
    def test_logged_in_user_can_create_post(self):
        self.client.login(username='gustav', password='pass')
        response = self.client.post('/posts/', {'title': 'My unique title!'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'My unique title!'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)





