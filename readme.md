# PROYECTO SANATORIO SAN MARTINO

Desarrollo para el curso de Python, institución CoderHouse, camada 41220. Tutor encargado: Esteban Acevedo.

## Sobre el proyecto

Proyecto elaborado sobre sanatorio ficticio para la consulta de médicos por especialidad y para la carga de datos de pacientes, médicos y obras sociales. Realizado en grupo por Francisco Lima, Gabriel San Martino y Gabriela Berdasco.

## Funcionalidad del proyecto

El proyecto se realizó con Python versión 3.10.6, en base a una plantilla obtenida de startBootstrap. Se comenzó el desarrollo en la plantilla base que contiene tanto nav como footer y una imagen acorde al tema de la página como fondo. Luego se desarrollo la vista de inicio donde agregamos distintos "call to action" para guiar al usuario de acuerdo a su búsqueda o necesidad. Dentro del nav se estableció qué al hacer click en el nombre del sanatorio, ubicado en la esquina superior izquierda, navegue hacia la página de inicio. El resto de los enlaces del nav se corresponden con la carga de datos en la db para cada uno de los modelos creados. Independientemente en la pantalla de inicio se encuentra un botón para la búsqueda de médicos por especialidad.


### Dependencias extras:

* Django: Creación de la aplicación para el desarrollo optimizado.

* Python-Dotenv: Se encarga de controlar todos los pares de key-values de un archivo que sea etiquetado como archivo de entorno o .env y, después, es el encargado de configurarlos como variables del entorno.

* SQLite3: Se utilizó para almacenar colecciones de datos. Las tres colecciones almacenan los datos ingresados por el usuario. Adicionalmente, la colección "médicos" se consume desde la app de acuerdo al pedido del usuario.

## Instrucciones para probar la app

1. En la terminal, seleccionar la carpeta donde se almacenará el proyecto.

> cd mi_carpeta

2. Clonar el repositorio con el comando: 

> git clone https://github.com/GabrielaBerdasco/1Entrega_Berdasco_Lima_SanMartino.git

3. En la carpeta seleccionada se creará una nueva carpeta con el código por lo que deberás moverte a dicha carpeta.

> cd sanatorio_San_Martino

4. Instalar las dependencias necesarias para correr el proyecto.

> pip install -r requirements.txt

5. Al terminar la instalación, ejecutar el comando para iniciar el servidor en la aplicación.

> python manage.py runserver

6. Para terminar el proceso en Windows presionar en la consola:

> ctrl + C 

