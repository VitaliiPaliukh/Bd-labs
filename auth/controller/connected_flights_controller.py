# auth/controller/connected_flights_controller.py
from flask import Blueprint, jsonify, request, g
from auth.service.flight_service import Service
from auth.dao.connected_flights_dao import ConnectedFlightsDAO

connected_flights_bp = Blueprint('connected_flights_bp', __name__)

@connected_flights_bp.route('/connected_flights/<int:connected_flight_id>', methods=['DELETE'])
def delete_connected_flight(connected_flight_id):
    Service.delete_connected_flight(connected_flight_id)
    return jsonify({"message": "Connected flight deleted successfully"}), 200

@connected_flights_bp.route('/connected_flights', methods=['GET'])
def get_connected_flights():
    connected_flights = Service.get_all_connected_flights()
    return jsonify([connected_flight.to_dict() for connected_flight in connected_flights]), 200
