class FlightData:
    """Data model for a flight result.

    Encapsulates flight information from Kiwi.com API.
    Supports both direct flights (stop_overs=0) and flights with layovers (stop_overs=1).
    """

    def __init__(
            self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date,
            stop_overs=0, via_city=""):
        self.price = price                      # Price in GBP
        self.origin_city = origin_city          # Departure city name
        self.origin_airport = origin_airport    # Departure airport IATA
        self.destination_city = destination_city  # Arrival city name (final destination)
        self.destination_airport = destination_airport  # Arrival airport IATA
        self.out_date = out_date                # Outbound date (YYYY-MM-DD)
        self.return_date = return_date          # Return date (YYYY-MM-DD)
        self.stop_overs = stop_overs            # Number of stopovers (0 = direct, 1+ = with layover)
        self.via_city = via_city                # City where stopover occurs (if applicable)
