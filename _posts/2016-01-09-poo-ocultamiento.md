---
layout: post
title: POO - Ocultamiento de los datos
date: 2016-01-09 19:00:00
categories: poo
tags: objetos
published: true
---

![ocultamiento]({{ site.url }}/assets/2016-01-09-poo-ocultamiento-img1.jpg)

## Modificadores de visibilidad

Las clases, los atributos y los métodos pueden tener diferentes criterios de "visibilidad": de acuerdo al modificador de acceso (o visibilidad) que posean podrán "ser vistos" desde determinados lugares. Por ejemplo, podría existir un método que sólo vaya a ser usado dentro de la misma clase que lo contiene y nunca desde otras clases, entonces puede calificarse a este método como "privado", de forma que no exista la posibilidad de que sea invocado desde afuera. Existen también otros modificadores para indicar distintos grados de visibilidad, y suelen ser muy similares en todos los lenguajes orientados a objetos. Por ejemplo, en Java existen los siguientes grados crecientes de visibilidad: private (sólo para la clase actual), protected (para todas las subclases), sin modificador (para todas las clases del mismo paquete), public (para todo el programa).

![modificadores en java]({{ site.url }}/assets/2016-01-09-poo-ocultamiento-img2.png)


## Getters y setters

Uno de los principios que conducen a un buen modelo orientado a objetos es el ocultamiento de los datos. Esto significa que no se debería necesitar conocer la implementación de un objeto para poder utilizarlo (este buen ocultamiento conduce a mayor independencia de los objetos, con lo cual se reduce el acoplamiento).

_Ejemplo:_

Si un objeto Persona tiene un atributo llamado "edad" de tipo entero, ese atributo podría ser accesible desde afuera si se lo indicara como público (en su modificador de visibilidad). Si esto fuera así, podría instanciarse un objeto persona, por ejemplo con una variable llamada "juan", en la que se asigne el valor 25 a su atributo edad, de esta manera: <code>juan.edad=25</code>. Pero esto conduce a problemas de diseño, ya que se está revelando que existe un atributo llamado "edad". Si, en el futuro se necesitara cambiar el nombre de este atributo (por motivos de diseño del sistema, cambios en los requerimientos, etc.), cualquier otra parte del código donde se accede a este atributo (ya sea para asignarle un valor o para leer el valor) debería modificarse también.

Para evitar estas situaciones, hay dos métodos que se utilizan para preservar el ocultamiento de los datos: los llamados "getters" y "setters". Son métodos que se utilizan para obtener (en inglés, "get") o dar (en inglés, "set") el valor de un atributo.

Los métodos <code>get</code> y <code>set</code> de un objeto son los únicos que "tienen permitido" acceder directamente a los atributos. Esto es sólo por convención y buenas prácticas de programación (ver "Ocultamiento" en "[Pautas para un correcto diseño orientado a objetos](/poo/2016/01/09/correcto-diseno-oo.html)"). Los IDEs suelen tener funcionalidad que inserta el código de los métodos getters y setters automáticamente.

Se verá que los atributos utilizados desde otros objetos no deberían ser accedidos de forma directa: es decir, si un objeto de tipo "Ventana" tiene un atributo llamado "ancho" de tipo int y un atributo llamado "color" de tipo String, entonces deberá crearse un getter y un setter por cada uno de ellos.

Una crítica que suele hacerse es que estos métodos revelan el tipo de dato utilizado para implementar el atributo, y de alguna manera violan el ocultamiento. Pero son útiles cuando deben realizarse operaciones especiales con los atributos, que podrían variar y no deben conocerse desde otros objetos.

Una aclaración que cabe en este lugar es que determinados atributos, que sólo necesitan ser accedidos dentro de la propia clase y nunca desde objetos externos, deberían contar con métodos getters y setters privados.

Por convención se coloca la palabra "get" o "set" seguida de el nombre del atributo: <code>getColor</code>, <code>setColor</code>. Hay una pequeña excepción cuando se utilizan atributos de tipo boolean: en este caso, el método para acceder a ellos no comienza con la palabra "get" ("obtener") sino con la palabra "is" ("es") o "has" ("tiene"). Por ejemplo, si un atributo se llamara "abierto" para simbolizar un circuito que puede estar abierto o cerrado, el método que obtiene el valor de ese atributo se llamará <code>isAbierto</code> ("está abierto").

En los getters y setters debe respetarse también el tipo del atributo. Es decir, el get devolverá un dato del tipo del atributo al que accede, y el set recibirá un parámetro del tipo del atributo.

_Ejemplo:_

Según lo dicho, un mal uso de los atributos se daría si se accedieran de manera directa desde objetos externos. Suponiendo que se ha instanciado un objeto de tipo "Ventana" con el nombre "v1", y se deseara dar el valor "blue" al atributo "color", sería incorrecto hacerlo de la siguiente manera: v1.color="blue" ya que se viola el encapsulamiento. En este caso, lo correcto sería: <code>v1.setColor("blue")</code> que, como se observa, recibe un parámetro de tipo String, ya que el atributo al que accede es de ese tipo.

El código (de forma genérica) para un getter es el siguiente:

<pre><code>public [tipo] get[Atributo] (){ 
   return [atributo]; 
}</code></pre>

Debe reemplazarse <code>[tipo]</code> por el tipo de dato del atributo al que se accede, y <code>[atributo]</code> por el nombre de éste.

Para el setter, el código genérico es:

<pre><code>public void set[Atributo] ([tipo] parametro){ 
   this.[atributo] = parametro; 
}</code></pre>
