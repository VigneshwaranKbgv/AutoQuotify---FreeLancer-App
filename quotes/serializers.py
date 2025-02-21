from rest_framework import serializers

class QuoteRequestSerializer(serializers.Serializer):
    service_type = serializers.ChoiceField(choices=[
        ('electrician', 'Electrician'),
        ('plumbing', 'Plumbing'),
        ('graphic_design', 'Graphic Design'),
        ('legal_consultation', 'Legal Consultation'),
        ('carpentry', 'Carpentry'),
        ('house_cleaning', 'House Cleaning'),
    ])
    urgency = serializers.FloatField(min_value=0, max_value=3)
    location = serializers.CharField()  # User enters a location (e.g., "Chennai")
