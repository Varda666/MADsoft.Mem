from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from memes.models import Mem
from users.models import User


class ModelCreateTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@mail.com',
            name='TestName',
        )
        self.user.set_password('123qwe')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.mem = Mem.objects.create(
            name='Название мема тест',
            text='Текст мема тест',
            image='media/test_image.jpg',
            owner=self.user,
        )

    def test_get_list_memes(self):
        response = self.client.get(
            reverse('memes:memes_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {"count": 1,
                 "next": None,
                 "previous": None,
                 "results": [
                     {
                         "id": 1,
                         "name": 'Название мема тест',
                         "text": 'Текст мема тест',
                         "owner": 'test@mail.com',
                     },
                 ]
                 },
            ]
        )

    def test_mem_create(self):
        data = {
            'id': 1,
            'owner': User.objects.get(email='test2@mail.com'),
            "name": 'Название мема тест 2',
            "text": 'Текст мема тест 2',
            "image": 'media/test_image2.jpg',

        }
        response = self.client.post(
            reverse('memes:meme_create'),
            data=data,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Mem.objects.all().count(),
            2
        )

    def test_mem_update(self):
        data = {
            'name': 'Название мема тест 3'
        }
        responce = self.client.put(
            reverse(
                'memes:mem_update',
                kwargs={'pk': self.mem.id}),
            data=data,
            format='json'
        )
        self.assertEqual(
            Mem.objects.get(pk=self.mem.id).name,
            'Название мема тест 3'
        )

    def test_mem_delete(self):
        response = self.client.delete(
            reverse('memes:mem_delete', kwargs={'pk': self.mem.id})
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(
            Mem.objects.all().count(),
            1
        )
