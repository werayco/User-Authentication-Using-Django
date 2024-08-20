from django.test import TestCase
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from model_bakery import baker
from http import HTTPStatus

from django.urls import reverse

user = get_user_model()

class TestLogin(TestCase):
    def setUp(self) -> None:
        self.username = "rayco"
        self.email = "rayco@gmail.com"
        self.password = "testpass123"

        user.objects.create_user(self.username,self.email,self.password)

    def test_login_page(self):
        resp = self.client.get(reverse("login"))
        self.assertEqual(resp.status_code,HTTPStatus.OK)
        self.assertTemplateUsed("accnts/login.html")


    def test(self):
        req_data = {"username":self.username,
                    "password":self.password}
        
        resp_post = self.client.post(reverse("login"),req_data)
        self.assertRedirects(resp_post,reverse("homepage"))

        
