from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Bookmark

class BookmarkAPITests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            password='test123'
        )

        self.user2 = User.objects.create_user(
            username='user2',
            password='test123'
        )

        self.bookmark = Bookmark.objects.create(
            user=self.user1,
            title='Python',
            url='https://www.python.org/',
            tags='Python'
        )

    def test_user_can_see_only_own_bookmarks(self):

        self.client.force_authenticate(user=self.user1)

        response = self.client.get('/api/bookmarks/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['count'], 1)

    def test_user_cannot_access_another_users_bookmark(self):

        self.client.force_authenticate(user=self.user2)

        response = self.client.get(
            f'/api/bookmarks/{self.bookmark.id}/'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_duplicate_bookmark_is_rejected(self):

        self.client.force_authenticate(user=self.user1)

        response = self.client.post(
            '/api/bookmarks/',
            {
                'title': 'Python duplicate',
                'url': 'https://www.python.org/',
                'tags': 'Programming'
            }
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)