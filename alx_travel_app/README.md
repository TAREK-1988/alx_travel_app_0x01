# ALX Travel App 0x00

This project is a simple travel booking backend built with Django and Django REST Framework.

## Milestone 2: Creating Models, Serializers, and Seeders

### Models

Defined in `listings/models.py`:

- `Listing` – Represents a property available for booking.
- `Booking` – Represents a reservation made for a listing.
- `Review` – Represents a user review and rating for a listing.

### Serializers

Defined in `listings/serializers.py`:

- `ListingSerializer` – Serializes `Listing` instances for API responses.
- `BookingSerializer` – Serializes `Booking` instances, exposing:
  - `listing` (nested, read-only)
  - `listing_id` (write-only) for creating bookings.

### Database Seeding

Custom management command:

- File: `listings/management/commands/seed.py`
- Command:

```bash
python manage.py seed

