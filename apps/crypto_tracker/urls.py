from django.urls import path

from apps.crypto_tracker import views as crypto_tracker_views

urlpatterns = [
    # Url for the get and post requests
    path('crypto/', crypto_tracker_views.CryptoDetailsView.as_view(), name='crypto_details_view')
]
