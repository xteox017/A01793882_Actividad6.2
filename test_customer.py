"""Module for Unit Testing of the customer module"""

import unittest
import os
import io
from unittest.mock import patch
from customer import Customer


class TestCustomer(unittest.TestCase):
    """Class to perform Customer unit tests"""

    def setUp(self):
        """Method for SetUp"""
        self.customer = Customer(
            customer_id='setup',
            first_name='First',
            last_name='Last',
            phone=1234567890)

    def test_customer_init(self):
        """Method to verify initialization"""
        self.assertEqual(self.customer.customer_id, 'setup')
        self.assertEqual(self.customer.first_name, 'First')
        self.assertEqual(self.customer.last_name, 'Last')
        self.assertEqual(self.customer.phone, 1234567890)

    def test_create_customer(self):
        """Method to verify customer creation"""
        Customer.create_customer('create_test', 'Create', 'Test', 2)
        expected_filename = "customer_create_test.json"
        self.assertTrue(os.path.exists(expected_filename),
                        "Customer file should exist")
        os.remove("customer_create_test.json")

    def test_load_file(self):
        """Method to verify customer loading"""
        load_test_customer = Customer.create_customer(
            'load_test', 'Load', 'Test', 3)
        loaded_customer = Customer.load_customer('load_test')

        self.assertEqual(loaded_customer.customer_id,
                         load_test_customer.customer_id,
                         "Customer IDs should be the same")
        self.assertEqual(loaded_customer.first_name,
                         load_test_customer.first_name,
                         "First Names should be the same")
        self.assertEqual(loaded_customer.last_name,
                         load_test_customer.last_name,
                         "Last Names should be the same")
        self.assertEqual(loaded_customer.phone, load_test_customer.phone,
                         "Phone Numbers should be the same")
        os.remove("customer_load_test.json")

    def test_delete_customer(self):
        """Method to verify customer deletion"""
        Customer.create_customer('delete_test', 'Delete', 'Test', 4)
        expected_filename = "customer_delete_test.json"
        self.assertTrue(os.path.exists(expected_filename),
                        "Customer file should exist")
        Customer.delete_customer('delete_test')
        self.assertFalse(os.path.exists(expected_filename),
                         "Customer file should no longer exist")

    def test_display_customer(self):
        """Method to verify display"""
        customer = Customer('display_test', 'Display', 'Test', 5)
        disp = ("Customer ID: display_test, "
                "First Name: Display, "
                "Last Name: Test, "
                "Phone Number: 5\n")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            customer.display_customer()
            self.assertEqual(fake_out.getvalue(), disp,
                             "The displayed information should be the same")

    def test_update_customer(self):
        """Method to verify update"""
        new_first_name = 'Updated First'
        new_last_name = 'Updated Last'
        new_phone = 6

        self.customer.update_customer(new_first_name, new_last_name, new_phone)

        self.assertEqual(self.customer.first_name, new_first_name)
        self.assertEqual(self.customer.last_name, new_last_name)
        self.assertEqual(self.customer.phone, new_phone)


if __name__ == '__main__':
    unittest.main()
