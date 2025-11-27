import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from listings.models import Listing, Booking, Review


class Command(BaseCommand):
    help = "Seed the database with sample listings, bookings, and reviews."

    def handle(self, *args, **options):
        self.stdout.write("Starting database seeding...")

        if Listing.objects.exists():
            self.stdout.write(
                self.style.WARNING("Listings already exist. Seeding aborted to avoid duplicates.")
            )
            return

        listings_data = [
            {
                "title": "Cozy Apartment in Cairo",
                "description": "A lovely 2-bedroom apartment near the Nile with Wi-Fi and AC.",
                "location": "Cairo, Egypt",
                "price_per_night": 55.00,
                "max_guests": 4,
                "is_active": True,
            },
            {
                "title": "Seaside Villa in Alexandria",
                "description": "Spacious villa with sea view and private garden.",
                "location": "Alexandria, Egypt",
                "price_per_night": 120.00,
                "max_guests": 6,
                "is_active": True,
            },
            {
                "title": "Desert Camp in Siwa Oasis",
                "description": "Unique desert experience with traditional breakfast included.",
                "location": "Siwa, Egypt",
                "price_per_night": 80.00,
                "max_guests": 3,
                "is_active": True,
            },
        ]

        created_listings = []
        for data in listings_data:
            listing = Listing.objects.create(**data)
            created_listings.append(listing)
            self.stdout.write(self.style.SUCCESS(f"Created listing: {listing}"))

        today = timezone.now().date()

        for listing in created_listings:
            # حجزين لكل Listing
            for i in range(2):
                check_in = today + timedelta(days=random.randint(1, 30))
                check_out = check_in + timedelta(days=random.randint(1, 5))

                booking = Booking.objects.create(
                    listing=listing,
                    guest_name=f"Guest {i + 1} - {listing.title}",
                    guest_email=f"guest{i+1}@example.com",
                    check_in=check_in,
                    check_out=check_out,
                    num_guests=random.randint(1, listing.max_guests),
                    status=random.choice(
                        [
                            Booking.STATUS_PENDING,
                            Booking.STATUS_CONFIRMED,
                            Booking.STATUS_CANCELLED,
                        ]
                    ),
                )
                self.stdout.write(self.style.SUCCESS(f"Created booking: {booking}"))

            # مراجعتين لكل Listing
            for i in range(2):
                rating = random.randint(3, 5)
                review = Review.objects.create(
                    listing=listing,
                    reviewer_name=f"Reviewer {i + 1} - {listing.title}",
                    rating=rating,
                    comment=f"This is a sample review with rating {rating} for {listing.title}.",
                )
                self.stdout.write(self.style.SUCCESS(f"Created review: {review}"))

        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully!"))

