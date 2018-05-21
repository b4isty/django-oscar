from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct


# Create your models here.

class Product(AbstractProduct):
    video_url = models.URLField()


from oscar.apps.catalogue.models import *
