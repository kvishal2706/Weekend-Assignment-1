import unittest
import json
import os

def add_art_space(name, location, description):
    # Create a dictionary to hold the art space details
    art_space = {
        'name': name,
        'location': location,
        'description': description
    }

    # Open the file to store the art space details
    with open('art_spaces.json', 'a') as file:
        # Write the art space details to the file
        file.write(json.dumps(art_space))
        file.write('\n') # add a newline character to separate entries

    # Return a message indicating success
    return f'Art space {name} added successfully!'

class TestAddArtSpace(unittest.TestCase):

    def setUp(self):
        # Create a new test file to store art space details
        self.filepath = 'test_art_spaces.json'
        with open(self.filepath, 'w') as file:
            file.write('')

    def tearDown(self):
        # Remove the test file
        os.remove(self.filepath)

    def test_add_art_space(self):
        # Define the details of the new art space
        name = 'Test Art Space'
        location = 'Test Location'
        description = 'Test Description'

        # Add the art space to the file and store the result
        result = add_art_space(name, location, description)

        # Check that the result is as expected
        expected_output = f'Art space {name} added successfully!'
        self.assertEqual(result, expected_output)

        # Check that the file now contains the new art space
        with open(self.filepath, 'r') as file:
            art_spaces = [json.loads(line) for line in file]
            self.assertEqual(len(art_spaces), 1)
            self.assertEqual(art_spaces[0]['name'], name)
            self.assertEqual(art_spaces[0]['location'], location)
            self.assertEqual(art_spaces[0]['description'], description)


#USER MANAGEMENT SYSTEM

class UserProfile:
    def __init__(self, name="", bio="", location=""):
        self.name = name
        self.bio = bio
        self.location = location

class UserAccount:
    def __init__(self, username="", password="", email=""):
        self.username = username
        self.password = password
        self.email = email
        self.profile = UserProfile()

    def set_profile(self, name="", bio="", location=""):
        self.profile.name = name
        self.profile.bio = bio
        self.profile.location = location

class UserManagementSystem:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password, email):
        if username not in self.users:
            self.users[username] = UserAccount(username, password, email)
            return True
        else:
            return False

    def login(self, username, password):
        if username in self.users:
            user = self.users[username]
            if user.password == password:
                return user
        return None

    def update_profile(self, user, name="", bio="", location=""):
        user.set_profile(name, bio, location)


class UserProfile:
    def __init__(self, name="", bio="", location=""):
        self.name = name
        self.bio = bio
        self.location = location

class UserAccount:
    def __init__(self, username="", password="", email=""):
        self.username = username
        self.password = password
        self.email = email
        self.profile = UserProfile()

    def set_profile(self, name="", bio="", location=""):
        self.profile.name = name
        self.profile.bio = bio
        self.profile.location = location

class UserDatabase:
    def __init__(self):
        self.users = {}

    def create_user(self, username="", password="", email=""):
        if username in self.users:
            return False

        self.users[username] = UserAccount(username, password, email)
        return True

    def login(self, username="", password=""):
        if username not in self.users:
            return None

        user = self.users[username]
        if user.password != password:
            return None

        return user

    def update_profile(self, user=None, name="", bio="", location=""):
        if user is None:
            return False

        user.set_profile(name, bio, location)
        return True

class ProgrammingManagement:
    def __init__(self):
        self.programming_items = {}

    def create_programming(self, name, description, category, date, location, performers):
        # logic to create a new programming item in the database
        programming_item = {
            'name': name,
            'description': description,
            'category': category,
            'date': date,
            'location': location,
            'performers': performers
        }
        # generate a unique ID for the new programming item
        programming_id = len(self.programming_items) + 1
        # save the programming item in the database with its ID
        self.programming_items[programming_id] = programming_item
        # return the ID of the new programming item
        return programming_id

    def get_programming(self, id):
        # logic to get a programming item from the database using its ID
        if id in self.programming_items:
            return self.programming_items[id]
        else:
            return None

    def update_programming(self, id, name=None, description=None, category=None, date=None, location=None, performers=None):
        # logic to update a programming item in the database using its ID
        programming_item = self.get_programming(id)
        if programming_item:
            if name:
                programming_item['name'] = name
            if description:
                programming_item['description'] = description
            if category:
                programming_item['category'] = category
            if date:
                programming_item['date'] = date
            if location:
                programming_item['location'] = location
            if performers:
                programming_item['performers'] = performers
            # save the updated programming item in the database
            self.programming_items[id] = programming_item
            return programming_item
        else:
            return None

    def delete_programming(self, id):
        # logic to delete a programming item from the database using its ID
        if id in self.programming_items:
            del self.programming_items[id]
            return True
        else:
            return False

import unittest

class TestProgrammingManagement(unittest.TestCase):

    def setUp(self):
        self.programming_management = ProgrammingManagement()
        self.programming_id = self.programming_management.create_programming('Test Programming', 'This is a test programming item', 'music', '2023-04-01', 'New Delhi', ['performer1', 'performer2'])

    def test_create_programming(self):
        result = self.programming_management.create_programming('Test Programming', 'This is a test programming item', 'music', '2023-04-01', 'New Delhi', ['performer1', 'performer2'])
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)

    def test_get_programming(self):
        result = self.programming_management.get_programming(self.programming_id)
        self.assertIsNotNone(result)

    def test_update_programming(self):
        result = self.programming_management.update_programming(self.programming_id, name='Updated Programming', location='Mumbai')
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Updated Programming')
        self.assertEqual(result['location'], 'Mumbai')

    def test_delete_programming(self):
        result = self.programming_management.delete_programming(self.programming_id)
        self.assertTrue(result)
