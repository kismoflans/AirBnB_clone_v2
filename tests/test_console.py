#!/usr/bin/python3
"""
Unittest for the Console class
Test files by using the following command line:
python3 -m unittest tests/test_console.py
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import models
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    """Define variables and methods for testing"""

    def setUp(self):
        """Set up for the tests"""
        models.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after tests"""
        models.storage._FileStorage__objects = {}

    def test_help_command(self):
        """Test the 'help' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help')
            output = f.getvalue().strip()
        self.assertIn('Documented commands', output)

    def test_quit_command(self):
        """Test the 'quit' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            result = HBNBCommand().onecmd('quit')
        self.assertIsNone(result)  # quit should return None to exit

    def test_create_command(self):
        """Test the 'create' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            output = f.getvalue().strip()
        self.assertTrue(len(output) > 0)  # Ensure an ID is printed

    def test_show_command(self):
        """Test the 'show' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show User {user_id}')
            output = f.getvalue().strip()
        self.assertIn('User', output)
        self.assertIn(user_id, output)

    def test_destroy_command(self):
        """Test the 'destroy' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy User {user_id}')
            output = f.getvalue().strip()
        self.assertEqual('', output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show User {user_id}')
            output = f.getvalue().strip()
        self.assertIn("** no instance found **", output)

    def test_all_command(self):
        """Test the 'all' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            HBNBCommand().onecmd('all User')
            output = f.getvalue().strip()
        self.assertIn('User', output)

    def test_update_command(self):
        """Test the 'update' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update User {user_id} email "test@example.com"')
            output = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show User {user_id}')
            output = f.getvalue().strip()
        self.assertIn('email', output)
        self.assertIn('test@example.com', output)

    def test_default_command(self):
        """Test the default command method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.all()')
            output = f.getvalue().strip()
        self.assertIn('User', output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.count()')
            output = f.getvalue().strip()
        self.assertEqual(output, '1')  # Assuming one User was created

    def test_empty_line(self):
        """Test the empty line behavior"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('')
            output = f.getvalue().strip()
        self.assertEqual('', output)

    def test_EOF_command(self):
        """Test the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            result = HBNBCommand().onecmd('EOF')
        self.assertIsNone(result)  # EOF should return None to exit


if __name__ == '__main__':
    unittest.main()
