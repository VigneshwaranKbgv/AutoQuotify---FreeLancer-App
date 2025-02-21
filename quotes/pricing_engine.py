from .google_trends import fetch_service_demand
from .maps_api import get_location_adjustment
from .market import fetch_base_price

def calculate_price_details(service_type, urgency, location):
    """
    Calculates the final service quote and returns a breakdown of the components.
    
    Steps:
      1. Fetch a dynamic base price from market data (via OSM).
      2. Get a demand factor from Google Trends.
      3. Get a location adjustment factor from OSM geocoding.
      4. Apply the urgency multiplier (if urgency is 0, treat it as 1 to avoid a zero price).
      5. Calculate the USD price and then convert to INR.
    
    Returns:
        dict: A dictionary containing all intermediate values and the final price.
    """
    base_price = fetch_base_price(service_type, location)
    demand_factor = fetch_service_demand(service_type)
    location_factor = get_location_adjustment(location)
    effective_urgency = urgency if urgency > 0 else 1.0
    
    final_price_inr = round(base_price * demand_factor * effective_urgency * location_factor, 2)
    
    breakdown = {
        'service_type': service_type,
        'location': location,
        'base_price': base_price,
        'demand_factor': demand_factor,
        'effective_urgency': effective_urgency,
        'location_factor': location_factor,
        'final_price_inr': final_price_inr,
    }
    return breakdown
