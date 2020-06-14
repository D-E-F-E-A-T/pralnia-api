from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Wash

from wash.serializers import WashSerializer

WASH_URL = reverse('wash:wash-list')

def sample_wash(user, **params):
    defaults = {
        'title': 'Sample Wash',
        'time_minutes': 10,
        'price': 5.00
    }

    defaults.update(params)

    return Wash.objects.create(user=user, **defaults)

class PublicWashApiTests(TestCase):
     
    def setUp(self):
        self.client = APIClient()
    
    def test_auth_required(self):
        res = self.client.get(WASH_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateWashApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@gmail.com',
            'pass123'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_washes(self):
        sample_wash(user=self.user)
        sample_wash(user=self.user)

        res = self.client.get(WASH_URL)

        washes = Wash.objects.all().order_by('-id')
        serializer = WashSerializer(washes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

