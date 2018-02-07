---
layout: post
title: Conjuntos en Pascal
date: 2011-06-04 19:00:00
categories: pascal
tags: paradigma_imperativo tipos datos variables colecciones conjuntos
published: true
---
Un conjunto es un grupo de elementos sin orden preestablecido (por lo que no existirá un índice para referenciarlos). Podría simbolizarse como un recipiente que contiene elementos mezclados al azar. Además, estos elementos no pueden estar repetidos (tal como en los conjuntos matemáticos).

En pascal, los conjuntos deben cumplir con algunas condiciones: los elementos no pueden estar repetidos, deben ser todos del mismo tipo (homogéneo), el tipo de los datos dentro del conjunto debe ser ordinal, y existe un máximo de 256 elementos para los conjuntos.

La definición de un tipo conjunto se efectúa con la palabra reservada **set** indicando el tipo de los datos del conjunto, de la siguiente forma:

<pre><code>type conjunto = set of char;</code></pre>

Para realizar operaciones con conjuntos se debe tener en cuenta que los operandos deben ser todos conjuntos del mismo tipo y no es posible operar entre conjuntos y elementos (por ejemplo, restar un elemento a un conjunto). Para operar con algún elemento, se lo debe encerrar entre corchetes, formando un nuevo conjunto que sólo contenga a ese elemento.
  
Algunas operaciones que pueden realizarse con conjuntos son:

## Asignación

La asignación permite almacenar un conjunto en una variable en la memoria. Para indicar que el dato es un conjunto, los elementos se encierran entre corchetes.

<pre><code>vocales := ['a', 'e', 'i', 'o', 'u'];</code></pre>

Si fuera necesario asignar el vacío a un conjunto, la asignación sería de corchetes vacíos:

<pre><code>letras := [ ];</code></pre>


## Unión

Mediante la unión de conjuntos se crea un nuevo conjunto que contiene todos los elementos de los conjuntos unidos.

El operador de unión es el signo + entre un conjunto y otro (operandos).

<pre><code>conjunto3 := conjunto1 + conjunto2</code></pre>

Debido a que los operandos de una unión deben ser conjuntos, si se deseara, por ejemplo, agregar una letra a un conjunto de char, se debe encerrar esta letra entre corchetes (creándose así un nuevo conjunto, que sólo contiene a la letra indicada) ya que, de otra manera, los datos serían de distinto tipo (uno de tipo conjunto y el otro del tipo correspondiente a los elementos que contiene):

<pre><code>letras := letras + ['g'];</code></pre>

## Diferencia

Mediante la diferencia se obtiene un nuevo conjunto conteniendo los elementos que pertenecen al primer conjunto y no pertenecen al segundo.

El operador de diferencia es el signo – entre dos conjuntos (operandos).

<pre><code>conjunto3 := conjunto1 – conjunto2;</code></pre>

## Intersección

Mediante la intersección se obtiene un conjunto que contenga a los elementos comunes entre todos los conjuntos.

Se utiliza el operador * entre dos conjuntos (operandos)

<pre><code>conjunto3 := conjunto1 * conjunto2; </code></pre>

## Diferencia simétrica

La diferencia simétrica consiste en un conjunto con los elementos que están en alguno de los conjuntos pero no en todos (es decir, los elementos que no estén en la intersección).

Se realiza mediante el operador >< entre dos conjuntos (operandos)

<pre><code>conjunto3 := conjunto1 >< conjunto2;</code></pre>

## Comparación

Se pueden comparar dos conjuntos con el signo de igualdad ("=") o con el de desigualdad ("<>"). El resultado de esta operación devolverá un valor boolean ("verdadero" o "falso", dependiendo de si los conjuntos son o no iguales en contenido):

<pre><code>conjunto1 = conjunto2</code></pre>

## Inclusión

Es posible saber si un elemento se encuentra incluido en un conjunto mediante la palabra reservada **in**. Esto arrojará un valor boolean dependiendo de si el elemento pertenece o no al conjunto:

<pre><code>17 in conjunto</code></pre>

Suele utilizarse en expresiones condicionales, como la que sigue:

<pre><code>if 'a' in letras then</code></pre>
