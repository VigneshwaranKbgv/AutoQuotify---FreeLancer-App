from .google_trends import fetch_service_demand
from .maps_api import get_location_adjustment
from .market import fetch_base_price

def calculate_price(service_type, urgency, location):
    # Fetch base price from market rates (in USD)
    base_price = fetch_base_price(service_type, location)
    
    # Get dynamic demand factor from Google Trends
    demand_factor = fetch_service_demand(service_type)
    
    # Get location adjustment factor from geocoding
    location_factor = get_location_adjustment(location)
    
    # If urgency is 0, use 1 to avoid zeroing out the price.
    effective_urgency = urgency if urgency > 0 else 1.0
    
    # Calculate final price in USD
    price_inr = base_price * demand_factor * effective_urgency * location_factor
    
    # Fixed conversion rate (1 USD = 82 INR)
    # Debug prints to the terminal
    print("----- Quote Calculation Debug Info -----")
    print(f"Service Type: {service_type}")
    print(f"Location: {location}")
    print(f"Base Price (USD): {base_price}")
    print(f"Demand Factor: {demand_factor}")
    print(f"Urgency: {urgency} (Effective Urgency: {effective_urgency})")
    print(f"Location Factor: {location_factor}")
    print(f"Final Price in INR: {price_inr}")
    print("----------------------------------------")
    
    return price_inr
