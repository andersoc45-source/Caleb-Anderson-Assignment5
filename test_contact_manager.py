# test_contact_manager.py
import unittest
from contact_manager import add_contact, find_contact, delete_contact, DuplicateContactError

class TestContactManager(unittest.TestCase):

    def test_add_contact(self):
        # Add Robert to contacts.
        contacts = {}
        add_contact("Robert", "111-111-1111", contacts)
        self.assertIn("Robert", contacts)

    def test_find_contact(self):
        # Find Laura in contacts.
        contacts = {"Laura": "222-222-2222"}
        phone = find_contact("Laura", contacts)
        self.assertEqual(phone, "222-222-2222")

    def test_find_contact_with_expected_failure(self):
        # Find Sam in contacts with expected failure.
        contacts = {"Laura": "222-222-2222"}
        phone = find_contact("Sam", contacts)
        self.assertEqual(phone, None)

    def test_delete_contact(self):
        # Delete Amy from contacts.
        contacts = {"Amy": "333-333-3333"}
        delete_contact("Amy", contacts)
        self.assertEqual(contacts, {})

    def test_delete_contact_with_expected_failure(self):
        # Delete Bob from contacts with expected failure.
        contacts = {"Amy": "333-333-3333"}
        delete_contact("Bob", contacts)
        self.assertEqual(contacts, {"Amy": "333-333-3333"})

    def test_add_duplicate_contact(self):
        # Raise a DuplicateContactError by attempting to duplicate Beth.
        contacts = {"Beth": "444-444-4444"}
        with self.assertRaises(DuplicateContactError):
            add_contact("Beth", "444-444-4444", contacts)

if __name__ == '__main__':
    unittest.main() # This line runs all tests in this file