class Connected_flight_dto:
    def __init__(self, connection_id, flight_id, connected_flight_id):
        self.connection_id = connection_id
        self.flight_id = flight_id
        self.connected_flight_id = connected_flight_id

    def to_dict(self):
        return {
            "connection_id": self.connection_id,
            "flight_id": self.flight_id,
            "connected_flight_id": self.connected_flight_id
        }