from rest_framework import generics as rest_generics

from apps.crypto_tracker import (
    serializers as crypto_tracker_serializers,
    models as crypto_tracker_models,
)


class CryptoDetailsView(rest_generics.ListCreateAPIView):
    """
    View to create crypto object or return a list of them.
    """

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        """
        # Override serializer class to pass the serializer based on the request method.
        serializer_methods = {
            "POST": crypto_tracker_serializers.BulkCryptoDetailsSerializer,
            "GET": crypto_tracker_serializers.CryptoDetailsSerializer,
        }
        return serializer_methods[self.request.method.upper()]

    def get_queryset(self):
        """
        Returns a queryset of a list of items for this view.
        """
        return crypto_tracker_models.CryptoDetail.objects.all().order_by('name')
