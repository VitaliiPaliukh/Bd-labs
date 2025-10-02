# auth/controller/connected_flights_controller.py
from flask import Blueprint, jsonify, request, g
from auth.service.flight_service import Service
from auth.dao.connected_flights_dao import ConnectedFlightsDAO

connected_flights_bp = Blueprint('connected_flights_bp', __name__)

@connected_flights_bp.route('/connected_flights/<int:connected_flight_id>', methods=['DELETE'])
def delete_connected_flight(connected_flight_id):
    """
        Delete a connected flight by its ID
        ---
        tags:
          - Connected Flights
        parameters:
          - name: connected_flight_id
            in: path
            required: true
            schema:
              type: integer
            description: ID of the connected flight to delete
        responses:
          200:
            description: Connected flight deleted successfully
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
        """
    Service.delete_connected_flight(connected_flight_id)
    return jsonify({"message": "Connected flight deleted successfully"}), 200

@connected_flights_bp.route('/connected_flights', methods=['GET'])
def get_connected_flights():
    """
        Get all connected flights
        ---
        tags:
            - Connected Flights
        responses:
          200:
            description: List of connected flights
        """
    connected_flights = Service.get_all_connected_flights()
    return jsonify([connected_flight.to_dict() for connected_flight in connected_flights]), 200
