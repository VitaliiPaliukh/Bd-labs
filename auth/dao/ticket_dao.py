from flask import g
from datetime import datetime
from auth.dto.ticket_dto import TicketDTO
from auth.dto.flight_dto import FlightDTO1
from auth.dto.user_dto import UserDTO


class TicketDAO:
    @staticmethod
    def get_all_tickets():
            conn = g.mysql.connection  # Отримуємо підключення до бази даних із глобального контексту Flask
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tickets')
            tickets = cursor.fetchall()
            cursor.close()

            # Повертаємо список об'єктів TicketDTO
            return [TicketDTO(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4]) for ticket in tickets]
    @staticmethod
    def get_all_flights():
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
    def update_ticket(ticket_id, user_id, flight_id, purchase_date, price):
        conn = g.mysql.connection
        cursor = conn.cursor()

        cursor.execute(
            '''
            UPDATE tickets
            SET user_id = %s, flight_id = %s, purchase_date = %s, price = %s
            WHERE ticket_id = %s
            ''',
            (user_id, flight_id, purchase_date, price, ticket_id)
        )
        conn.commit()
        cursor.close()

        return TicketDTO(ticket_id, user_id, flight_id, purchase_date, price)

    @staticmethod
    def get_flights_for_user():
        query = """
        SELECT f.flight_id, f.flight_number, f.departure_time, f.arrival_time, f.baggage_allowance,
               a1.name AS departure_airport, a2.name AS arrival_airport, al.name AS airline
        FROM tickets t
        JOIN flights f ON t.flight_id = f.flight_id
        JOIN airports a1 ON f.departure_airport_id = a1.airport_id
        JOIN airports a2 ON f.arrival_airport_id = a2.airport_id
        JOIN airlines al ON f.airline_id = al.airline_id
        """
        conn = g.mysql.connection
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        flights = [FlightDTO1(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in result]
        return flights

    @staticmethod
    def get_users_for_flight():
        query = """
            SELECT u.username, u.email, u.password_hash
            FROM tickets t
            JOIN users u ON t.user_id = u.user_id
            JOIN flights f ON t.flight_id = f.flight_id
            """
        conn = g.mysql.connection
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        users = [UserDTO(row[0], row[1], row[2]) for row in result]
        return users
