from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app_pereval.models import Pereval, Level, User, Coord, PerevalImage
from app_pereval.serializers import PerevalSerializer


class PerevalApiTestCase(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            beauty_title='test btitle',
            title='test title',
            other_titles='test other_titles',
            connect='test connect',

            level=Level.objects.create(
                winter='1A',
                summer='1A',
                autumn='1A',
                spring='1A',
            ),
            user_id=User.objects.create(
                email='test@example.com',
                name='test',
                fam='test',
                oct='test',
                phone='7777777777',
            ),
            coord_id=Coord.objects.create(
                latitude=125.36,
                longitude=259.25,
                height=1256
            ),
        )

        self.image_1 = PerevalImage.objects.create(
            data='https://a.d-cd.net/IEAAAgK6u-A-1920.jpg',
            title='image1',
            pereval_id=self.pereval_1,
        )

        self.pereval_2 = Pereval.objects.create(
            beauty_title='test btitle1',
            title='test title1',
            other_titles='test other_titles1',
            connect='test connect1',

            level=Level.objects.create(
                winter='1B',
                summer='1B',
                autumn='1B',
                spring='1B',
            ),
            user_id=User.objects.create(
                email='test1@example.com',
                name='test1',
                fam='test1',
                oct='test1',
                phone='7777778887',
            ),
            coord_id=Coord.objects.create(
                latitude=178.367,
                longitude=7859.25,
                height=2556
            ),
        )

        self.image_2 = PerevalImage.objects.create(
            data='https://vsegda-pomnim.com/uploads/posts/2022-04/1650930638_66-vsegda-pomnim-com-p-pereval-katu-yarik-gornii-foto-70.jpg',
            title='image2',
            pereval_id=self.pereval_2,
        )

    def test_get_list(self):
        response = self.client.get(reverse('pereval-list'))
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2],
                                            many=True,
                                            context={'request': response.wsgi_request}).data

        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        response = self.client.get(reverse('pereval-detail', kwargs={'pk': self.pereval_1.id}))
        serializer_data = PerevalSerializer(self.pereval_1, context={'request': response.wsgi_request}).data

        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_user_email(self):
        """Тест для объектов модели, отфильтрованных по email"""
        email = self.pereval_1.user_id.email
        url = f'/pereval/?user_id__email={email}'
        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
