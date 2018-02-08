---
layout: post
title: Juego en C++ - El ahorcado (con interfaz gráfica)
date: 2018-02-08
categories: c++
tags: juegos objetos proyectos
published: false

---
## Introducción

En el proyecto descripto en este artículo se usó el framework para C++ Qt 5.1.0 para generar la interfaz gráfica.

El IDE utilizado es Qt Creator (en su versión 2.7.2). Puede descargarse gratuitamente desde: [www.qt.io/download-open-source](www.qt.io/download-open-source)

Breve explicación del juego: en “el ahorcado” (“hangman” en inglés) se debe adivinar una palabra al azar. Para esto, en cada turno el jugador dice una letra del alfabeto que él supone es parte de la palabra. Si la letra no se encuentra en la palabra, se dibuja una parte de un hombrecito ahorcado (un poco truculento por ser un juego para niños, pero es así). Si la letra forma, efectivamente, parte de la palabra, no se dibuja ninguna parte y el jugador avanza. Las partes del ahorcado son 6: la cabeza, el tronco, los dos brazos y las dos piernas, por lo que el jugador tiene 5 chances de equivocarse.

![ilustración]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img0.png)

 
## Diseño y algoritmo

Según el nivel elegido por el usuario se le brindará determinada ayuda:

- Nivel 1: Se muestra la primera y la última letra
- Nivel 2: Se muestra sólo la primera letra
- Nivel 3: No hay ayuda

Las palabras se encuentran en un archivo de texto que se leerá, almacenando cada palabra en un string dentro de un contenedor.

El usuario cuenta con 6 oportunidades que estarán contabilizadas en una variable.

Una vez elegido el nivel y al comenzar el juego, se cargarán las palabras en el contenedor y se seleccionará una al azar. Para esto, se generará un número al azar menor a la cantidad máxima de elementos del contenedor y este número indicará la posición del elemento a seleccionar (índice). Una vez utilizada una palabra, se elimina del contenedor para que el usuario pueda continuar jugando sin repeticiones hasta que cierre el programa.

Comienza mostrándose una imagen de la horca vacía y tantas etiquetas como letras haya. Dependiendo del nivel, también se mostrarán las ayudas si corresponden. Cada etiqueta equivale a una letra.

Para acomodar las etiquetas se tomará el ancho de la ventana al que se le restarán 30 pixeles (para dejar un margen) y al resultado se lo dividirá por la cantidad de letras de la palabra para saber el tamaño de las etiquetas a generar. Éstas se generarán por código y se colocarán una al lado de otra.

Además existirá un cuadro de texto donde el usuario podrá ingresar una letra por vez, sin repetir, y un botón para indicar que está listo para arriesgar una oportunidad.

Cuando el usuario ingresa su opción, si la letra existe en la palabra se muestra en la etiqueta correspondiente y se contabiliza como letra ya utilizada. Si la letra no existe en la palabra se modifica la imagen de la horca para sumar una parte del ahorcado y se resta una oportunidad. Si la letra no existe y además al ahorcado le quedaba una sola parte por completar, se completa y el juego termina.

No se distinguen mayúsculas, minúsculas, vocales acentuadas o con diéresis (estos casos son tenidos en cuenta).

## Desarrollo: interfaz

Para comenzar con el desarrollo, en Qt Creator ir a **File > New file or project > Applications > Qt Gui Application** y continuar con el asistente hasta el final, dejando las opciones por defecto (podemos darle un nombre al proyecto).

![crear proyecto]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img1.png)

El proyecto tendrá una carpeta “Headers” para los archivos de encabezados, una carpeta “Sources” para los archivos de código fuente y una carpeta “Forms” para los archivos de la interfaz gráfica (“gui”) con la primera ventana ya creada.

![archivos del proyecto]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img2.png)

“Espiando” la implementación de la función main que da inicio al programa podremos ver que primero instancia una de estas ventanas y luego la muestra, con el siguiente código:

    MainWindow w;
    w.show();

Haciendo doble click sobre el archivo mainwindow.ui (o el nombre correspondiente si se lo hemos cambiado) se abrirá la pantalla de diseño donde podremos ver la primera ventana del programa, además de una extensa variedad de herramientas a su izquierda (con un filtro superior que permite buscar):

![pantalla de diseño]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img3.png)

En la parte inferior derecha pueden verse las propiedades del elemento gráfico actualmente seleccionado (en este caso, el único existente: la ventana -o formulario-), también con una opción de filtro para buscar. Todas estas propiedades pueden modificarse mediante el código, pero desde este menú es posible también hacerlo mediante la interfaz gráfica.

Con un click en la opción “palette” podemos modificar los colores:

![paleta de colores]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img4.png)

También podremos cambiarle el nombre a la ventana editando la propiedad “windowTitle”:

![nombre de la ventana]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img5.png)

Mediante las agarraderas de las esquinas es posible ampliar o reducir el tamaño de la ventana inicial, aunque también es posible modificar numéricamente el ancho y alto utilizando la propiedad “geometry”.

En el panel de la izquierda se encuentran todos los elementos que es posible agregar, agrupados en categorías. Para agregarlos, basta con arrastrarlos desde este panel hasta el formulario. En este caso, agregaremos dos “label” (en la categoría “display widgets”), tres “radio button” (en la categoría “buttons”) y un “push button” (en la categoría “buttons”).

![componentes agregados]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img6.png)

Para cambiar los textos basta con hacer doble click sobre el elemento. Por ejemplo, en un label pondremos el título “El ahorcado” y en otro pondremos “elegir nivel”. En los radio buttons pondremos los 3 niveles posibles: fácil, medio, difícil. Y en el push button pondremos “Jugar!”.

Para editar las propiedades de los textos, hacer click sobre el elemento deseado y, desde el panel inferior derecho, click en los “...” de la propiedad “font” para elegir un tipo y tamaño de fuente.

![propiedades de los textos]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img7.png)

![propiedades de los textos]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img8.png)

Pero el texto es sólo un elemento decorativo. Para programar, lo que nos interesa es el nombre de cada uno de estos objetos. Si hacemos click sobre alguno de ellos para seleccionarlo, veremos en el panel de propiedades su “objectName” y podremos cambiarlo por algún otro nombre que represente de qué objeto se trata.

![nombre del objeto]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img9.png)

Es conveniente darle un nombre a cada objeto que aparece en la pantalla, porque de esta manera los identificaremos en el código cuando les agreguemos funcionalidad. Excepcionalmente, a los objetos que no tendrán funcionalidad (como el título, por ejemplo) podríamos dejarles el nombre por defecto (en el caso de los objetos de la [clase](/poo/2016/01/07/programacion-orientada-a-objetos.html) _QLabel_ -es decir, los que aparecen como “label” en la caja de herramientas- el nombre sería algo como “label”, “label_2”, “label_3”, etc.).

> En este punto vale mencionar algo que se llama “notación húngara” y que consiste en poner como nombre el tipo de objeto de que se trate, seguido de una palabra que lo identifique. Por ejemplo, el botón que inicia el juego y cuyo texto indica “Jugar!” podría llamarse “btnJugar”. Muchos defenestran este tipo de práctica por considerarla engorrosa y redundante ya que los IDEs modernos indican toda la información necesaria (¿obviando considerar que no siempre el código se leerá dentro de un IDE, tal vez?). Por otra parte, en los días del “auto-completado” uno podría recordar que había un botón en alguna parte pero sin saber su nombre exacto... ¡ah! pero sabe que el nombre comenzaba con “btn”, lo cual basta y sobra para que nuestro maravilloso IDE nos muestre todos los objetos que hemos creado y que comienzan con ese nombre. Por otra parte, y especialmente con las variables que no son parte de la interfaz gráfica, ante cualquier cambio de tipo de la variable habría que también cambiar el nombre y esto sería muy poco conveniente. En fin, queda a gusto del consumidor, pero seguir buenas prácticas de programación siempre es importante.

A los _radio buttons_ de selección de nivel los nombré “nivelFacil”, “nivelMedio” y “nivelDificil” y al botón le puse el _ObjectName_ “comenzar”. A la ventana principal le dejé el _ObjectName_ por defecto, “MainWindow”.

Si abrimos el archivo .ui en modo edición podremos ver que cada propiedad tiene su correspondiente en etiquetas _XML_, y esto va modificándose a medida que cambiamos los valores en el panel de propiedades:

![propiedades en el código]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img10.png)

Estos archivos XML serán luego convertidos a encabezados C++ durante la compilación.

Ahora habrá que agregar una nueva ventana para el juego en sí, que se abrirá al elegir el nivel y presionar el botón “Jugar”. Para esto, hacer click derecho sobre el nombre del proyecto y seleccionar “Add New”:

![nueva ventana]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img11.png)

Luego, en **Qt > Qt Designer Form Class > Widget**. Yo le puse el nombre “Juego” a esta ventana y dejé todo lo demás por defecto. Automáticamente se crearán 3 archivos: <code>juego.h</code>, <code>juego.cpp</code> y <code>juego.ui</code>. Este último es el responsable de la interfaz gráfica.

Usaremos una serie de imágenes que corresponde a cada oportunidad de adivinar la palabra, es decir, al “ahorcado” a medida que se va armando. Están disponibles para ser descargadas en [este archivo zip (click para descargar)](/assets/2018-02-08-juego-ahorcado-gui-archivoimgs.zip). La particularidad es que tienen todas la misma dimensión, con lo cual será fácil reemplazar cada una con una nueva cuando el usuario pierda una oportunidad de adivinar.

Una forma sencilla de agregar imágenes es usando la propiedad pixmap de los elementos de tipo label. Para agregar la primera imagen (la horca vacía), colocar un _label_ en la ventana de juego y darle el objectName “horca”. Luego por código se podrá editar esta propiedad mediante el [método](/poo/2016/01/07/programacion-orientada-a-objetos.html) `setPixmap()`. Pero también necesitamos tener las imágenes en una colección de “recursos”, de manera que podamos seleccionarlas desde ahí para insertarlas en el label. Los recursos se compilan dentro del ejecutable y pueden accederse en tiempo de ejecución.

Para crear una colección de recursos hacer click derecho sobre el **nombre del proyecto (en modo edición) > New > seleccionar, dentro de la categoría Qt, la opción “Qt Resource File”**; darle el nombre “recursos” y dejar lo demás por defecto. En el proyecto se agregará una carpeta llamada “Resources” con el archivo `recursos.qrc` (que no es más que un archivo XML). Hacer click sobre este archivo y luego Add > Add prefix (que agrega una ruta para los recursos). Colocar “/imagenes” en el campo “Prefix”.

![colección de recursos]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img12.png)

Una vez hecho esto, se pueden agregar archivos desde **Add > Add Files**, y así seleccionaremos cada una de las imágenes del ahorcado.

Ahora sí, clickeando sobre el label colocado previamente, llamado “horca”, es posible acceder a la propiedad _pixmap_ y ver los recursos. Si esto no fuera así, será necesario reiniciar Qt Creator.

![ver recursos]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img13.png)

Seleccionar como imagen inicial la de la horca vacía, ya que así comienza el juego. Luego, mediante el código, se cambiará esta imagen por la correspondiente a medida que el juego avance. Para que se pueda ver la imagen será necesario agrandar este label (arrastrando y soltando desde las agarraderas de las esquinas o bien mediante la propiedad _geometry_).

Además, agregar un _Combo Box_ (dentro de “Input Widgets”) con el _ObjectName_ “alfabeto” para mostrar las letras del alfabeto, más un _Push Button_ con el texto “Adivinar” para jugar y el _ObjectName_ “adivinar”. Más adelante se les dará funcionalidad.

El aspecto de la ventana será aproximadamente este:

![ventana de juego]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img14.png)

## Desarrollo: funcionalidad

> La lógica del programa estará dada en los archivos .cpp. Pero las declaraciones de las clases y métodos estarán en los archivos .h. Por esto, para implementar un método en un archivo .ccp primero deberá estar declarado en el archivo .h. Por cada archivo .cpp que creemos, el framework automáticamente agregará el #include de su contraparte .h.

Volviendo a _MainWindow_ (la ventana principal del juego), seleccionar el radio button de nivel medio y buscar entre sus propiedades la llamada _checked_ para activarla. Esto hará que este nivel sea el seleccionado por defecto.

![nivel seleccionado por defecto]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img15.png)

La característica principal de un radio button es que nunca hay uno solo y que son auto-excluyentes (seleccionando uno se desactiva el que estuviera seleccionado previamente, ya que sólo uno por vez puede estar activo). Este es el comportamiento por defecto, indicado por la propiedad _autoExclusive_.

A continuación daremos funcionalidad al botón “comenzar”. Para esto utilizaremos _eventos_, que no son más que acciones que disparan la ejecución de cierto código. Dentro de Qt se llama “slot” al método que ejecuta este tipo de acciones. Por esto, daremos click derecho al botón y seleccionaremos **Go to slot > clicked()**, de manera que el framework genere automáticamente la estructura de este método y lo deje listo para insertar nuestro código.

![botón comenzar]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img16.png)

Nos encontraremos con el siguiente método vacío dentro del archivo `mainwindow.cpp`:

    void MainWindow::on_comenzar_clicked()
    {
    }

Y, como habíamos dicho, la declaración de este método se agregará también de manera automática en el archivo .h:

    private slots:
        void on_comenzar_clicked();

Antes de poder darle funcionalidad a este botón (la de que, al hacer click, se abra la ventana de juego), debemos incluir el archivo de cabecera de la nueva ventana que se abrirá. Para esto, dentro del archivo `mainwindow.h` incluiremos `juego.h` y también crearemos un puntero a un objeto de la clase Juego:

![incluir archivo de cabecera]({{site.baseurl}}/assets/2018-02-08-juego-ahorcado-gui-img17.png)

Ahora, volviendo al slot on_comenzar_clicked() dentro de mainwindow.cpp, agregar el siguiente código:

    void MainWindow::on_comenzar_clicked()
    {
        juego = new Juego(this);
        juego->show();
        this->hide();
    }

Lo que hace la primera línea es instanciar un _objeto_ de tipo “Juego” y asignarlo a la _variable_ juego que se declaró previamente dentro del archivo .h, además de pasarle como parámetro a _this_, que no es más que el objeto desde el cual se está trabajando: la ventana principal. En la segunda línea, como _juego_ es un puntero (al que se le asignó un objeto de tipo “Juego” al hacer la operación _new_), se utiliza el operador **->** para invocar su método `show()` que se encarga de “dibujar” la ventana del juego en pantalla. Por último, al objeto actual (_this_ -la ventana principal) le invocamos el método `hide()` para que se oculte y deje visible sólo la ventana del juego. Con esto lograremos que, desde la primera ventana, se abra la segunda al hacer click en el botón.

Ahora entonces podremos enfocar nuestros esfuerzos en la ventana _Juego_. Haciendo doble click sobre `juego.cpp` estaremos visualizando su código.

Como vamos a utilizar variables de tipo string y tipo vector, será necesario incluir al principio del archivo la definición de sus clases y la parte del namespace correspondiente (además de #include "ui_juego.h" y #include <fstream> que ya estarán por defecto al crear el archivo):

    #include <string>
    #include <vector>
    using std::string;
    using std::vector;
