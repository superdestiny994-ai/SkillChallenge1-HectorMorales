Este proyecto es la reorganizacion de un script básico de lista de tareas. Lo que se hizo fue separar las distintas "responsabilidades" del código original,
que estaba todo en un solo archivo, en carpetas independientes, utilizando el diseño Modelo-Vista-Controlador (MVC). De esta manera, el código 
es más ordenado, fácil de leer y de mantener.

Estructura del proyecto:

- main.py: Es el archivo principal que inicia la aplicación.
- Modelo/datos.py: Se encarga exclusivamente de guardar y manipular los datos de las tareas en memoria. Contiene las funciones para añadir, completar y eliminar tareas.
- VIsta/interfaz.py: Controla todo lo que el usuario ve en la consola. Se encarga de imprimir los menus, mostrar la lista y recibir los datos que ingresa el usuario.
- Control/logica.py: Actúa como el intermediario. Toma la información que ingresa el usuario en la vista, la envía al modelo para que se procese, y decide qué mostrar después.

Manejo de errores:

El script original se caía si se ingresaban datos incorrectos. Para solucionar esto, añadi algunas validaciones sencillas:
- Si el usuario ingresa letras o texto cuando el sistema le pide el número de una tarea para completar o eliminar, el programa muestra un aviso y vuelve a preguntar en 
  lugar de cerrarse.
- Si el usuario ingresa un número que no corresponde a ninguna tarea (fuera de rango), el sistema le indica cuáles son los números válidos.
- Si se intenta completar o eliminar tareas cuando la lista está completamente vacía, el programa lo detecta y lo notifica.
- Al agregar una tarea, se valida que el usuario no envíe un texto vacío o lleno de espacios.

Cómo ejecutar el programa:

Para iniciar el sistema de tareas, abre tu consola en esta carpeta y ejecuta el siguiente comando:

 "python main.py"
