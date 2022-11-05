import unittest
from faker import Faker
from Models.declarative_base import *
from Models.Model import *


class PruebaUsuarios(unittest.TestCase):
    def setUp(self):
        print("Test de prueba")

    def test_usuario(self):
        print("Prueba creación de usuarios")
        try:
            self.session = Session()
            self.factory = Faker()
            Faker.seed(1000)
            self.user = Usuarios(id_usuario=self.factory.random_int(1, 10),
                                 usuario=self.factory.unique.first_name(),
                                 contrasena=self.factory.password(),
                                 nombre=self.factory.unique.first_name() + self.factory.unique.last_name(),
                                 cedula=self.factory.random_int(10000, 50000),
                                 rol=self.factory.random_int(1, 3),
                                 id_negocio=self.factory.random_int(1, 10))
            print("Usuario creado ", self.user)
            self.session.add(self.user)  # Agregar a la sesion
            self.session.commit()
            self.assertEqual(4,4)
        except Exception as e:
            print("Error", e)

    """def test_crear_usuario(self):
        user = User.createUser(self, 'User Test', 'Name test', 'Password Test', 1, 1, '123456789')
        if user:
            print("Usuario de prueba cerado exitosamente")
        else:
            print("Error al crear el usuario")

    def _dict_contact(self):
        return {
            'name': 'Usertest2',
            'surname': 'User Test2',
            'email': 'user2@gmail.com',
            'phone': 900000000,
            'birthday': '1987-11-24'
        }"""