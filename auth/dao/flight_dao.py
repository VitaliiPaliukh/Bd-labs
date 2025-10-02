from auth.dto.flight_dto import FlightDTO

from flask import g
from collections import defaultdict
from itertools import groupby

class FlightDAO:
    @staticmethod
    def get_all_flights():
        conn = g.mysql.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM flights')
        flights = cursor.fetchall()
        cursor.close()

        return [
            FlightDTO(flight[0], flight[1], flight[2], flight[3], flight[4]) for flight in flights
        ]

    @staticmethod
    def get_all_flight():
        query = """
            SELECT f.flight_id, f.flight_number, f.departure_time, f.arrival_time, f.baggage_allowance,
                   a1.name AS departure_airport, a2.name AS arrival_airport, al.name AS airline
            FROM flights f
            JOIN airports a1 ON f.departure_airport_id = a1.airport_id
            JOIN airports a2 ON f.arrival_airport_id = a2.airport_id
            JOIN airlines al ON f.airline_id = al.airline_id
            """
        conn = g.mysql.connection
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        flights = [FlightDTO(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in result]
        return flights

    @staticmethod
    def delete_flight(flight_id):
            conn = g.mysql.connection
            cursor = conn.cursor()
            cursor.execute('DELETE FROM flights WHERE flight_id = %s', (flight_id,))
            conn.commit()
            cursor.close()

    def get_flights_grouped_by_city():
        conn = g.mysql.connection
        cursor = conn.cursor()

        query = '''
            SELECT 
                departure.location AS departure_city,
                arrival.location AS arrival_city,
                flight_number,
                departure_time,
                arrival_time
            FROM flights
            JOIN airports AS departure ON flights.departure_airport_id = departure.airport_id
            JOIN airports AS arrival ON flights.arrival_airport_id = arrival.airport_id
            ORDER BY departure.location, arrival.location
        '''
        cursor.execute(query)
        flights = cursor.fetchall()

        flights_list = [
            {
                'departure_city': flight[0],
                'arrival_city': flight[1],
                'flight_number': flight[2],
                'departure_time': flight[3],
                'arrival_time': flight[4]
            }
            for flight in flights
        ]

        cursor.close()

        grouped_flights = defaultdict(list)
        for flight in flights_list:
            grouped_flights[flight['departure_city']].append(flight)

        return dict(grouped_flights)