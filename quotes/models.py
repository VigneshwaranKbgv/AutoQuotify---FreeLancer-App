from django.db import models

class ServiceQuote(models.Model):
    service_type = models.CharField(max_length=100)
    demand_factor = models.FloatField()
    urgency = models.FloatField()
    location_adjustment = models.FloatField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_type} Quote - {self.price}"
