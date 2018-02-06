---
layout: post
title: Tipos subrango y enumerado en Pascal
date: 2011-06-01 19:00:00
categories: pascal
published: true
---

Estos son tipos definidos por el usuario, por lo que se debe crear primero el tipo, utilizando la palabra reservada _type_.

Tanto el subintervalo como el enumerado son tipos de datos ordinales. Es decir, los valores que adopten las variables de alguno de estos tipos tendrán un predecesor y un sucesor, que pueden obtenerse con las funciones _pred(valor)_ y _succ(valor)_.

## Subintervalo

Este tipo de dato es simple (ya que cada variable sólo contendrá un valor) pero definido por el usuario. Lo que el usuario define, en este caso, es el rango de valores que una variable puede adoptar.

Sólo puede establecerse un subrango de datos ordinales, donde se determina el menor valor del rango y el mayor. Siempre se debe recordar que al primer valor del rango no puede aplicársele la función _pred(valor)_, ya que esto daría un error. Lo mismo sucede con el último valor del rango y la función _succ(valor)_.

Por ejemplo, si se necesitara una variable que almacene dígitos entre el 0 y el 9, se podría definir un tipo subrango, al que hemos llamado _digito_, de la siguiente forma:
<pre><code>type digito = 0 .. 9;</code></pre>

Los subrangos brindan su utilidad en la creación de datos de tipo array, para la manipulación de índices.


## Enumerado

En este caso el programador especifica, uno a uno, los valores que puede adoptar el dato. Este tipo se convertirá en un tipo de dato ordinal, siendo el orden en que sean definidos los valores lo que determinará su posición. El primer valor asignado recibirá el número de orden 0, el siguiente el 1, luego el 2, etc. La sintaxis requiere que los valores sean encerrados entre paréntesis y separados por coma. Por ejemplo, para crear un tipo de dato llamado _presidente_ que permita almacenar como valores los nombres de los primeros cinco presidentes de Argentina, se utiliza la siguiente sintaxis:

<pre><code>type presidente = (Rivadavia, Urquiza, Derqui, Mitre, Sarmiento);</code></pre>

Así, una variable de tipo _presidente_ puede adoptar uno de los cinco valores definidos. En el ejemplo, _Rivadavia_ adopta la posición 0, Urquiza la posición 1, Derqui la 2, Mitre la 3 y Sarmiento la 4.

Para asignar un valor a una variable de este tipo, puede utilizarse la asignación directa o la asignación mediante el número de orden. Un ejemplo de lo primero (utilizando una variable llamada _procer_, de tipo _presidente_) sería el siguiente: 
<pre><code>procer:=Derqui;</code></pre>

Sabiendo que cada valor posible de un dato de un tipo enumerado tiene una correspondencia numérica con su posición, otra opción es asignar a la variable el valor correspondiente a su número de orden. Esto es:
<pre><code>procer:=presidente(2);</code></pre>
Esto asigna el valor 'Derqui' a la variable _procer_ (ya que ese es el valor correspondiente a la posición 2). Debe tenerse en cuenta que los datos contenidos en una variable de tipo enumerado no pueden leerse ni escribirse directamente. Es decir, dada la variable llamada _procer_ de tipo _presidente_, la siguiente sintaxis es inválida:
<pre><code>writeln(procer)</code></pre>
Para poder leer el contenido de una variable de tipo enumerado se deberá utilizar otra forma. Por ejemplo, se puede utilizar una estructura de selección _case_:

<pre><code>case procer of
    Rivadavia: writeln('Rivadavia');
    Urquiza: writeln('Urquiza');
    Derqui: writeln('Derqui');
    Mitre: writeln('Mitre');
    Sarmiento: writeln('Sarmiento');
end;</code></pre>

Para conocer el número de orden que corresponde a un determinado valor es posible utilizar la función _ord_, que devuelve un número entero, de la siguiente forma:
<pre><code>posicion:=ord(Mitre);</code></pre>

Suponiendo que la variable _posicion_ es de tipo integer, se asigna a la misma el número 3, correspondiente al valor "Mitre" del tipo enumerado definido anteriormente.

También pueden obtenerse los valores anterior y siguiente a un valor enumerado determinado. Esto se logra con las funciones _pred_ y _succ_:

<pre><code>anterior:=pred(procer);
siguiente:=succ(procer);</code></pre>

En este caso, las variables _anterior_ y _siguiente_ son del tipo _presidente_ definido con anterioridad y, suponiendo que _procer_ contiene el valor "Urquiza", correspondiente a la posición 1, los valores que se almacenarán en ellas serán: _Rivadavia_ (posición 0) en _anterior_ y _Derqui_ (posición 2) en _siguiente_. Algo importante a considerar es que el valor en la posición 0 no tiene antecesor y el valor en la última posición no tiene sucesor.


Incluso, podría crearse un subrango de un tipo enumerado. Por ejemplo:

<pre><code>type  
   dias = (lunes,martes,miercoles,jueves,viernes,sabado,domingo);  
   laborables = lunes .. viernes;  
   finDeSemana = sabado .. domingo;</code></pre>

