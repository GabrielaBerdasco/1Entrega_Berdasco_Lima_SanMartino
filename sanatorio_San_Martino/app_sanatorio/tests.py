import random
from re import sub 
import string

from django.test import TestCase
from app_blog.models import Blog, Comentario

class BlogTestCase(TestCase):
    pass


    def test_creacion_entrada(self) :
        lista_letras_titulo = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        lista_letra_subtitulo = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        lista_letra_cuerpo = [random.choice(string.ascii_letters + string.digits) for _ in range(50)]
        titulo_prueba = " ".join(lista_letras_titulo)
        subtitulo_prueba = " ".join(lista_letras_titulo)
        cuerpo_prueba = " ".join(lista_letras_titulo)
        blog1 = Blog.objects.create(titulo = titulo_prueba, subtitulo = subtitulo_prueba,cuerpo = cuerpo_prueba)

        self.assertIsNotNone(blog1.id) 
        self.assertEqual(blog1.titulo, titulo_prueba)
        self.assertEqual(blog1.subtitulo,subtitulo_prueba)
        self.assertEqual(blog1.cuerpo, cuerpo_prueba)


    def test_creacion_comentario(self) :
        lista_letra_comentario = [random.choice(string.ascii_letters + string.digits) for _ in range(50)]
        comentario_prueba = " ".join(lista_letra_comentario)
        comentario1 = Comentario.objects.create(comentario = comentario_prueba)
        
        self.assertIsNotNone(comentario1.id) 
        self.assertEqual(comentario1.titulo, comentario_prueba)


