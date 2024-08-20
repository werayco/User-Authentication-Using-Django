from django.test import TestCase
from .models import posts
from http import HTTPStatus
from model_bakery import baker
from django.urls import reverse


# Create your tests here.
class ModelTest(TestCase):
    def test_model_exists(self):
        query_set = posts.objects.count()
        self.assertEqual(query_set, 0)

    def string_rep_obj(self):
        baked = baker.make(posts)
        self.assertEqual(str(baked), baked.name)
        self.assertTrue(isinstance(baked, posts))


class homepage(TestCase):
    def setUp(self) -> None:
        inst_1 = baker.make(
            posts
        )  # the baker module is used to create random instances for testing
        inst_2 = baker.make(posts)
        inst_3 = baker.make(posts, name="Ryan")

    def test_checks_homepage_template(self):
        resp = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(resp, "posts/index.html")
        self.assertEqual(resp.status_code, HTTPStatus.OK)


class DetailedPageTest(TestCase):
    def setUp(self) -> None:
        self.post = baker.make(posts)

    def test_checksIf_cannonical_url_returns_correct_response(self):
        reps = self.client.get(self.post.get_absolute_url())
        self.assertContains(reps, self.post.name)

        self.assertEqual(reps.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(reps, "posts/index.html")
