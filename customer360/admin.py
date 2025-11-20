from django.contrib import admin
from .models import Customer, Interaction

# Copilot: Register Customer and Interaction for admin UI
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone")
    search_fields = ("name", "email", "phone")


@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "interaction_date", "channel", "direction")
    list_filter = ("channel", "direction", "interaction_date")
    search_fields = ("customer__name", "summary")
