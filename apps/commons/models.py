from django.db import models

# Create your models here.
class TimeStampBaseModel(models.Model):
    """
    Base model for time stamps.
    """
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
