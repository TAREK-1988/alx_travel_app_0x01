from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    """Serializer for Listing model."""

    class Meta:
        model = Listing
        fields = [
            "id",
            "title",
            "description",
            "location",
            "price_per_night",
            "max_guests",
            "is_active",
            "created_at",
            "updated_at",
        ]


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model."""

    listing_id = serializers.PrimaryKeyRelatedField(
        source="listing",
        queryset=Listing.objects.all(),
        write_only=True,
        help_text="ID of the listing being booked",
    )

    listing = ListingSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = [
            "id",
            "listing",
            "listing_id",
            "guest_name",
            "guest_email",
            "check_in",
            "check_out",
            "num_guests",
            "status",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

