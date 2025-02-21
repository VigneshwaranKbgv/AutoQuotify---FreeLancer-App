from .osm import fetch_osm_businesses

def fetch_base_price(service_type, location):
    """
    Automatically compute a base price using OSM data.
    We query OSM for nodes matching the service and location.
    The formula used is:
    
        base_price = default_price * (scaling_factor / (count + 1))
    
    where 'count' is the number of businesses found and scaling_factor is a chosen constant.
    We then cap the computed price to be within 50% to 150% of a default price.
    
    Parameters:
        service_type (str): Service name (e.g., "electrician").
        location (str): Location (e.g., "Chennai").
    
    Returns:
        float: The computed base price (in USD).
    """
    # Default base prices (in USD) for fallback purposes.
    default_prices = {
        'electrician': 60,
        'plumbing': 50,
        'graphic_design': 70,
        'legal_consultation': 100,
        'carpentry': 40,
        'house_cleaning': 30,
    }
    service_type_lower = service_type.lower()
    default_price = default_prices.get(service_type_lower, 50)
    
    try:
        businesses = fetch_osm_businesses(service=service_type_lower, location=location)
        count = len(businesses)
        # Define a scaling factor; the idea is that if count is high, competition drives price down.
        scaling_factor = 50  # You can adjust this constant based on research.
        computed_price = default_price * (scaling_factor / (count + 1))
        
        # Clamp the computed price to a reasonable range:
        min_price = 0.5 * default_price
        max_price = 1.5 * default_price
        if computed_price < min_price:
            computed_price = min_price
        if computed_price > max_price:
            computed_price = max_price
            
        return round(computed_price, 2)
    except Exception as e:
        print("Error fetching base price from OSM:", e)
        return default_price
