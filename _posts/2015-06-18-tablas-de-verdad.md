---
layout: post
title: Tablas de verdad
date: 2015-06-18 10:00:00
categories: conceptos
published: true
---

# Valor de verdad

Las tablas de verdad son un elemento de la lógica proposicional para determinar el valor de verdad (es decir, si es "verdadero" o "falso") de una proposición. Los valores de verdad posibles son dos: **verdadero** y **falso**, que también pueden expresarse como **1** y **0**. Una proposición sólo puede ostentar uno de ellos (ni los dos a la vez, ni ninguno de ellos). Estos valores se llaman "booleanos" por el álgebra de Boole, que tiene la particularidad de operar con datos binarios (que sólo tienen dos valores posibles).

Normalmente se representa al valor Verdadero con la letra V y al valor Falso con la F. También se usan las letras T (por "true", "verdadero" en inglés) y F (por "false", "falso" en inglés).


# Proposición

Una proposición es una afirmación capaz de tener un valor de verdad. Es decir, una oración de la cual se puede decir que es verdadera o que es falsa.

_Ejemplo 1:_

<pre>"El día está soleado" (será verdadero o será falso, según si el día está o no está soleado).</pre>


Una proposición puede ser: atómica si no puede subdividirse, o molecular si está compuesta por dos o más proposiciones, unidas por un operador lógico.

_Ejemplo 2:_

Proposición atómica: <code>"El día está soleado".</code>

Proposición molecular: <code>"El día está soleado y caluroso"</code>. Es molecular porque puede sudividirse en dos proposiciones: "el día está soleado" y "el día está caluroso".



Cuando se realizan operaciones con proposiciones, uniéndolas mediante **operadores lógicos**, se suele dar nombres (usualmente compuestos de una sola letra) a las proposiciones. Esto es para ayudar a la legibilidad. Entonces podríamos decir que la proposición "el día está soleado" se va a llamar "p" y que la proposición "el día está caluroso" se va a llamar "q". Como tenemos también una proposición molecular que se forma al unir estas dos, podemos darle el nombre "r" a la proposición "el día está soleado y caluroso".

# Operaciones lógicas

Una operación lógica se compone de operandos (proposiciones) y operadores. Mediante una operación lógica se unen proposiciones para obtener una nueva proposición compuesta.

Los operadores lógicos (también llamados "conectores lógicos") usados para unir proposiciones son: AND ("y"), OR ("o"), NOT ("no"), IMPLICA, BICONDICIONAL ("si y sólo si"). Mediante ellos se forman proposiciones moleculares.

El operador AND se representa mediante el símbolo ![operador and](/assets/2015-06-18-tablas-de-verdad-img3.jpg) y se utiliza para la operación **conjunción**.

El operador OR se representa mediante el símbolo ![operador or](/assets/2015-06-18-tablas-de-verdad-img4.jpg) y se utiliza para la operación **disyunción**.

El operador NOT se representa mediante el símbolo ![operador not](/assets/2015-06-18-tablas-de-verdad-img5.jpg) y se utiliza para la operación **negación**.

El operador IMPLICA se representa mediante el símbolo ![operador implicación](/assets/2015-06-18-tablas-de-verdad-img1.jpg) y se usa para la operación **implicación** (también llamada "**condicional**"). A la proposición que se coloca a la izquierda del operador se la llama "_antecedente_" y a la que se coloca a la derecha de la llama "_consecuente_". Esta operación no es conmutativa.

El operador BICONDICIONAL se representa mediante el símbolo ![operador bicondicional](/assets/2015-06-18-tablas-de-verdad-img2.jpg) y se usa para la operación **doble implicación** (también llamada "**equivalencia**").

La negación es una operación unaria, porque involucra un único operando (proposición). El resto son binarias, porque involucran dos operandos.

Además, pueden unirse más de dos proposiciones, usando más de un operador lógico.


# Tabla de verdad de cada operador lógico

Como dijimos, los operadores lógicos unen proposiciones. Entonces, al unir dos proposiciones, se obtiene una nueva proposición, cuyo valor de verdad dependerá de cuáles son concretamente los valores de verdad de las proposiciones unidas. Si, por ejemplo, hoy el día está soleado y además caluroso, podemos decir que la proposición "p" es **verdadera** y que la proposición "q" también es **verdadera**. Pero tenemos que ver qué pasa con la proposición "r", que está compuesta por "p ![operador and](/assets/2015-06-18-tablas-de-verdad-img3.jpg) q" (es decir, es una conjunción). Para averiguar cuál es ese resultado, se debe conocer el valor de verdad de p (que ya acordamos que, en este ejemplo es Verdadero), el valor de verdad de q (que, en este ejemplo es Falso) y la tabla de verdad de la conjunción. Si el operador lógico fuera ![operador or](/assets/2015-06-18-tablas-de-verdad-img4.jpg) ("o") usaríamos la tabla de verdad de la disyunción, y así siempre usando la tabla de la operación correspondiente.

Las tablas de las operaciones, de acuerdo a las distintas posibles combinaciones de los valores de verdad de los operandos, son las siguientes:

&nbsp;

## CONJUNCIÓN
![tabla de conjunción](/assets/2015-06-18-tablas-de-verdad-img6.jpg)

Esto se lee:
  
Cuando **p** es Verdadero y **q** es Verdadero, **p ![operador and](/assets/2015-06-18-tablas-de-verdad-img3.jpg) q** es Verdadero
  
Cuando **p** es Verdadero y **q** es Falso, **p ![operador and](/assets/2015-06-18-tablas-de-verdad-img3.jpg) q** es Falso
  
Cuando **p** es Falso y **q** es Verdadero, **p ![operador and](/assets/2015-06-18-tablas-de-verdad-img3.jpg) q** es Falso
  
Cuando **p** es Falso y **q** es Falso, **p ![operador and](/assets/2015-06-18-tablas-de-verdad-img3.jpg) q** es Falso

La característica de la conjunción es que sólo es V cuando ambos operandos son V.


## DISYUNCIÓN

![tabla de disyunción](/assets/2015-06-18-tablas-de-verdad-img7.jpg)

Esto se lee:
  
Cuando **p** es Verdadero y **q** es Verdadero, **p ![operador or](/assets/2015-06-18-tablas-de-verdad-img4.jpg) q** es Verdadero
  
Cuando **p** es Verdadero y **q** es Falso, **p ![operador or](/assets/2015-06-18-tablas-de-verdad-img4.jpg) q** es Verdadero
  
Cuando **p** es Falso y **q** es Verdadero, **p ![operador or](/assets/2015-06-18-tablas-de-verdad-img4.jpg) q** es Verdadero
  
Cuando **p** es Falso y **q** es Falso, **p ![operador or](/assets/2015-06-18-tablas-de-verdad-img4.jpg) q** es Falso

La característica de la disyunción es que sólo es F cuando ambos operandos son F.


## NEGACIÓN

![tabla de negación](/assets/2015-06-18-tablas-de-verdad-img8.jpg)

La característica de la negación es que invierte el valor de verdad de la proposición.

## IMPLICACÓN

![tabla de implicación](/assets/2015-06-18-tablas-de-verdad-img8.jpg)

Esto se lee:
  
Cuando **p** es Verdadero y **q** es Verdadero, **p ![operador implicación](/assets/2015-06-18-tablas-de-verdad-img1.jpg) q** es Verdadero
  
Cuando **p** es Verdadero y **q** es Falso, **p ![operador implicación](/assets/2015-06-18-tablas-de-verdad-img1.jpg) q** es Verdadero
  
Cuando **p** es Falso y **q** es Verdadero, **p ![operador implicación](/assets/2015-06-18-tablas-de-verdad-img1.jpg) q** es Verdadero
  
Cuando **p** es Falso y **q** es Falso, **p ![operador implicación](/assets/2015-06-18-tablas-de-verdad-img1.jpg) q** es Falso

La característica de la implicación es que sólo es F cuando el antecedente es V y el consecuente es F.

## DOBLE IMPLICACIÓN

![tabla de bicondicional](/assets/2015-06-18-tablas-de-verdad-img9.jpg)

Esto se lee:
  
Cuando **p** es Verdadero y **q** es Verdadero, **p ![operador bicondicional](/assets/2015-06-18-tablas-de-verdad-img2.jpg) q** es Verdadero
  
Cuando **p** es Verdadero y **q** es Falso, **p ![operador bicondicional](/assets/2015-06-18-tablas-de-verdad-img2.jpg) q** es Falso
  
Cuando **p** es Falso y **q** es Verdadero, **p ![operador bicondicional](/assets/2015-06-18-tablas-de-verdad-img2.jpg) q** es Falso
  
Cuando **p** es Falso y **q** es Falso, **p ![operador bicondicional](/assets/2015-06-18-tablas-de-verdad-img2.jpg) q** es Verdadero

La característica de la doble implicación es que sólo es V cuando ambos operadores tienen el mismo valor de verdad.
