from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from quotes.google_trends import fetch_service_demand
from quotes.maps_api import get_location_adjustment
from .serializers import QuoteRequestSerializer
from .pricing_engine import calculate_price
from .models import ServiceQuote  # Optional: if you want to save quotes

@api_view(['POST', 'GET'])
def get_quote(request):
    if request.method == 'GET':
        return render(request, 'quotes/index.html')

    serializer = QuoteRequestSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        price = calculate_price(
            service_type=data['service_type'],
            urgency=data['urgency'],
            location=data['location']
        )
        # Optionally save the quote
        ServiceQuote.objects.create(
            service_type=data['service_type'],
            demand_factor=fetch_service_demand(data['service_type']),
            urgency=data['urgency'],
            location_adjustment=get_location_adjustment(data['location']),
            price=price
        )
        return Response({'price': price})
    return Response(serializer.errors, status=400)

def index(request):
    return render(request, 'quotes/index.html')
