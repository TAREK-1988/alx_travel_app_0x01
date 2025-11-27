from django.contrib import admin
from .models import Listing, Booking, Review


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "price_per_night", "max_guests", "is_active", "created_at")
    list_filter = ("location", "is_active", "created_at")
    search_fields = ("title", "location")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("listing", "guest_name", "check_in", "check_out", "status", "created_at")
    list_filter = ("status", "check_in", "check_out")
    search_fields = ("guest_name", "guest_email")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("listing", "reviewer_name", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("reviewer_name", "comment")

