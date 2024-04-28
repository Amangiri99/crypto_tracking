from django.db import models

from apps.commons import models as commons_models


class CryptoDetail(commons_models.TimeStampBaseModel):
    """
    Class to store information about the crypto.
    """

    name = models.CharField(max_length=128)
    short_name = models.CharField(max_length=16)
    price = models.CharField(max_length=32)
    one_hour_change = models.CharField(max_length=16)
    one_day_change = models.CharField(max_length=16)
    one_week_change = models.CharField(max_length=16)
    market_cap = models.CharField(max_length=64)
    volume_in_dollars = models.CharField(max_length=64)
    volume_in_crypto = models.CharField(max_length=64)
    circulating_supply = models.CharField(max_length=64)
