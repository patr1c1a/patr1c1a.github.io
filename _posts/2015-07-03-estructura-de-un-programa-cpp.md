---
layout: post
title: Estructura de un programa de consola en C++
date: 2015-07-03 19:00:00
categories: cpp
published: true
---

C++ es un lenguaje **compilado** que adopta los paradigmas imperativo y orientado a objetos.

Proviene de C, lo cual le brinda características de bajo nivel. Su nombre lleva el operador de incremento que se utiliza en C (++), indicando que es una "mejora" de C.

El punto de inicio de un programa en C++ es la función _main_ (que retorna un entero y no recibe parámetros), por lo que esta función es imprescindible para que compile.

Detalles de sintaxis importantes: los bloques de código se definen entre **llaves** y las instrucciones finalizan con **punto y coma**. Los strings se indican con **doble comilla**.

Como detalle semántico, las variables deben declararse (indicando su tipo de datos) antes de utilizarse. También debe indicarse el tipo de valor de retorno de las funciones y el tipo de los parámetros que reciben (ya que C++ no es un lenguaje dinámico, como Python).

Para poder utilizar funcionalidad de entrada/salida de datos, se importa la biblioteca _iostream_ colocando al principio <code>#include \<iostream\></code>. Esto no es obligatorio, pero normalmente será necesario en la mayoría de los programas.

De la misma forma, para utilizar strings se recomienda importar la biblioteca correspondiente, mediante <code>#include \<string\></code>


_Ejemplo 1:_ "Hello World" en C++

<pre><code>#include <iostream>
int main()
{
   std::cout << "Hello, world!\n";
   return 0
}</code></pre>

En este ejemplo, la función _main_ retorna el valor 0 (aunque esto no es imprescindible para que el programa compile). Normalmente se utiliza el número 0 para indicar que no hubo error. Es decir, esta función retornará 0 si llega a ejecutarse hasta el final sin ningún error.


_Ejemplo 2:_ para evitar tener que agregar _std::_ cada vez antes de _cin_, _cout_ y otras instrucciones, podemos definir el espacio de nombres _std_ (abreviatura de "standard").

<pre><code>#include <iostream>
using namespace std;

int main() 
{
    cout << "Hello, world!\n";
    return 0; 
}</code></pre>

La directiva "using" indica que se use ese espacio de nombres cada vez que sea necesario.

Un espacio de nombres es un ámbito dentro del cual los identificadores de variables, funciones, clases, etc. son únicos. Es decir, podrían existir dos espacios de nombres diferentes, cada uno con una función llamada _miFuncion()_ y con contenidos diferentes. Al no compartir el espacio de nombres, cada función puede llamarse por separado, anteponiendo el espacio de nombres:

_Ejemplo 3:_

<pre><code>namespace unEspacio
{
  void miFuncion()
  {
    // cuerpo de la función unEspacio::miFuncion()
  }
}

namespace otroEspacio
{
  void miFuncion()
  {
    // cuerpo de la función otroEspacio::miFuncion()
  }
}</code></pre>


La forma de leer datos e imprimir datos en la pantalla es utilizando las instrucciones _cin_ y _cout_ respectivamente. Éstas trabajan mediante un concepto llamado "stream de datos", que no es más que un buffer (un espacio compartido de la memoria) donde se colocan los datos en el orden en que llegan y luego se toman uno a uno, también en orden.

Tanto _cin_ como _cout_ utilizan las entradas y salidas de datos estándar. También hay otros streams aparte del estándar, que se usan para propósitos específicos (por ejemplo, _cerr_ es para errores y _clog_ es para registro de _logs_).

## cout

_Ejemplo 4:_ La instrucción cout se utiliza seguida del operador de inserción **<<** que inserta en el stream estándar lo que sigue a continuación de ese operador.

<pre><code>cout << "esto se imprime en la pantalla";   // imprime el string literal en la pantalla
cout << 45;                                 // imprime el entero literal en la pantalla
cout << x;                                  // imprime el valor de x en la pantalla</code></pre>

_Ejemplo 5:_ También se pueden encadenar datos para enviarse a la salida estándar e imprimirlos en pantalla, unos a continuación de otros, sin espacios.

<pre><code>cout << "El valor de la variable x es: " << x << "y esto es un ejemplo";</code></pre>

_Ejemplo 6: cout_ no agrega automáticamente un salto de línea luego de imprimir (el cursor queda en la misma línea) y es necesario indicar expresamente que se comience una nueva línea, con _\n_.

<pre><code>cout << "Esta oración...";
cout << "...y esta otra se imprimen en una sola línea." << \n; 
cout << "Esta cadena empieza en una nueva línea";</code></pre>

_Ejemplo 7:_ De forma similar a \n puede utilizarse _endl_, que también crea una nueva línea pero, además, elimina los contenidos del stream.

<pre><code>cout << "Algo para imprimir." << endl;</code></pre>

## cin

_cin_ lee de la entrada de datos estándar y coloca lo leído en el stream estándar. Normalmente, la entrada estándar por defecto es el teclado (aunque esto puede configurarse) y _cin_ hace que se espere una entrada mediante el teclado, seguida de la tecla Enter.

_Ejemplo 8: cin_ se usa con el operador de extracción **`>>`** seguido por una variable donde se guardan los datos extraídos.

<pre><code>int edad;
cin >> edad;</code></pre>

Nótese que la variable edad se declaró (como de tipo entero -**int**-) antes de utilizarse. cin utiliza este tipo de la variable que encuentra luego del operador de extracción para saber cómo debe interpretar los datos leídos. El inconveniente que esto tiene es que, si los datos ingresados no son del tipo esperado (por ejemplo, la variable es de tipo _int_ pero el usuario ingresa letras), la extracción de los datos falla pero el programa continúa, lo cual produce resultados inesperados al intentar leer la variable posteriormente.

_Ejemplo 9:_

<pre><code>#include <iostream>
using namespace std;
     
int main()
{
    	int i;
    	cin >> i;
    	cout << "El valor ingresado es: " << i;
    	return 0;
}</code></pre>

En cuanto a los strings, _cin_ considera que los espacios en los strings cortan la entrada de datos, entonces, si la variable es de tipo string y el usuario ingresa espacios, sólo quedará la primera palabra. Para poder ingresar un string que contenga espacios, se utiliza la función _getline_, que recibe como primer parámetro a _cin_ y como segundo parámetro a la variable donde almacenar el string:

_Ejemplo 10:_

<pre><code>#include <iostream>
#include <string>
using namespace std;

int main ()
{
  string nombre;
  cout << "Ingresa tu nombre: ";
  getline (cin, nombre);
  cout << "Hola " << nombre << ".\n";
  return 0;
}</code></pre>

## Estructuras de control

Si lo que queremos es escribir una estructura de control como _if_, _for_ o _while_, tendremos que incluir la condición entre paréntesis:

_Ejemplo 11:_

<pre><code>int edad;
cout << "Ingresar edad de la persona: ";
cin >> edad;
if (edad >= 18)
    cout << "\nLa persona es mayor de edad: ";
else
    cout << "\nLa persona es menor de edad: ";</code></pre>
