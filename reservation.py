"""Module for creating reservations with Reservation class"""

import json
import os


class Reservation:
    """Class for managing hotel reservations"""

    def __init__(self, reservation_id, customer_id, hotel_name, room):
        """Initialization method"""
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_name = hotel_name
        self.room = room
        self.filename = f"reservation_{reservation_id}.json"

    def save_file(self):
        """Method to save reservation to a JSON file"""
        reservation_info = {
            'reservation_id': self.reservation_id,
            'customer_id': self.customer_id,
            'hotel_name': self.hotel_name,
            'room': self.room
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(reservation_info, f)

    @staticmethod
    def create_reservation(reservation_id, customer_id, hotel_name, room):
        """Method for creating a reservation"""
        reservation = Reservation(reservation_id,
                                  customer_id,
                                  hotel_name,
                                  room)
        reservation.save_file()
        return reservation

    @staticmethod
    def delete_reservation(reservation_id):
        """Method to delete reservation file"""
        filename = f"reservation_{reservation_id}.json"
        os.remove(filename)
