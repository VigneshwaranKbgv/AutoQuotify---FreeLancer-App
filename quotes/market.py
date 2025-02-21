def fetch_base_price(service_type, location):
    """
    Simulate fetching a base price from market data.
    In a real-world scenario, you'd query an external API or database.
    Prices are given in USD.
    """
    market_prices = {
        'electrician': {'Chennai': 40, 'Mumbai': 70, 'Delhi': 65},
        'plumbing': {'Chennai': 35, 'Mumbai': 60, 'Delhi': 55},
        'graphic_design': {'Chennai': 50, 'Mumbai': 80, 'Delhi': 75},
        'legal_consultation': {'Chennai': 90, 'Mumbai': 130, 'Delhi': 120},
        'carpentry': {'Chennai': 30, 'Mumbai': 55, 'Delhi': 50},
        'house_cleaning': {'Chennai': 25, 'Mumbai': 45, 'Delhi': 40},
    }
    default_prices = {
        'electrician': 60,
        'plumbing': 50,
        'graphic_design': 70,
        'legal_consultation': 100,
        'carpentry': 40,
        'house_cleaning': 30,
    }
    service_type = service_type.lower()
    location_title = location.title()
    if service_type in market_prices and location_title in market_prices[service_type]:
        return market_prices[service_type][location_title]
    else:
        return default_prices.get(service_type, 50)
