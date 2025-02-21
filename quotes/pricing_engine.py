from .google_trends import fetch_service_demand
from .maps_api import get_location_adjustment
from .market import fetch_base_price

def calculate_price_details(service_type, urgency, location):
    """
    Calculates the final quote and returns a breakdown of the calculation.
    """
    # Fetch base price from market rates (in USD)
    base_price = fetch_base_price(service_type, location)
    
    # Get dynamic demand factor from Google Trends
    demand_factor = fetch_service_demand(service_type)
    
    # Get location adjustment factor from geocoding
    location_factor = get_location_adjustment(location)
    
    # If urgency is 0, use 1 to avoid zeroing out the price.
    effective_urgency = urgency if urgency > 0 else 1.0
    
    final_price_inr = round(base_price * demand_factor * effective_urgency * location_factor, 2)
    
    breakdown = {
        'service_type': service_type,
        'location': location,
        'base_price_usd': base_price,
        'demand_factor': demand_factor,
        'effective_urgency': effective_urgency,
        'location_factor': location_factor,
        'final_price_inr': final_price_inr,
    }
    return breakdown
