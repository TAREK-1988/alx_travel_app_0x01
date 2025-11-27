# alx_travel_app/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# ---------------------------------------------------------------------------
# Swagger / OpenAPI schema configuration
# ---------------------------------------------------------------------------

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel App API",
        default_version="v1",
        description=(
            "API documentation for the ALX Travel App.\n\n"
            "This backend exposes CRUD operations for travel listings and "
            "bookings which can be consumed by web or mobile clients."
        ),
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Django admin site (useful for local debugging)
    path("admin/", admin.site.urls),

    # Application API routes:
    #   /api/listings/
    #   /api/bookings/
    path("api/", include(("listings.urls", "listings"), namespace="listings")),

    # Swagger UI – interactive API documentation
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # Raw OpenAPI JSON schema
    path(
        "swagger.json",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
]

