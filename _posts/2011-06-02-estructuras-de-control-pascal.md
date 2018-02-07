---
layout: post
title: Estructuras de control en Pascal
date: 2011-06-02 19:00:00
categories: pascal
tags: paradigma_imperativo bucle loop while if for case
published: true
---

Las estructuras de control permiten dirigir el sentido que tomará la ejecución del programa. Si una estructura contiene más de una sentencia, éstas deberán encerrarse entre las instrucciones "begin" y "end;" para indicar que ese bloque de código corresponde a esa estructura en particular.

Al igual que en los demás lenguajes, en Pascal existen estructuras selectivas y estructuras repetitivas.

# Estructuras selectivas

Hacen que el curso del programa se bifurque en una u otra dirección dependiendo de las condiciones que se cumplan durante su ejecución.

## Selección simple: IF - THEN - ELSE ("si" - "entonces" - "si no")

Evalúa una proposición y efectúa una acción si el resultado es verdadero, con el siguiente formato: <code>si proposición=verdadera entonces ejecutar acción</code>.

De manera opcional, se puede establecer una acción a realizar para el caso de que la proposición evaluada resulte falsa: <code>si proposición=verdadera entonces ejecutar acción 1. Si no, ejecutar acción 2</code>.

La sintaxis en Pascal es la siguiente:

<pre><code>if  proposición=verdadera  then
    ejecutar acción 1
else
    ejecutar acción 2</code></pre>

La "acción 1" puede estar compuesta por más de una instrucción, en cuyo caso se colocará una etiqueta "begin" al comienzo y "end;" al final, y cada sentencia dentro del bloque se diferenciará de la siguiente mediante un punto y coma. Como excepción, si la estructura lleva la instrucción **else**, en la línea inmediatamente anterior a ella debe obviarse el punto y coma, ya que el punto y coma señala el final de la instrucción "if" y, si ésta incluye "else", el final de la instrucción completa se encuentra al término de éste.

Pueden combinarse varias proposiciones unidas mediante conectores lógicos "and" y "or". Éstos funcionan de la misma forma en que funcionan las operaciones lógicas en tablas de verdad: en el caso del "and" ambas condiciones deben resultar verdaderas para que el resultado sea _true_; en el caso del "or" basta con que una de ella resulte verdadera. Si se utilizan proposiciones unidas por conectores lógicos, deben estar encerradas entre paréntesis:

<pre><code>if (proposición_1 = verdadera) and (proposición_2 = verdadera) then
begin   
    sentencia 1
    sentencia 2
end;</code></pre>

Las proposiciones no son más que algún valor booleano que se indique como true o false. Es decir, la proposición a evaluarse puede estar conformada por una expresión que se traduzca en true o en false (una comparación, una variable booleana, una llamada a función...). De cualquier forma, la sentencia "if" siempre comparará la proposición con el valor _true_ y ejecutará las instrucciones que contiene si esa proposición coincide con ese valor. Así, podría escribirse algo como:

<pre><code>if (variable1) and (variable2) then</code></pre>

En el ejemplo anterior, "variable1" y "variable2" son dos variables booleanas.

También puede expresarse la negación de una proposición anteponiendo la palabra reservada "not", que equivale a decir que el resultado de la evaluación debe ser falso:

<pre><code>if not  proposición  then
    sentencia</code></pre>

En este caso, la sentencia "if" también evaluará el valor de verdad de la condición comparándolo con true: si la proposición indicada no se cumple, entonces el resultado será true.

&nbsp;

##  Selección múltiple: CASE ("caso")
  
Se utiliza para seleccionar una opción de entre varias. Es una forma de evitar múltiples "if". La expresión a evaluar es llamada "selector" y consta de la palabra **case** seguida de una **variable** de tipo ordinal y la palabra reservada **of**. Luego se establece una lista de sentencias de acuerdo a diferentes valores que puede adoptar la variable (los "casos"). Opcionalmente, se puede establecer un bloque **else** para el caso de que la variable adopte un valor que no coincida con ninguna de las sentencias de la lista. Finalizada la estructura del case se coloca un "end;" (en este caso no se corresponde con ningún "begin"). El formato es el siguiente:

<pre><code>case variable_ordinal of
    valor1: sentencia 1;
    valor2: sentencia2;
    valor3: sentencia3;
else
    sentencia4;
end;</code></pre>


# Estructuras iterativas

Permiten que una sentencia o un bloque de código se repita una determinada cantidad de veces.

##  Iteración fija: FOR ("para")
  
Realiza una iteración una cantidad de veces explícita. Para ello necesita una variable de tipo ordinal, a la que asignará valores dentro del rango que se le especifique, incrementándose en uno. Por ejemplo, si se declara una variable llamada "cuenta" de tipo integer, se puede utilizar un for con el siguiente formato:

<pre><code>for cuenta := 5 to 9 do
    sentencia</code></pre>

En este caso la sentencia se ejecutará cinco veces, ya que la variable "cuenta" primero adoptará el valor 5, luego el valor 6, y así hasta llegar al 9, en que repetirá la sentencia por última vez.

Por supuesto, los valores literales pueden reemplazarse por variables o por constantes, siempre que ellos hayan sido declarados y se les haya asignado algún valor previamente:

<pre><code>for cuenta := 1 to maximo do
    sentencia</code></pre>

Una variante es asignar los valores decrementando la variable. Es decir, para el primer ejemplo, la variable adoptaría primero el valor 9, luego el 8, y así sucesivamente hasta llegar al 5 y terminar la iteración. Esto se efectúa mediante la palabra reservada "downto":

<pre><code>for cuenta := 9 downto 5 do
    sentencia</code></pre>

## Iteración condicional: WHILE ("mientras")
  
Se evalúa una proposición (o un grupo de ellas unidas por conectores lógicos) y, de resultar verdadera, se ejecutan las sentencias, repitiéndose el proceso hasta que la proposición deje de ser verdadera. En este caso es importante prever que en algún momento la proposición se vuelva falsa, porque de lo contrario se entraría en un bucle infinito. Por ejemplo, si se utilizara un **while** para llevar la cuenta de algo, el formato sería similar al siguiente:

<pre><code>contador := 0;
read(edad);
while edad <= 21 do
begin
    contador := contador + 1;
    read(edad);
end;</code></pre>

En este caso se utilizan dos variables de tipo entero, "contador" y "edad", y el bloque de código incrementa la variable "contador" en 1 cada vez que se lee de teclado una edad menor o igual a 21.

Notar que se inicializó la variable "contador" en 0, para evitar que se sume contenido "basura", y que previamente a evaluar la proposición se le dio un valor a la variable "edad" (ingresado por teclado), ya que de lo contrario se estaría evaluando contenido "basura" en la primera iteración. Luego, dentro del bloque, se vuelve a asignar un valor a la variable a través del teclado, para que exista la posibilidad de que la proposición resulte falsa en algún momento, al cambiar el valor de la variable _edad_.

El while se caracteriza por evaluar la condición (comparándola con el valor "true") antes de ejecutar el bloque de código. Es decir, si la proposición fuera falsa en la primera evaluación, el bloque nunca se ejecuta.

##  Iteración condicional: REPEAT UNTIL ("repetir hasta")
  
Similar al while, funciona repitiendo una sentencia o un bloque de código hasta que se cumpla una condición (hasta que la condición se vuelva verdadera, es decir, hasta que valga "true"). En este caso, en primer lugar se ejecutan las sentencias y luego se evalúa, y la iteración se realizará mientras la proposición no sea verdadera. El formato es el siguiente:

<pre><code>contador := 0;
repeat
    read (edad);
    contador := contador+1;
until edad > 21;</code></pre>

En este caso existe una excepción en cuanto a la necesidad de encerrar el bloque de código entre etiquetas "begin" y "end", aunque si se colocan no afectan la ejecución del programa.
