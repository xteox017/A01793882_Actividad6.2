"""Module for hotel creation with Hotel class"""

import json
import os


class Hotel:
    """Class for managing available hotels"""

    def __init__(self, name, rating, rooms):
        """Initialization method"""
        self.name = name
        self.rating = rating
        self.rooms = rooms
        self.filename = f"hotel_{name}.json"

    def save_file(self):
        """Method to save hotel to a JSON file"""
        info = {
            'name': self.name,
            'rating': self.rating,
            'rooms': self.rooms
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(info, f)

    @staticmethod
    def create_hotel(name, rating, rooms):
        """Method for creating a hotel"""
        hotel = Hotel(name, rating, rooms)
        hotel.save_file()
        return hotel

    @staticmethod
    def load_hotel(name):
        """Method to load hotel from a JSON file"""
        filename = f"hotel_{name}.json"
        with open(filename, 'r', encoding='utf-8') as f:
            info = json.load(f)

        hotel_name = info['name']
        rating = info['rating']
        rooms = info['rooms']

        return Hotel(hotel_name, rating, rooms)

    @staticmethod
    def delete_hotel(name):
        """Method to delete hotel file"""
        filename = f"hotel_{name}.json"
        os.remove(filename)

    def display_hotel(self):
        """Method to display hotel information"""
        name = self.name
        rating = self.rating
        rooms = self.rooms

        print(f"Hotel: {name}, Stars: {rating}, Rooms: {rooms}")

    def update_hotel(self, name=None, rating=None):
        """Method to update hotel information"""
        if name:
            self.name = name
        if rating:
            self.rating = rating
        self.save_file()

    def reserve_room(self, room_id):
        """Method to reserve a room if available"""
        available = self.rooms.get(room_id)
        if available:
            self.rooms[room_id] = False

    @staticmethod
    def cancel_reservation(reservation_id):
        """Method to delete reservation file"""
        filename = f"reservation_{reservation_id}.json"
        os.remove(filename)
