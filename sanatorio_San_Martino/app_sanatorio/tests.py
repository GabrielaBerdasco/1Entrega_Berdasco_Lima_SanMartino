import random
import string

from django.test import TestCase

from app_sanatorio.models import Medico

class MedicoTestCase(TestCase):
    pass

    def test_creacion_medico(self):
        # Test 1: Comprueba que se pueda crear un médico con letras y número al azar.
            lista_letra_nombre = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
            lista_letra_apellido = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
            lista_letra_especialidad = [random.choice(string.ascii_letters + string.digits) for _ in range(50)]
            nombre_prueba = "".join(lista_letra_nombre)
            apellido_prueba = "".join(lista_letra_apellido)
            especialidad_prueba = "".join(lista_letra_especialidad)
            medico = Medico.objects.create(nombre = nombre_prueba, apellido = apellido_prueba, especialidad = especialidad_prueba)
            print(nombre_prueba)
            print(apellido_prueba)
            print(especialidad_prueba)


            self.assertIsNotNone(medico.id) 
            self.assertEqual(medico.nombre, nombre_prueba)
            self.assertEqual(medico.apellido,apellido_prueba)
            self.assertEqual(medico.especialidad, especialidad_prueba)
