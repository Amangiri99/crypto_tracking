from rest_framework import serializers

from apps.crypto_tracker import models as crypto_tracker_models


class CryptoDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer for crypto details
    """

    def validate_name(self, value):
        """
        Field level validation for name field
        """
        if value is None:
            raise serializers.ValidationError("Name is a required field")
        return value

    class Meta:
        model = crypto_tracker_models.CryptoDetail
        fields = "__all__"


class BulkCryptoDetailsSerializer(serializers.Serializer):
    """
    Serializer for crypto details
    """

    data = CryptoDetailsSerializer(many=True)

    def save(self, *kwargs):
        """ """
        bulk_update_list = []
        bulk_create_list = []
        for item in self.validated_data["data"]:
            crypto_name = item.get("name")
            if crypto_name:
                try:
                    instance = crypto_tracker_models.CryptoDetail.objects.get(
                        name=crypto_name
                    )
                    # Update existing instance with validated data
                    for attr, value in item.items():
                        setattr(instance, attr, value)
                    bulk_update_list.append(instance)
                except crypto_tracker_models.CryptoDetail.DoesNotExist:
                    new_instance = crypto_tracker_models.CryptoDetail(**item)
                    bulk_create_list.append(new_instance)

        if bulk_update_list:
            crypto_tracker_models.CryptoDetail.objects.bulk_update(
                bulk_update_list,
                fields=[
                    "price",
                    "one_hour_change",
                    "one_day_change",
                    "one_week_change",
                    "market_cap",
                    "volume_in_dollars",
                    "volume_in_crypto",
                    "circulating_supply",
                    "updated_at",
                ],
            )
        if bulk_create_list:
            crypto_tracker_models.CryptoDetail.objects.bulk_create(bulk_create_list)
