---
layout: post
title: POO - Constructores y miembros estáticos
date: 2016-01-10 19:00:00
categories: poo
tags: objetos
published: true
---


## Constructores

El concepto de "constructor" refiere a un método especial de las clases para "construir" objetos a partir de ella. Asimilando el concepto de clase al de un "molde" del cual se obtienen objetos concretos, entonces el constructor sería quien "utiliza" ese molde para crearlos.

El constructor puede recibir parámetros o no, y en algunos lenguajes (como Java o C#) su valor de retorno será un objeto de la clase a la que hace referencia, mientras que en otros no retorna nada sino que implícitamente crea el objeto.

Al crear un objeto, es necesario asignarlo a alguna expresión o variable, para que pueda utilizarse quedar guardado (de otra forma, el objeto quedaría inaccesible en la memoria).

Cuando se desea obtener a un nuevo objeto ("instanciar" un objeto) de una clase en particular, el método que se ejecuta es el de este constructor. Usualmente los lenguajes tienen alguna sintaxis especial para invocarlo. Por ejemplo, en Java se utiliza la palabra clave <code>new</code> seguida del nombre del constructor y sus parámetros. En Python no se utiliza palabra clave sino directamente el nombre del constructor y los parámetros.

_Ejemplo de invocación a un constructor:_

En Java:

<pre><code>Estudiante laura = new Estudiante();</code></pre>

En Python:

<pre><code>laura = Estudiante()</code></pre>

El constructor de una clase tiene la particularidad de que lleva como nombre el mismo de la clase. Puede recibir parámetros o no y dentro de su cuerpo puede inicializar atributos, ejecutar otros métodos y realizar cualquier tarea que un método pueda realizar.

En Java, como los constructores están definidos en la clase Object de la cual todas las demás clases derivan, el contenido del constructor debe tener la llamada al método <code>super()</code> para ejecutar los contenidos del constructor de la clase Object, que se encargará de agregar el código necesario para crear objetos con la llamada a <code>new</code>. El método <code>super()</code> simplemente invoca el constructor de la superclase (por ejemplo, si la clase A es superclase de B, entonces al invocar <code>super()</code> en B, se está automáticamente invocando a <code>super()</code> de A). Esto es así porque, para crear un objeto, primero se debe crear el objeto padre.

## Miembros estáticos ("static")

Muchos lenguajes permiten tener atributos o métodos de una clase como estáticos. Esto evita que un objeto deba instanciarse para poder utilizar el miembro estático de que se trate.

En C, C++ y Java, por ejemplo, se utiliza el modificador <code>static</code> delante de la declaración. En Python se usa el "decorador" [@staticmethod](https://docs.python.org/3/library/functions.html#staticmethod) para un método estático.

### Atributos "static":

Una variable estática es una cuya vida se extiende a lo largo de toda la ejecución del programa (es decir, siempre tiene alocado su lugar en memoria).

Cuando un grupo de objetos son instanciados a partir de una clase, cada uno de ellos tiene su propia "copia" de sus atributos (o "variables de instancia"). En el caso de los atributos estáticos, sólo existirá una única "copia" de este atributo, compartida por todos los objetos de esa misma clase. El atributo se asocia a la clase y no a los objetos que se instancian a partir de ella (por eso, a estos atributos suele llamárseles "atributos de clase").
  
Los atributos estáticos suelen referenciarse usando el nombre de la clase, por ejemplo: <code>Clase.atributo</code> (donde "Clase" es el nombre de la clase y "atributo" es el nombre del atributo).

### Métodos "static":

Al igual que como sucede con los atributos estáticos, los métodos estáticos pertenecen a la clase y no necesitan una instancia (es decir, un objeto) de la clase para poder ser utilizados. la invocación suele hacerse llamando a <code>Clase.metodo()</code> para ejecutarlos.

Un ejemplo muy usual de método estático es el método <code>main</code> de algunos lenguajes. Se trata del método principal por el cual comienza la ejecución de un programa. Este método debe aparecer dentro de cualquiera de las clases del programa. Y, justamente, no importa en cuál clase se encuentre porque, al ser un método estático, no necesita instanciarse a la clase que lo contiene para poder ejecutarlo.
