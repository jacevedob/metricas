import unittest
import os
import sys

myDir = os.getcwd()
sys.path.append(myDir)

from Database.baseDatos import DB
from Models.User import User


class PruebaUsuaurios(unittest.TestCase):

    def test_crear_usuario(self):
         return User.createUser(self, 'User Test','Name test', 'Password Test', 1, 1, '123456789')

    def _dict_contact(self):
        return {
            'name': 'Usertest2',
            'surname': 'User Test2',
            'email': 'user2@gmail.com',
            'phone': 900000000,
            'birthday': '1987-11-24'
        }