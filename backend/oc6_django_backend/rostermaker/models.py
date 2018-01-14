from django.db import models
import datetime

# Create your models here.

class Paddler(models.Model):

    PADDLING_SIDE_RIGHT = "right"
    PADDLING_SIDE_LEFT = "left"
    PADDLING_SIDE_BOTH = "both"

    PADDLING_SIDES = [(PADDLING_SIDE_BOTH, "both"), (PADDLING_SIDE_LEFT, "left"), (PADDLING_SIDE_RIGHT, "right")]

    # note: id not required as it's automatically inserted by Django
    name = models.CharField(unique=True, max_length=40)
    paddling_side = models.CharField(choices=PADDLING_SIDES, blank=False, max_length=10)
    # TODO-Brandon: storing in milliseconds for now to make serialization a bit easier
    # Time in milliseconds
    time = models.IntegerField(default=0)
    # time = models.DateTimeField(default=datetime.time(0))

    class Meta:
        ordering = (['time'])