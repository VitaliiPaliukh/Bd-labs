from flask import g
from auth.dto.connected_flight_dto import Connected_flight_dto

class ConnectedFlightsDAO:
    @staticmethod
    def delete_connected_flight(connected_flight_id):
        conn = g.mysql.connection
        cursor = conn.cursor()
        cursor.execute('DELETE FROM connected_flights WHERE connected_flight_id = %s', (connected_flight_id,))
        conn.commit()
        cursor.close()

    @staticmethod
    def get_all_connected_flights():
        conn = g.mysql.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM connected_flights')
        flights = cursor.fetchall()
        cursor.close()

        return [
            Connected_flight_dto(flight[0], flight[1], flight[2]) for flight in flights
        ]


