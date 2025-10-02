from flask import Blueprint, request, jsonify
from datetime import datetime

from auth.dao.ticket_dao import TicketDAO
from auth.service.flight_service import Service
tickets_bp = Blueprint('tickets', __name__)

@tickets_bp.route('/', methods=['GET'])
def get_all_tickets():
    """
        Get all tickets
        ---
        tags:
          - Tickets
        responses:
          200:
            description: A list of all tickets
            schema:
              type: object
              properties:
                tickets:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        example: 1
                      user_id:
                        type: integer
                        example: 10
                      flight_id:
                        type: integer
                        example: 5
                      purchase_date:
                        type: string
                        format: date
                        example: "2025-10-01"
                      price:
                        type: number
                        example: 250.50
        """
    tickets = TicketDAO.get_all_tickets()
    tickets_dict = [ticket.to_dict() for ticket in tickets]
    return jsonify({"tickets": tickets_dict}), 200


@tickets_bp.route('/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    """
        Update an existing ticket
        ---
        tags:
          - Tickets
        parameters:
          - in: path
            name: ticket_id
            required: true
            type: integer
            description: Ticket ID to update
          - in: body
            name: body
            required: true
            description: Ticket data for update
            schema:
              type: object
              required:
                - user_id
                - flight_id
                - purchase_date
                - price
              properties:
                user_id:
                  type: integer
                  example: 2
                flight_id:
                  type: integer
                  example: 7
                purchase_date:
                  type: string
                  format: date
                  example: "2025-10-02"
                price:
                  type: number
                  example: 199.99
        responses:
          200:
            description: Ticket updated successfully
          400:
            description: Missing or invalid fields
        """
    data = request.json
    user_id = data.get('user_id')
    flight_id = data.get('flight_id')
    purchase_date = data.get('purchase_date')
    price = data.get('price')

    if not all([user_id, flight_id, purchase_date, price]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    updated_ticket = TicketDAO.update_ticket(ticket_id, user_id, flight_id, purchase_date, price)

    return jsonify({"message": "Ticket updated successfully", "updated_ticket": updated_ticket.to_dict()}), 200


@tickets_bp.route('/user/flights', methods=['GET'])
def get_flights_for_user():
    """
        Get all flights for the current user
        ---
        tags:
          - Tickets
        responses:
          200:
            description: List of flights for a user
        """
    flights = Service.get_flights_for_user()
    flights_dict = [flight.to_dict() for flight in flights]
    return jsonify(flights_dict)

@tickets_bp.route('/flight/user', methods=['GET'])
def get_users_for_flight():
    users = Service.get_users_for_flight()
    users_dict = [user.to_dict() for user in users]
    return jsonify(users_dict)
