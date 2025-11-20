from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


# Copilot: Added Interaction model to record interactions so views like
# `summary` and `interact` can work even if the original project didn't
# provide this model. If you already had an Interaction model elsewhere,
# you can remove or adapt this to match your previous schema.
class Interaction(models.Model):
    CHANNEL_CHOICES = [
        ("email", "Email"),
        ("phone", "Phone"),
        ("chat", "Chat"),
        ("in_person", "In Person"),
    ]

    DIRECTION_CHOICES = [
        ("inbound", "Inbound"),
        ("outbound", "Outbound"),
    ]

    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="interactions")
    interaction_date = models.DateField(auto_now_add=True)
    channel = models.CharField(max_length=32, choices=CHANNEL_CHOICES)
    direction = models.CharField(max_length=16, choices=DIRECTION_CHOICES)
    summary = models.TextField(blank=True)

    def __str__(self):
        return f"Interaction {self.id} (Customer {self.customer_id})"

