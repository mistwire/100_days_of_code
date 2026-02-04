class FlightData:
    """Data model for a flight result.

    Encapsulates flight information extracted from Kiwi.com API response.
    Used by FlightSearch and NotificationManager to pass data cleanly.
    """

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price                      # Price in USD (int or float)
        self.origin_city = origin_city          # Departure city name (e.g., "Boston")
        self.origin_airport = origin_airport    # Departure airport IATA (e.g., "BOS")
        self.destination_city = destination_city  # Arrival city name (e.g., "Denver")
        self.destination_airport = destination_airport  # Arrival airport IATA (e.g., "DEN")
        self.out_date = out_date                # Outbound date (e.g., "2024-02-05")
        self.return_date = return_date          # Return date (e.g., "2024-03-04")

