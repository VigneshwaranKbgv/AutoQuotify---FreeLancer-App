from pytrends.request import TrendReq
from django.core.cache import cache

def fetch_service_demand(service_keyword):
    """
    Uses pytrends to fetch interest data for the given service keyword over the past 3 months.
    Returns a multiplier: 1 + (average interest / 100).
    The value is cached for 30 minutes.
    """
    cache_key = f"trend_{service_keyword.lower()}"
    cached_demand = cache.get(cache_key)
    if cached_demand is not None:
        return cached_demand

    pytrends = TrendReq(hl='en-US', tz=360)
    try:
        pytrends.build_payload([service_keyword], timeframe='today 3-m')
        trends_data = pytrends.interest_over_time()
        if not trends_data.empty:
            avg_interest = trends_data[service_keyword].mean()
            demand_factor = 1 + (avg_interest / 100)
        else:
            demand_factor = 1.0
    except Exception:
        demand_factor = 1.0

    cache.set(cache_key, demand_factor, timeout=1800)  # Cache for 30 minutes
    return demand_factor
