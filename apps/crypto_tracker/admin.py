from django.contrib import admin

from apps.crypto_tracker import models as cryptp_tracker_models

# Register your models here.
admin.site.register(cryptp_tracker_models.CryptoDetail)
