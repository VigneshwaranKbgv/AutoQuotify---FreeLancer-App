# AutoQuotify - Dynamic Price Quotation API

## Overview
AutoQuotify is a dynamic price quotation API designed for service providers and freelancers. It calculates service quotes based on location, urgency, and real-time market data, integrating external sources like Google Trends and OpenStreetMap (OSM) for enhanced accuracy.

## Tech Stack
- **Backend:** Python, Django, Django REST Framework (DRF)
- **Frontend:** HTML, CSS, JavaScript (optional for UI improvements)
- **Database:** SQLite / PostgreSQL
- **External APIs:**
  - OpenStreetMap (OSM) for vendor and location-based services
  - Google Trends (via PyTrends) for market demand analysis

## Features
- Dynamic pricing based on real-time market trends
- Location-based pricing using OpenStreetMap
- Urgency factor for price adjustments
- API-based architecture for easy integration
- Logging and debugging support for quote calculation

## Project Structure
```
AUTOQuotify/
│-- autoquotify/
│   │-- __init__.py
│   │-- asgi.py
│   │-- settings.py
│   │-- urls.py
│   │-- wsgi.py
│
│-- quotes/
│   │-- __init__.py
│   │-- admin.py
│   │-- apps.py
│   │-- google_trends.py
│   │-- maps_api.py
│   │-- market.py
│   │-- models.py
│   │-- osm.py
│   │-- pricing_engine.py
│   │-- serializers.py
│   │-- tests.py
│   │-- urls.py
│   │-- views.py
│   │-- templates/
│       │-- index.html
│
│-- manage.py
```

## Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/VigneshwaranKbgv/AutoQuotify---FreeLancer-App.git
   cd AutoQuotify
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run Django migrations**
   ```bash
   python manage.py migrate
   ```

4. **Start the server**
   ```bash
   python manage.py runserver
   ```

## Usage
- Visit `http://127.0.0.1:8000/` to access the web UI.
- Use the API endpoint: `POST /quote/` with parameters like `service_type`, `location`, and `urgency`.
- Check console logs for quote breakdown and OSM response.

## Future Enhancements
- Vendor integration for live price comparison
- Machine Learning-based price prediction
- User authentication for service providers
- UI/UX improvements with interactive elements

## Contributing
Contributions are welcome! Feel free to fork the repo and create pull requests.

## License
This project is licensed under the MIT License.

