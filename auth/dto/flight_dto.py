class FlightDTO:
    def __init__(self, flight_id, flight_number, departure_time, arrival_time, baggage_allowance):
        self.flight_id = flight_id
        self.flight_number = flight_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.baggage_allowance = baggage_allowance

    def to_dict(self):
        return {
            "flight_id": self.flight_id,
            "flight_number": self.flight_number,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "baggage_allowance": self.baggage_allowance
        }


class FlightDTO1:
    def __init__(self, flight_id, flight_number, departure_time, arrival_time, baggage_allowance, departure_airport, arrival_airport, airline):
        self.flight_id = flight_id
        self.flight_number = flight_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.baggage_allowance = baggage_allowance
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.airline = airline

    def to_dict(self):
        return {
            'flight_id': self.flight_id,
            'flight_number': self.flight_number,
            'departure_time': self.departure_time,
            'arrival_time': self.arrival_time,
            'baggage_allowance': self.baggage_allowance,
            'departure_airport': self.departure_airport,
            'arrival_airport': self.arrival_airport,
            'airline': self.airline
        }