from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuoteRequestSerializer
from .pricing_engine import calculate_price_details
from .models import ServiceQuote  # Optional, if you want to store quotes

@api_view(['POST', 'GET'])
def get_quote(request):
    if request.method == 'GET':
        return render(request, 'quotes/index.html')

    serializer = QuoteRequestSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        breakdown = calculate_price_details(
            service_type=data['service_type'],
            urgency=data['urgency'],
            location=data['location']
        )
        # Optionally, save the quote to the database
        ServiceQuote.objects.create(
            service_type=data['service_type'],
            demand_factor=breakdown['demand_factor'],
            urgency=data['urgency'],
            location_adjustment=breakdown['location_factor'],
            price=breakdown['final_price_inr']
        )
        return Response({'breakdown': breakdown})
    return Response(serializer.errors, status=400)

def index(request):
    return render(request, 'quotes/index.html')
