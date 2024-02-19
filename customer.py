"""
Module for creating customers with Customer class
"""

import json
import os


class Customer:
    """Class for managing hotel customers"""

    def __init__(self, customer_id, first_name, last_name, phone):
        """Initialization method"""
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.filename = f"customer_{customer_id}.json"

    def save_file(self):
        """Method to save customer to a JSON file"""
        info = {
            'customer_id': self.customer_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(info, f)

    @staticmethod
    def create_customer(customer_id, first_name, last_name, phone):
        """Method for creating a customer"""
        customer = Customer(customer_id, first_name, last_name, phone)
        customer.save_file()
        return customer

    @staticmethod
    def load_customer(customer_id):
        """Method to load customer from a JSON file"""
        filename = f"customer_{customer_id}.json"
        with open(filename, 'r', encoding='utf-8') as f:
            info = json.load(f)

        c_id = info['customer_id']
        first_name = info['first_name']
        last_name = info['last_name']
        phone = info['phone']

        return Customer(c_id, first_name, last_name, phone)

    @staticmethod
    def delete_customer(customer_id):
        """Method to delete customer file"""
        filename = f"customer_{customer_id}.json"
        os.remove(filename)

    def display_customer(self):
        """Method to display customer information"""
        customer_id = self.customer_id
        first_name = self.first_name
        last_name = self.last_name
        phone = self.phone

        print(f"Customer ID: {customer_id}, "
              f"First Name: {first_name}, "
              f"Last Name: {last_name}, "
              f"Phone Number: {phone}")

    def update_customer(self, first_name=None, last_name=None, phone=None):
        """Method to update customer information"""
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if phone:
            self.phone = phone
        self.save_file()
