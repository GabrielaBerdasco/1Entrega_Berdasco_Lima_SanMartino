# PROYECTO SANATORIO SAN MARTINO

Desarrollo para el curso de Python, institución CoderHouse, camada 41220. 
Profesor a cargo: Pedro Rojas Gavidia.

**Nota importante:** Para las variables de ambiente se utilizó python-dotenv por lo que, para correr el código, es necesario crear un archivo .env dentro de la carpeta sanatorio_San_Martino, donde se encuentra el archivo settings.py, con variable SECRET_KEY_ENV que contenga secret_key de Django.

#### Vista sin loguear

![Demonstration web](./sanatorio_San_Martino/app_sanatorio/static/app_sanatorio/assets/img/inicial.gif)

#### Vista registro y funcionalidad usuario general

![Demonstration web](./sanatorio_San_Martino/app_sanatorio/static/app_sanatorio/assets/img/usuariogral.gif)

#### Vista funcionalidad usuario staff

![Demonstration web](./sanatorio_San_Martino/app_sanatorio/static/app_sanatorio/assets/img/usuarioStaff.gif)

## Sobre el proyecto

Proyecto elaborado sobre sanatorio ficticio para la consulta de médicos por especialidad, blog con vista de informacion del sanatorio, registro y login de usuarios staff (medicos, personal del sanatorio) y usuarios en general (pacientes). Cada usuario que sea parte del staff podrá realizar, editar y eliminar posteos en el blog, además podrá hacer comentarios sobre otros artículos del blog. El usuario general podrá realizar comentarios en los blogs del sanatorio así como también eliminarlos. 

Realizado en grupo por:
> **Francisco Lima** que se encargó de migrar las bases de datos, modificó template base - views - url, creó el modelo blog, carpeta media, views -  url de artículo e implementó los test unitarios.

> **Gabriel San Martino** fue responsable de crear la app sanatorio, el template base, login y logout, también de implementar ckeditor, agregar view - urls- template para editar y eliminar entradas del blog y los comentarios.

> **Gabriela Berdasco** fue la encargada de iniciar el proyecto junto con el readme, crear app cuentas y app blog, agregar view - url - template para cargar avatar y editar perfil, también de adaptar el front.

Cabe destacar que el proyecto fue realizado en varias reuniones de meet grupales en donde todos los miembros participaron activamente aportando conocimientos adquiridos en el curso y por medio de investigación independiente.


## Funcionalidad del proyecto

El proyecto se realizó con Python versión 3.10.6, en base a una plantilla obtenida de startBootstrap. Se comenzó el desarrollo en la plantilla base que contiene tanto nav como footer y una imagen acorde al tema de la página como fondo. Luego se desarrolló la vista de inicio donde agregamos distintos "call to action" para guiar al usuario de acuerdo a su búsqueda o necesidad. Dentro del nav se estableció qué al hacer click en el nombre del sanatorio, ubicado en la esquina superior izquierda, navegue hacia la página de inicio (url: '/'), también hay un enlace para la página sobre nosotros (url: 'about/') con información de los miembros del proyecto. El resto de los enlaces del nav se corresponden con la carga y consumo de datos en la db (url: 'page/' para listar entradas de blog, 'crear-blog' para crear una nueva entrada, habilitado sólo para miembros del staff) y el tratamiento de la información del usuario (se correponde con app_cuentas, url: 'accounts/'). Independientemente en la pantalla de inicio se encuentra un botón para la búsqueda de médicos por especialidad, en la página listar blog se encuentra un enlace para visualizar cada artículo del blog de acuerdo a su id(url: 'page/page#'), para eliminar o editar dicha entrada así como también para realizar comentarios (los que sólo podrán ser eliminados por el usuario que los creó).


### Dependencias extras:

* Django: Creación de la aplicación para el desarrollo optimizado.

* Python-Dotenv: Se encarga de controlar todos los pares de key-values de un archivo que sea etiquetado como archivo de entorno o .env y, después, es el encargado de configurarlos como variables del entorno.

* SQLite3: Se utilizó para almacenar colecciones de datos, las mismas almacenan los datos ingresados por los usuarios. Adicionalmente, se consumen de acuerdo al pedido del usuario.

* CKEditor: es un editor de texto versátil el cuál nos sirve para dar estilo personalizado al campo de escritura de los blogs y los comentarios.

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


