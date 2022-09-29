import random
import string

from django.test import TestCase
from django.contrib.auth.models import User

from app_blog.models import Blog, Comentario


class BlogTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Crea objetos que no se modifican en ninguno de los métodos de prueba.
        User.objects.create(username='Testing')

    def setUp(self):
        # Crea objeto que puede ser modificado durante la prueba.
        Blog.objects.create(titulo='A test', subtitulo='Una prueba', cuerpo='Esto es una prueba.')

    def test_creacion_entrada(self) :
        # Test 1: Comprueba que se pueda crear una entrada de blog con letras y número al azar.
        lista_letra_titulo = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        lista_letra_subtitulo = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        lista_letra_cuerpo = [random.choice(string.ascii_letters + string.digits) for _ in range(50)]
        titulo_prueba = "".join(lista_letra_titulo)
        subtitulo_prueba = "".join(lista_letra_subtitulo)
        cuerpo_prueba = "".join(lista_letra_cuerpo)
        blog1 = Blog.objects.create(titulo = titulo_prueba, subtitulo = subtitulo_prueba,cuerpo = cuerpo_prueba)
        print(titulo_prueba)
        print(subtitulo_prueba)
        print(cuerpo_prueba)


        self.assertIsNotNone(blog1.id) 
        self.assertEqual(blog1.titulo, titulo_prueba)
        self.assertEqual(blog1.subtitulo,subtitulo_prueba)
        self.assertEqual(blog1.cuerpo, cuerpo_prueba)


    def test_creacion_comentario(self) :
        # Test 2: Crea las foreing keys necesarias y comprueba que se pueda crear un comentario con letras y número al azar.
        usuario = User.objects.get(username='Testing')
        articulo = Blog.objects.get(titulo='A test')
        articulo.autor=usuario
        lista_letra_comentario = [random.choice(string.ascii_letters + string.digits) for _ in range(50)]
        comentario_prueba = "".join(lista_letra_comentario)
        comentario1 = Comentario.objects.create(articulo = articulo, cuerpo = comentario_prueba, autor = usuario)
        print(comentario_prueba)

        self.assertIsNotNone(comentario1.id) 
        self.assertIsNotNone(comentario1.articulo) 
        self.assertIsNotNone(comentario1.autor) 
        self.assertEqual(comentario1.cuerpo, comentario_prueba)
        self.assertEqual(comentario1.articulo, articulo)
        self.assertEqual(comentario1.autor, usuario)



