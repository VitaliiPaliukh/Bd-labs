from flask import Blueprint, jsonify
from auth.dao.flight_dao import FlightDAO
from auth.service.flight_service import Service

flight_bp = Blueprint('flight_bp', __name__)

@flight_bp.route('/flights', methods=['GET'])
def get_flights():
    """
        Get all flights
        ---
        tags:
          - Flights
        responses:
          200:
            description: List of flights
        """
    flights = Service.get_all_flights()
    return jsonify([flight.to_dict() for flight in flights]), 200

@flight_bp.route('/flights/<int:flight_id>', methods=['DELETE'])
def delete_flight(flight_id):
    FlightDAO.delete_flight(flight_id)
    return jsonify({"message": "Flight deleted successfully"}), 200


@flight_bp.route('/grouped-flight/', methods=['GET'])
def get_flights_grouped_by_city():
    """
        Get flights grouped by city
        ---
        tags:
          - Flights
        responses:
          200:
            description: Flights grouped by city
        """
    grouped_flights = Service.get_flights_grouped_by_city()
    return jsonify(grouped_flights)

