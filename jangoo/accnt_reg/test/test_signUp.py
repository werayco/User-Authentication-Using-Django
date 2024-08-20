from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import UserCreationForm
from ..forms import UserRegform
# Create your tests here.

class TestSignUp(TestCase):
    def setUp(self) -> None:
        self.form = UserRegform()

    def test_if_the_form_isASubclass(self):
        self.assertTrue(issubclass(UserRegform,UserCreationForm))
        self.assertTrue("email" in self.form.Meta.fields)
        self.assertTrue("username" in self.form.Meta.fields)
        self.assertTrue("password1" in self.form.Meta.fields)
        self.assertTrue("password2" in self.form.Meta.fields)

    def test_with_sample_data(self):
        sample = {"username":"ray", "email":"heisrayco@gmail.com","password1":"hocuspocus11","password2":"hocuspocus11"}
        form_sample = UserRegform(sample)
        if form_sample.is_valid():
            form_sample.save()
    
    def test_the_accnt_signUp_template(self):
        resp = self.client.get(reverse("sign"))
        self.assertEqual(resp.status_code,HTTPStatus.OK)
        self.assertTemplateUsed(resp,"accnts/sign_up.html")

class TestLogin(TestCase):
    def test_login_template(self):
        resp_login = self.client.get(reverse("login"))
        self.assertEqual(resp_login.status_code,HTTPStatus.OK)
        self.assertTemplateUsed(resp_login,"accnts/login.html")


