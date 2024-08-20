from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
 

class posts(models.Model):
    name = models.CharField(max_length=20000)
    description = models.CharField(max_length=20000)
    time_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("about", kwargs={"id": self.pk})
