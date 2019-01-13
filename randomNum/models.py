from django.db import models, connection
import random
import json


class RandomNum(models.Model):
    random_number = models.FloatField()
    objects = models.Manager()

    class Meta:
        managed=False
        db_table = "random_number"

    



