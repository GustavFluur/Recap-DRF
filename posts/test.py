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


class PostDetailView(APITestCase):
    def setUp(self):
        gustav = User.objects.create_user(username='gustav', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Post.objects.create(
            owner=gustav, title='My unique title!', content ='gustavs content'
        )
        Post.objects.create(
            owner=brian, title='another unique title!', content ='brian s content'
        )
    
    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'My unique title!')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/<invalid_id>')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_user_can_update_own_post(self):
        self.client.login(username='gustav', password='pass')
        response = self.client.put('/posts/1/', {'title': 'another unique title!'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'another unique title!')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_users_cant_update_post_they_dont_own(self):
        self.client.login(username='gustav', password='pass')
        response = self.client.put('/posts/2/', {'title': 'another unique title!'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)











