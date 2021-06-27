# SDPVES

#### Sistema para la determinación de personas vacunadas en El Salvador.

###### Proyecto para la cátedra: _Herramientas de Productividad, Ciclo I-2021._

## Notas antes de empezar

* Este proyecto se trabaja con PyCharm Professional 2021.1, en su versión gratuita para estudiantes. Puede trabajar con
  cualquier otro editor pero se prefiere este por facilidad de uso y su alta integración con Django.


* Este proyecto hace uso de Python 3.9.5, Django 3.2.4 y MySQL o MariaDB. Este proyecto usa MariaDB 10.5.11, pero puede
  perfectamente trabajar con MySQL en su versión más reciente.

## Preparando el ambiente

* Abra la GUI para gestionar sus bases de datos (o por consola) e ingrese con el usuario `root`.
    * Cree el siguiente usuario:  
      usuario: `hdp`  
      contraseña: `hdp`

    * Cree la base de datos `sdpves`.


* Instale:  
  `virtualenv` y  
  `virtualenvwrapper`
  mediante `pip install virtualenv virtualenvwrapper`.

* Si trabaja en Windows, instale: `virtualenvwrapper-win`.


* Cree la nueva variable de entorno en su equipo: `WORKON_HOME` con el valor: `usuario/.virtualenvs`, donde `usuario` es
  la ruta a la carpeta del usuario actualmente en uso. Ejemplo: `C:\Users\MiUsuario\`, en Windows, o `/home/miusuario/`
  en Linux.

  Esto hace que todos los entornos virtuales se creen en la carpeta especificada. Por defecto es `Envs` pero PyCharm no
  detecta dicha carpeta y los entornos no son reconocidos.


* Abra un terminal y cree el entorno virtual llamado `sdpves` (o el nombre que prefiera) con el
  comando `mkvirtualenv sdpves`.


* Si el entorno existe, bórrela y créela de nuevo.


* A partir de aquí estará dentro automáticamente en su entorno virtual.


* Clone este repositorio. Esto creará la carpeta SDPVES en la ruta donde ejecutó el comando de clonación.


* Entre a la carpeta SDPVES.


* Ejecute `setprojectdir .`. Esto es para hacer que cada vez que quiera entrar al entorno virtual `sdpves`, lo dirija
  automáticamente al interior de la carpeta SDPVES.


* Instale las librerías necesarias mediante: `pip install -r requirements.txt`.


* Cierre el entorno virtual con el siguiente comando: `deactivate`, y cierre la consola de comandos.

## Configurando PyCharm

### Python

* Abra PyCharm y abra la carpeta SDPVES.


* Ahora, diríjase a `Settings` y busque `Python Interpreter` en la sección relacionada con el proyecto. Esta ventana
  listará las versiones de Python instaladas en su sistema. Seleccione la tuerca y de clic en
  `Add`. Esto abrirá una ventana y, verifique que la opción del costado izquierdo sea `Virtualenv Environment`. Ahora
  verifique que la opción `Existing environment` esté seleccionada. Aquí, debería de aparecer el entorno virtual
  previamente creado. Selecciónela. Esto debería de dejarle en un entorno listo para programar.

### Base de datos

* Abra la pestaña `Database` que se encuentra al costado derecho.


* Clic en el símbolo más y agregue un nuevo datasource


* Seleccione el gestor: MySQL o MariaDB (dependerá de cuál está usando).


* Ingrese el usuario y contraseña previamente creada.


* Ingrese el nombre de la base de datos para trabajar y finalice. Tendría que ver configurado todo.


* Ahí mismo verá una opción para descargar los drivers. Descárguelos.


* Pruebe la conexión dando en `Test Connection`. Si todo está bien, de en `Apply`, caso contrario, verifique pasos
  anteriores o alguna otra posible falla. Luego, minimize la pestaña.


* Ahora, realice el siguiente atajo: `CTRL + ALT + R`. Esto le abrirá una nueva pestaña.


* Ejecute en orden:
    * `makemigrations vacunacion`
    * `migrate`
    * `createsuperuser`

  El usuario a crear es `admin` y su contra es `admin` (puede ser cualquier otro). En el apartado de correo, presione
  ENTER y continue. Le dirá que la contraseña es insegura. Para pruebas, presione `y` para aceptar la contraseña y que
  se cree el usuario.


* Abra otra vez la pestaña Database y diríjase a la tabla departamento.


* Haga click derecho y seleccione `Import Data From File`, busque el archivo que se encuentra en este repositorio  
  en la carpeta `backups-tablas` y selecciona el respectivo archivo.


* Repita lo mismo para la tabla municipio y persona.

### Arrancando el proyecto

* Ahora abra la pestaña que se abrió al realizar el atajo `CTRL + ALT + R` y ejecute `runserver`.


* Abra su navegador y coloque la dirección `127.0.0.1:8000` y verá el proyecto andando. A partir de aquí puede continuar
  libremente con el desarrollo.

### El administrador del sistema SDPVES
Para trabajar como el administrador del sistema SDPVES, presione el botón: `INICIAR SESIÓN` e ingrese las credenciales `admin` y `admin`.
Esta ventana es una forma más amigable que el administrador propio de Django dado que se hicieron ciertas modificaciones a favor de un mejor experiencia de uso.  

Esta presentación del panel de administración se limita a lo usado en el proyecto exclusivamente, es decir, no puede administrar más
cosas de otros modulos. Para ello, debe volver a habilitar el panel de administración de Django, descomentandolo en `urlpatterns`,
en el archivo `urls,py` del proyecto `sdpves`. Una vez finalizada las acciones que requieran usar este panel de administración durante
su desarrollo, procure deshabilitarlo nuevamente antes de subir sus cambios.


## Desarrollo

* Todo cambio puede colocarse directamente a `main` o subir su propia rama.


* Si instaló librerías, realice `pip freeze > requirements.txt` para actualizar la lista de librerías y mencione su
  inclusión o eliminación en el commit que vea necesario. Pero, si una librería no se usa, pero tampoco se elimina, en
  el commit correspondiente detalle el por qué se ha ignorado en el código.

# Copyright 2021

* _Josué Andrés Hernández Martínez_
