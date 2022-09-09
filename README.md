# SDPVES

#### Sistema para la determinación de personas vacunadas en El Salvador.

###### Proyecto para la cátedra: _Herramientas de Productividad, Ciclo I-2021._

## Antes de empezar

* Este proyecto se trabaja con PyCharm exclusivamente.

* Este proyecto hace uso de Python, Django y MySQL/MariaDB.


* Abra la GUI para gestionar sus bases de datos e ingrese con el usuario `root`.
    * Cree el siguiente usuario:  
      usuario: `hdp`  
      contraseña: `hdp`

    * Cree la base de datos `sdpves`.


* Procure tener instalada la versión de Python 3.9.5 (se trabaja con esta versión).


* Instale:  
  `virtualenv`  
  `virtualenvwrapper` y  
  `virtualenvwrapper-win`  
  mediante `pip install virtualenv virtualenvwrapper virtualenvwrapper-win`.


* Cree un entorno virtual llamado `sdpves` con `mkvirtualenv sdpves`.


* Si el entorno existe, bórrela y créela de nuevo.


* A partir de aquí estará dentro automáticamente en su entorno virtual.


* Instale las librerías necesarias mediante: `pip install -r requirements.txt`.


* Cierre el entorno virtual ejecutando directamente `deactivate` y cierre la consola de comandos.

## Trabajando con PyCharm

* Abra PyCharm.


* Click en `Get from VCS`.


* Ingrese la url que proporciona el repositorio para clonar.


* Posiblemente pregunte que quiere abrir el proyecto. Selecciona que sí.


* Con el proyecto abierto, es posible que pida configurar el intérprete python que usará. Selecciónalo.


* Seleccione `Add Interpreter`.


* Se abrirá una ventana para crear entornos virtuales y seleccione `New existing environment`, y busque en la lista su  
  entorno virtual, en este caso `sdpves` y seleccionadla.


* Espere a que se configure todo y luego cierre PyCharm y abra de nuevo, abriendo el proyecto.


* Abra la terminal incluida con el IDE y verifique que `(sdpves)` está presente.  
  Caso contrario, ejecute: `workon sdpves`.


* Abra la pestaña `Database` que se encuentra al costado derecho.


* Clic en el símbolo más y agregue un nuevo datasource


* Seleccione el gestor: MySQL o MariaDB.


* Ingrese el usuario y contraseña previamente creada.


* Ingrese la base de datos para trabajar y finalice. Tendría que ver configurado todo.


* Ahí mismo verá una opción para descargar los drivers. Instálelo.


* Haga el siguiente atajo: `CTRL + ALT + R`. Esto le abrirá una nueva pestaña.


* Ejecute en orden:
    * `makemigrations vacunacion`
    * `migrate`
    * `createsuperuser`. El usuario a crear es `hdp` y su contra es `hdp`.


* Abra otra vez la pestaña Database y diríjase a la tabla departamento.


* Haga click derecho y seleccione `Import Data From File`, busque el archivo que se encuentra en este repositorio  
  en la carpeta `backups-tablas` y selecciona el respectivo archivo. Verifique que `First row is header` esté  
  seleccionada y de clic en Import.


* Repita lo mismo para la tabla municipios.


* Ahora abra la pestaña que se abrió al realizar el atajo `CTRL + ALT + R` y ejecute `runserver`.


* Abra su navegador y coloque la dirección `localhost:8000` y verá el proyecto andando.

A partir de aquí puede continuar libremente con el desarrollo.

Si quiere abrir el administrador, abra: `localhost:8000/admin` e ingrese las credenciales creadas anteriormente.

## Desarrollo

* Todo cambio puede colocarse directamente a `main` o subir su propia rama.


* Si instaló librerías, realice `pip freeze > requirements.txt` para actualizar la lista de  
  librerías.

## Copyright

* _Josué Andrés Hernández Martínez_
