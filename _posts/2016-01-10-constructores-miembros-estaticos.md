---
layout: post
title: POO - Constructores y miembros estáticos
date: 2016-01-10 19:00:00
categories: poo
tags: objetos
published: true
---


## Constructores

El "constructor" de una clase es un método especial para "construir" objetos. Asimilando el concepto de clase al de un "molde" del cual se obtienen objetos concretos, entonces el constructor sería quien "utiliza" ese molde para crearlos.

El constructor puede recibir parámetros o no y, en algunos lenguajes (como Java o C#) su valor de retorno será un objeto de la clase a la que hace referencia, mientras que en otros no retorna nada sino que implícitamente crea el objeto.

Si el constructor retorna un objeto, entonces es necesario asignarlo a alguna expresión o variable, para que pueda utilizarse o quedar guardado (de otra forma, el objeto quedaría inaccesible en la memoria).

En muchos lenguajes, el constructor de una clase suele llevar como nombre el mismo de la clase (aunque no es el caso de Python, cuyos constructores tienen un nombre especial: <code>__init__</code>). Puede recibir parámetros o no y, dentro del cuerpo, pueden inicializarse atributos, invocarse otros métodos o realizar cualquier tarea necesaria para inicializar el objeto. Además, muchos lenguajes permiten la sobrecarga de métodos, con lo cual podrían existir diferentes versiones del constructor de una clase, cada una con diferentes parámetros.

Usualmente, los lenguajes tienen alguna sintaxis especial para invocar al constructor. Por ejemplo, en Java se utiliza la palabra clave <code>new</code> seguida del nombre del constructor (o de la clase, ya que coinciden) y sus parámetros. En Python no se utiliza palabra clave sino directamente el nombre de la clase y los parámetros del constructor.

_Ejemplo de invocación a un constructor (asignando el objeto creado a una nueva variable):_

En Java:

<pre><code>Estudiante laura = new Estudiante();</code></pre>

En Python:

<pre><code>laura = Estudiante()</code></pre>

En varios lenguajes existe una clase de la cual heredan todas las demás clases, generalmente llamada Object. Es el caso de Java, Python o C#, aunque no de C++. Por ejemplo, para crear un objeto en Java primero se debe crear un objeto de la clase padre, subiendo así por la jerarquía de herencias hasta llegar a crear un Object. Y, tanto en Java como en Pyton, es el método <code>super()</code> el usado para llamar al constructor de la superclase. Si no lo invocamos explícitamente, será llamado de forma implícita.


## Miembros estáticos ("static")

Muchos lenguajes permiten tener atributos o métodos de una clase como estáticos. Esto evita que un objeto deba instanciarse para poder utilizar el miembro estático de que se trate.

En C, C++ y Java, por ejemplo, se utiliza el modificador <code>static</code> delante de la declaración. En Python se usa el "decorador" [@staticmethod](https://docs.python.org/3/library/functions.html#staticmethod) para un método estático.

### Atributos "static":

Una variable (o atributo) estática es una cuya vida se extiende a lo largo de toda la ejecución del programa (es decir, siempre tiene alocado su lugar en memoria), sin necesidad de que se haya instanciado un objeto.

Cuando un grupo de objetos son instanciados a partir de una clase, cada uno de ellos tiene su propia "copia" de sus atributos (o "variables de instancia"). Pero los atributos estáticos son compartidos por todos los objetos de la misma clase. El atributo se asocia a la clase y no a los objetos que se instancian a partir de ella (por eso, a estos atributos suele llamárseles "atributos de clase").
  
Los atributos estáticos suelen referenciarse usando el nombre de la clase, por ejemplo: <code>Clase.atributo</code> (donde "Clase" es el nombre de la clase y "atributo" es el nombre del atributo).

### Métodos "static":

Al igual que como sucede con los atributos estáticos, los métodos estáticos pertenecen a la clase y no necesitan una instancia (es decir, un objeto) de la clase para poder ser utilizados. la invocación suele hacerse llamando a <code>Clase.metodo()</code> para ejecutarlos.

Un ejemplo muy usual de método estático es el método <code>main</code> de algunos lenguajes (como en C++ o Java). Se trata del método principal por el cual comienza la ejecución de un programa. Este método puede aparecer dentro de cualquiera de las clases del programa. Y, justamente, no importa en cuál clase se encuentre porque, al ser un método estático, no necesita instanciarse la clase que lo contiene para poder ejecutarlo.
