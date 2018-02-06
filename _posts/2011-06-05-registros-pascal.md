---
layout: post
title: Registros en Pascal
date: 2011-06-05 19:00:00
categories: pascal
published: true
---
Un registro es una estructura que permite agrupar datos de diversos tipos con alguna clase de correspondencia lógica. Cada uno de estos datos que componen un registro es llamado "**campo**".

Un campo tiene un nombre y un tipo, ya que cada uno de ellos es una variable (sólo que en este caso la palabra "var" no aparece en cada uno de los campos).

Un ejemplo de utilización sería el de un registro conteniendo los datos de un empleado, en el que los campos podrían ser el nombre y apellido (de tipo string), la edad (de tipo integer), el sueldo (de tipo real), etc.

Una estructura de estas características se define de la siguiente forma:

<pre><code>type empleado = record
   nombre: string[50];
   edad: integer;
   sueldo: real;
end;</code></pre>

Nótese que la estructura finaliza con la etiqueta "end;" pero no existe un "begin" que le corresponda.

Los datos contenidos en un campo pueden ser de cualquier tipo, incluso otros datos estructurados (por ejemplo, uno de los campos podría estar constituido por un arreglo, o incluso por otro registro).

Definido el tipo, se puede declarar una variable del tipo registro y asignarle valores a cada uno de los campos. Para referenciar a cada uno de ellos se utiliza un punto separando el nombre de la variable del nombre del campo. Siguiendo el ejemplo anterior, podría definirse una variable llamada "roberto" del tipo "empleado", y completar cada uno de sus campos de la siguiente forma:

<pre><code>roberto.nombre:= 'Roberto Gomez';
roberto.edad:= 58;
roberto.sueldo:= 2440.5;</code></pre>

Un registro puede ser asignado a otro sin necesidad de hacer referencia a cada uno de sus campos, siempre que ambos sean del mismo tipo. Por ejemplo, si se tuviera una variable llamada "andres" de tipo "empleado" y se deseara rellenar sus campos con los mismos datos que contiene el registro "roberto", podría hacerse la siguiente asignación: <code>andres := roberto;</code>

Podrá observarse que el uso de muchas variables de tipo registro puede resultar engorroso en caso de necesitar gran cantidad de ellas. Supóngase que una empresa debe mantener información de 100 empleados: sería casi imposible mantener el código para almacenar los datos de cada uno de ellos en variables separadas. Por esto es que los registros suelen agruparse en otras estructuras, como los arreglos.


## Arreglos de registros

Se trata de la construcción de un arreglo, tal como se haría con cualquier otro, cuyo tipo de dato sea un tipo registro. Para esto se hará necesario que el tipo registro esté definido con anterioridad. Por ejemplo:

<pre><code>type empleado = record
   nombre: string[50];
   edad: integer;
   sueldo: real;
   end;
vector = array [1 .. 100] of empleado;</code></pre>

De esta forma, pueden organizarse varios registros dentro de un arreglo ordenado de ellos.

A fines gráficos, el vector resultante de esta definición se podría graficar de la siguiente manera:

![arreglo de empleados](/assets/2011-06-5-registros-pascal-img1.png)

En este caso, el nombre de la variable de tipo record será el de la variable de tipo array con su índice, seguido del punto y el nombre del campo: suponiendo que se declaró una variable llamada "arreglo" y que el índice se referencia con una variable entera "i", se puede acceder a cada campo de cada posición del arreglo de la siguiente forma:

<pre><code>arreglo[i].nombre
arreglo[i].edad
arreglo[i].sueldo</code></pre>

De esta forma se podría llenar cada campo de los registros contenidos en un vector utilizando una estructura iterativa, como en el ejemplo siguiente:

<pre><code>i:= 1;
write('Ingrese nombre del empleado. Para terminar ingrese zzz: ');
readln(n);
while (i &lt;= 100)  and  (n &lt;&gt; 'zzz') do
begin
   arreglo[i].nombre:= n;
   write('Ingrese edad del empleado: ');
   readln(arreglo[i].edad);
   write('Ingrese sueldo del empleado: ');
   readln(arreglo[i].sueldo);
   write('Ingrese nombre del empleado. Para terminar ingrese zzz: ');
   readln(n);
   i:= i+1;
end;</code></pre>

Deben realizarse algunas observaciones en cuanto a este ejemplo. En primer lugar, debido a que la estructura utilizada es un **while**, el índice del arreglo debe moverse "manualmente". Por esto se utiliza una variable "i" del mismo tipo que el índice (en este caso, integer), que se inicializa en 1 (ya que el primer elemento del arreglo tiene el índice 1) y se la incrementa dentro de cada iteración.

La razón para utilizar una estructura while es que ésta permite establecer una condición de corte para el caso de que se desee interrumpir la carga de datos antes de completar todos los espacios disponibles en el vector. En el ejemplo, la condición de corte es que el nombre ingresado sea "zzz".

Así, la condición a evaluar en el while es doble: por un lado, que el índice (i) no supere el máximo de espacio del vector (en este ejemplo, cien); por otro, que el nombre sea diferente de "zzz".

Para permitir evaluar la condición de corte, es necesario que la variable contenga algún valor para que sea evaluado en la primera iteración. En este caso, como los datos deben ser almacenados en el vector siempre y cuando el nombre no sea "zzz", se utiliza una variable auxiliar del mismo tipo que el campo "nombre" (string), ya que si se leyera directamente sobre la variable a almacenar en el vector (<code>arreglo[i].nombre</code>), el nombre "zzz" quedaría cargado.

