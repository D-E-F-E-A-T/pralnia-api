from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Clothe

from wash.serializers import ClotheSerializer

CLOTHE_URL = reverse('wash:clothe-list')

class PublicClothesApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
    
    def test_login_required(self):
        res = self.client.get(CLOTHE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateClothesApiTest(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@mail.com',
            'pass123'
        )
        self.client.force_authenticate(self.user)
    
    def test_retrieve_clothe_list(self):
        Clothe.objects.create(user=self.user, name='Hat')
        Clothe.objects.create(user=self.user, name='Trousers')

        res = self.client.get(CLOTHE_URL)

        clothes = Clothe.objects.all().order_by('-name')
        serializer = ClotheSerializer(clothes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_clothe_successful(self):
        payload = {'name':'Scarf'}
        self.client.post(CLOTHE_URL, payload)

        exists = Clothe.objects.filter(
            user=self.user,
            name=payload['name']
        ).exists()
        self.assertTrue(exists)


