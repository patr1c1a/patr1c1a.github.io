---
layout: post
title: Arreglos en Pascal
date: 2011-06-2 19:00:00
categories: pascal
published: true
---

## Vectores (arreglos de 1 dimensión)

Un vector es una agrupación de datos que tienen un orden (por eso la denominación "arreglo") y que son todos del mismo tipo (por eso en Pascal los arreglos son _homogéneos_).

El orden está dado por un índice, que dentro de Pascal es representado por una variable de tipo ordinal, en un rango que se indica al declarar el tipo. La cantidad máxima de elementos que un vector puede contener en Pascal es 250.
Los vectores se almacenan en la memoria en posiciones consecutivas, por lo que es posible acceder en forma directa a alguno de los datos contenido en un vector por medio de su índice.
La declaración de un vector se hace utilizando la palabra reservada _array_, seguida del índice _(límite inferior y límite superior)_ y el tipo de dato que el vector contendrá:

<pre><code>type vector = array [1 .. 50] of integer;</code></pre>

En este caso se ha declarado un tipo de arreglo que tiene 50 lugares para guardar números enteros, con un índice que comienza en el número 1 y finaliza en el 50. Pero nada obsta a que el índice comience en otro número arbitrario o que, incluso, no sea de tipo entero.

Al declarar una variable del tipo del arreglo que se ha definido (_vector_, en este ejemplo) se podrá acceder a un elemento en particular del mismo por medio de su índice. Por ejemplo, si en una variable de tipo _vector_, tal como fue descripto arriba, se deseara almacenar un valor en el quinto elemento, se podría hacer lo siguiente:

Declaración de la variable: <code>var arreglo: vector;</code>

Acceso al quinto elemento del vector para asignarle un valor: <code>arreglo[5] := 700;</code>

Por supuesto, como el vector fue declarado de números enteros, sólo podrá asignársele valores enteros. De la misma forma, debido a que se utilizaron números para determinar el índice, se accederá colocando un número en los corchetes. Si el índice del vector fuera de caracteres (por ejemplo, de 'a' hasta 'z'), el quinto elemento debería ser referenciado de la siguiente forma: <code>arreglo['e'] := 700;</code>

También puede referenciarse al índice por medio de una variable que coincida con el tipo de dato utilizado para el índice. En caso de que el índice sea numérico, podría utilizarse una variable de tipo _integer_ como índice. Esta es la forma en que generalmente se hará referencia a una posición del vector. Por ejemplo, si se deseara rellenar el vector anterior con el número 0 en cada una de sus 50 posiciones, se podría declarar una variable de tipo entero y llenar el vector utilizando una estructura iterativa:

<pre>for i := 1 to 50 do
   arreglo[i] := 0;</pre>

Debe recordarse que Pascal es fuertemente tipado, por lo que no pueden asignarse tipos de datos diferentes entre sí. Por lo que, de ser necesario rellenar un vector con la repetición de un número entero, no podría asignarse este número directamente al vector (<code>arreglo:=0</code>), ya que el arreglo es de un tipo _array_ y el número es de tipo _integer_. En cambio, el vector en cada una de sus posiciones sí contiene datos de tipo integer, por lo que es perfectamente posible asignar como se hizo en el ejemplo iterativo anterior. Esto es un efecto de la abstracción.

&nbsp;

## Matrices (arreglos de n dimensiones)

Una matriz no es más que un vector con más de una dimensión (o un "vector de vectores").

Lo más común es utilizar matrices de dos dimensiones. Serían lo que en lenguaje coloquial se llama “tablas”, ya que son una combinación de filas y columnas. Al igual que los arreglos de una dimensión (vectores), el tipo de datos que contienen es homogéneo (es decir, todos datos del mismo tipo).
La declaración del tipo es muy similar a la de un vector con la diferencia de que, en este caso, se usarán dos índices (el primero para las filas y el segundo para las columnas):

<pre><code>type matriz = array [1..5, 1..3] of integer;</code></pre>

Esta matriz de 5 filas y 3 columnas correspondería a un esquema gráfico como el siguiente:

<table>
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<tr>
<td border="1">&nbsp;</td>
<td border="1">&nbsp;</td>
<td border="1">&nbsp;</td>
</tr>
<tr>
<td border="1">&nbsp;</td>
<td border="1">&nbsp;</td>
<td border="1">&nbsp;</td>
</tr>
<tr>
<td border="1">&nbsp;</td>
<td border="1">&nbsp;</td>
<td border="1">&nbsp;</td>
</tr>
<tr>
<td border="1">&nbsp;</td>
<td border="1">&nbsp;</td>
<td border="1">&nbsp;</td>
</tr>
<tr>
<td border="1">&nbsp;</td>
<td border="1">&nbsp;</td>
<td border="1">&nbsp;</td>
</tr>
</table>
Un elemento en una matriz se referencia con todos sus índices: <code>arreglo[4,1]</code> corresponde a la cuarta fila, primera columna.

Para recorrer una matriz, es necesario utilizar estructuras iterativas anidadas, ya que por un lado se debe recorrer el índice de las filas y, por otro, el de las columnas:

<pre><code>for i := 1 to 5 do
begin
     for k := 1 to 3 do
        arreglo[i,j] := 0;
end;</code></pre>

