import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDP3PPszP_ZndSOKX4g4r7rf649c6Hea0U')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
