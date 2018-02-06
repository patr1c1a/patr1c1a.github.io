---
layout: post
title: Codificar, compilar y depurar C++
date: 2015-07-04 19:00:00
categories: cpp
published: true
---

## Compilador

La [ISO](https://en.wikipedia.org/wiki/International_Organization_for_Standardization) es la encargada de estandarizar C++. Por ejemplo, en 2014 se lanzó [C++14](https://en.wikipedia.org/wiki/C%2B%2B14).

C++ es un lenguaje compilado y los archivos de código se almacenan con la extensión .cpp para poder compilarlos.

### Compilación en Linux

[GCC](https://gcc.gnu.org/) es un clásico compilador para C y otros lenguajes, con una versión para C++ llamada g++ (que automáticamente utiliza las bibliotecas específicas de C++).

En entornos Linux puede compilarse un archivo de extensión .cpp desde la terminal. Para esto es necesario contar con el compilador de C++, el cual puede instalarse mediante la instrucción <code>sudo apt-get install g++</code>. Luego, posicionándose en el directorio donde el archivo se encuentra, puede compilarse escribiendo la instrucción <code>g++ archivo.cpp</code> (donde "archivo.cpp" es el nombre del archivo a compilar). Esto generará un archivo objeto (código de máquina) llamado "archivo.o". Para unir varios archivos objeto en un único ejecutable (lo llamaremos "programa" para el ejemplo), utilizar:

<code>g++ -o programa archivo1.o archivo2.o archivo3.o</code>
  
(la cantidad de archivos .cpp es variable y puede haber uno o más).

O, para ahorrarse estos pasos y hacer todo en uno:

<code>g++ -o programa archivo1.cpp archivo2.cpp archivo3.cpp</code>

Opcionalmente, también pueden agregarse "flags" que determinan ciertas opciones de compilación. Por ejemplo, para compilar para C++11 el flag utilizado es <code>-std=c++11</code>; y para C++14 se debe utilizar <code>-std=c++1y</code> si el compilador g++ es previo a la versión 5.2 A partir de g++ 5.2 se soporta el flag <code>-std=c++14</code> para C++14.``

<pre><code>g++ -std=c++11 -o programa archivo.cpp</code></pre>


### Compilación en Windows

En Windows, el compilador de C++ más utilizado es [MinGW GCC](http://www.mingw.org/), aunque también se puede utilizar [Cygwin GCC](http://www.cygwin.com/).

Para descargar MinGW se debe visitar [www.mingw.org](http://www.mingw.org/) y luego desde allí ir a _"Downloads" > "Installer" > click en el archivo .exe_

Al ejecutar el instalador se ofrecen varias opciones. Marcar _mingw32-base_, _mingw32-gcc-g++_ y _msys-base._

![instalador MinGW]({{ site.url }}/assets/2015-07-04-codificar-compilar-depurar-cpp-img1.jpg)

Cerrar el programa (en la X superior) y seleccionar _"Review changes" > "Apply"_. Luego, en las variables de entorno del sistema, agregar en path: _C:\MinGW\bin;C:\MinGW\msys\1.0\bin;_

Cygwin es un poco más complejo (y completo) que MinGW. Se descarga yendo a [www.cygwin.com](http://www.cygwin.com/) > _"Install cygwin" > descargar el .exe correspondiente (32 o 64 bits)_.


## IDEs (entornos integrados de desarrollo)

Normalmente no alcanzará con sólo un compilador y querremos algunas facilidades más (código coloreado, sugerencias de funciones, acceso rápido a la implementación, refactorización, depurador, etc.), entonces necesitaremos algún IDE ("integrated development environment" - "entorno integrado de desarrollo").


### Qt Creator (multiplataforma)**

Este IDE se descarga desde [www.qt.io/download-open-source](https://www.qt.io/download-open-source/) (detecta automáticamente el sistema operativo).

Para crear un nuevo proyecto de consola en C++ se debe ir a _"File" > "New File or Project"_ y allí elegir la opción _"Non-Qt Project" > "Plain C++ Project"_ y luego click en "Choose". La opción "Non-Qt Project" incluye los proyectos que no utilizan la librería de Qt.

![QT Creator pantalla de creación de proyecto]({{ site.url }}/assets/2015-07-04-codificar-compilar-depurar-cpp-img2.png)

En la siguiente ventana colocar el nombre del proyecto de desarrollo y la ubicación donde se guardará, y presionar el botón "Next".

![QT Creator pantalla de nombre de proyecto]({{ site.url }}/assets/2015-07-04-codificar-compilar-depurar-cpp-img3.png)

A continuación permite elegir los kits a utilizar: debug/release. Debug contiene información adicional necesaria para depurar la aplicación durante el desarrollo pero que puede eliminarse al momento de obtener la versión final. Normalmente se utiliza la configuración "debug" para probar el programa durante el desarrollo y la configuración "Release" para crear el archivo final del programa.

![QT Creator pantalla de selección de kit de desarrollo]({{ site.url }}/assets/2015-07-04-codificar-compilar-depurar-cpp-img4.png)

En el siguiente paso se puede seleccionar un sistema de control de versiones (utilizados usualmente al programar en equipos de desarrollo). Si no se utiliza ninguno, dejar seleccionado "None" y presionar "Finish".

![QT Creator pantalla de control de versiones]({{ site.url }}/assets/2015-07-04-codificar-compilar-depurar-cpp-img5.png)

Para ejecutar el código presionar el botón "Run" o Ctrl+R.

![QT Creator vista del proyecto creado]({{ site.url }}/assets/2015-07-04-codificar-compilar-depurar-cpp-img6.png)

Como se dijo anteriormente (sección "compilación en linux") se pueden indicar "flags" para compilar. Esto se hace en el archivo .pro que se crea con el proyecto. Por ejemplo, para compilar en C++11 se debería agregar <code>QMAKE_CXXFLAGS += -std=c++11</code>

![archivo .pro]({{ site.url }}/assets/2015-07-04-codificar-compilar-depurar-cpp-img7.png)

### Visual Studio (sólo Windows)**

Este IDE, aparte de soportar los lenguajes de Microsoft como Visual Basic y C#, ofrece la posibilidad de compilar código C++. Puede descargarse una versión gratuita desde [www.visualstudio.com/es-es/products/visual-studio-express-vs.aspx](https://www.visualstudio.com/es-es/products/visual-studio-express-vs.aspx).

Para crear una aplicación de consola, se debe crear un nuevo proyecto desde _"File" > "New Project"_ y allí elegir la opción "_Win32 Console Application_", dándole el nombre deseado en la parte inferior de la ventana (y eligiendo en qué carpeta se desea guardar). Luego, click en Ok.

![Visual Studio pantalla de creación de proyecto]({{ site.url }}/assets/2015-07-04-codificar-compilar-depurar-cpp-img8.png)

El nuevo proyecto crea automáticamente los archivos necesarios y deja preparada la función _main_ para escribir el código.

Para ejecutar el programa, presionar _Ctrl+F5_ ó ir a "_Debug" > "Start without debugging"_ ó click en el botón de contorno de flecha en la barra de menú.

![Visual Studio ejecución del programa]({{ site.url }}/assets/2015-07-04-codificar-compilar-depurar-cpp-img9.png)

Para utilizar el depurador _("debugger"),_ marcar un punto de corte ("_breakpoint_") y ejecutar presionando F5 ó yendo a "_Debug" > "Start debugging"_ ó click en el botón "_Local Windows Debugger_" en la barra de menú.

![Visual Studio depurador]({{ site.url }}/assets/2015-07-04-codificar-compilar-depurar-cpp-img10.png)

### Eclipse (multiplataforma)

Luego de instalar el compilador de C++, si no se tiene Eclipse instalado, ir a [www.eclipse.org/downloads](http://www.eclipse.org/downloads/) para descargar la opción "_Eclipse IDE for C/C++ Developers_" y luego descomprimir el archivo en cualquier carpeta (el programa es portable). En caso de ya tener instalada la versión de Eclipse para Java, instalar el plugin CDT desde el menú _Help > Install New Software > en "Work with"_ desplegar el menú y elegir la versión de Eclipse instalada (por ejemplo, "Kepler - http://download.eclipse.org/releases/kepler"). En "_Name_", expandir _"Programming Language" > Marcar "C/C++ Development Tools" > "Next" > aceptar términos y condiciones > "Finish"_.

Para crear un proyecto de C++ en Eclipse, ir a "_File" > "New" > "Project" > "C/C++" > "C++ project"_. Colocar el nombre del programa y la carpeta donde se lo quiere guardar.

![Eclipse pantalla de creación de proyecto]({{ site.url }}/assets/2015-07-04-codificar-compilar-depurar-cpp-img11.png)

Elegir la opción "_Empty Project_" para comenzar desde cero (sólo con las bibliotecas necesarias) o "_Hello World C++ Project_" para que automáticamente se cree un archivo .cpp con la función main. Luego, presionar "_Finish_".

![Eclipse pantalla de proyecto]({{ site.url }}/assets/2015-07-04-codificar-compilar-depurar-cpp-img12.png)

Para ejecutar, presionar el botón circular verde con una flecha blanca ("Run").

Si, al ejecutar, aparecen errores del tipo "<span class="color-new">Unresolved Inclusion Error</span>", hacer click derecho sobre el proyecto, ir a _"Properties" >Â "C/C++ General" > "Paths and Symbols" > En "Includes":_

Para MinGW GCC:

  1. Click en "Add" y agregar los siguientes directorios en "GNU C", donde `$MINGW_HOME` es el directorio base de MinGW: 
      * `$MINGW_HOME\lib\gcc\mingw32\4.x.x\include`
      * `$MINGW_HOME\include`
      * `$MINGW_HOME\lib\gcc\mingw32\4.x.x\include-fixed`
  2. Click en "Add" y agregar los siguientes directorios en "GNU C++", donde `$MINGW_HOME` es el directorio base de MinGW: 
      * `$MINGW_HOME\lib\gcc\mingw32\4.x.x\include\c++`
      * `$MINGW_HOME\lib\gcc\mingw32\4.x.x\include\c++\mingw32`
      * `$MINGW_HOME\lib\gcc\mingw32\4.x.x\include\c++\backward`
      * `$MINGW_HOME\lib\gcc\mingw32\4.x.x\include`
      * `$MINGW_HOME\include`
      * `$MINGW_HOME\lib\gcc\mingw32\4.x.x\include-fixed`

Para Cygwin GCC:

  1. Click en "Add" y agregar los siguientes directorios en "GNU C", donde `$CYGWIN_HOME` es el directorio base de Cygwin: 
      * `$CYGWIN_HOME\lib\gcc\i686-pc-cygwin\4.x.x\include`
      * `$CYGWIN_HOME\lib\gcc\i686-pc-cygwin\4.x.x\include-fixed`
      * `$CYGWIN_HOME\usr\include`
      * `$CYGWIN_HOME\usr\include\w32api`
  2. Click en "Add" y agregar los siguientes directorios en "GNU C++", donde `$CYGWIN_HOME` es el directorio base de Cygwin: 
      * `$CYGWIN_HOME\lib\gcc\i686-pc-cygwin\4.x.x\include\c++`
      * `$CYGWIN_HOME\lib\gcc\i686-pc-cygwin\4.x.x\include\c++\i686-pc-cygwin`
      * `$CYGWIN_HOME\lib\gcc\i686-pc-cygwin\4.x.x\include\c++\backward`
      * `$CYGWIN_HOME\lib\gcc\i686-pc-cygwin\4.x.x\include`
      * `$CYGWIN_HOME\lib\gcc\i686-pc-cygwin\4.x.x\include-fixed`
      * `$CYGWIN_HOME\usr\include`
      * `$CYGWIN_HOME\usr\include\w32api`

	  

## Depurar código ("debug")

La depuración permite analizar el código de un programa cuando, en la ejecución, se observan resultados diferentes a los esperados. La idea es detectar errores para poder solucionarlos.


### Impresión por pantalla

Cuando no se cuenta con una herramienta de depuración es posible utilizar la impresión de valores por pantalla, colocando instrucciones de impresión en las partes del código que se desee analizar. Esto permite explorar la secuencia de ejecución y los valores en determinado puntos de la ejecución.

Para utilizar este método de depuración, simplemente se colocarán salidas por pantalla de alguna expresión que se desee analizar. Es importante imprimir, además del valor, alguna indicación que ayude a saber a qué corresponde. Ejemplo:

<pre><code>cout << "Valor de la variable x: " << x << endl</code></pre>

Esto también es útil para saber si alguna parte del código se está ejecutando o no, y si los valores de las variables están siendo asignados, especialmente cuando una misma variable recibe varios valores a lo largo de una porción de código. Por esto, a medida que el código se complejiza, también puede ser conveniente agregar, a la instrucción de salida por pantalla, algo que indique por dónde pasa la ejecución en ese momento. Ejemplo:

<pre><code>cout << "Valor de x al iniciar funcion1: " << x << endl</code></pre>
