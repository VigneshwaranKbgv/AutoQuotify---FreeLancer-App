import requests

def fetch_osm_businesses(service, location="India"):
    """
    Query the Overpass API for businesses in a given location that match the specified service.
    This example searches for nodes with the tag "service" equal to the provided service.
    
    Parameters:
        service (str): The service type (e.g., "electrician").
        location (str): The location to search in (default "India").
    
    Returns:
        list: A list of matching OSM elements (nodes).
    """
    overpass_url = "https://overpass-api.de/api/interpreter"
    
    query = f"""
    [out:json];
    area["name"="{location}"][admin_level=2]->.searchArea;
    node(area.searchArea)["service"="{service}"];
    out body;
    """
    
    try:
        response = requests.post(overpass_url, data=query, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        # Print the entire OSM response JSON to the console
        print("Full OSM response:")
        print(data)
        
        return data.get("elements", [])
    except Exception as e:
        print("Error fetching OSM data:", e)
        return []
