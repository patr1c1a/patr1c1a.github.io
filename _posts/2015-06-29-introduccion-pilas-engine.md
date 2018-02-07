---
layout: post
title: Introducción a Pilas Engine (motor de videojuegos en español para principiantes)
date: 2015-06-29 19:00:00
categories: python
tags: objetos juegos
published: true
---

Pilas Engine es un [motor](https://es.wikipedia.org/wiki/Motor_de_videojuego) para programar videojuegos de manera sencilla y sólo con conocimientos básicos de programación.

Para poder utilizar Pilas y no morir en el intento, es necesario manejar algunos conceptos iniciales de programación, como los [tipos de datos](/conceptos/2015/06/18/tipos-de-datos.html), las [estructuras de control](/conceptos/2015/06/23/estructuras-de-control.html) y [funciones](/conceptos/2015/06/23/funciones.html).

Y, a pesar de que está pensado para principiantes, para hacer algo "serio" seguramente será necesario investigar algunas cosas específicas de Pilas, para lograr lo que sea que se esté construyendo. Para ello, hay documentación oficial en español que puede consultarse acá:

* Manual: [http://manual.pilas-engine.com.ar/](http://manual.pilas-engine.com.ar/)
* API (documentación sobre objetos y funciones): [http://api.pilas-engine.com.ar](http://api.pilas-engine.com.ar/)
* Comunidad de usuarios: [http://foro.pilas-engine.com.ar](http://foro.pilas-engine.com.ar/)


## Instalación de Pilas Engine:

Desde [acá](http://pilas-engine.com.ar/#/descargas) puede descargarse la última versión para Windows, Mac o Linux. También puede descargarse el código fuente, para quienes quieran ver cómo está programado o, incluso, hacerle cambios. Además están disponibles versiones anteriores.


## ¿Qué es precisamente Pilas Engine?

Pilas está orientado a facilitar el desarrollo de videojuegos a personas que generalmente no hacen juegos, utilizando Python. Más técnicamente, es una [biblioteca](https://es.wikipedia.org/wiki/Biblioteca_%28inform%C3%A1tica%29) para Python. Es decir que resuelve gran parte del problema sobre cómo programar un videojuego y nos deja situados varios pasos más adelante, para poder concentrarnos en programar el juego directamente, sin necesidad de preocuparnos por muchos detalles que el desarrollo de juegos implica, como la física, el control de la pantalla, diseño de personajes, control de los personajes, etc. Entonces podemos ver que Pilas es de _alto nivel_, ya que oculta toda esta complejidad que en realidad sucede "por debajo" de nuestros juegos.

Pilas fue originalmente desarrollado en español, por lo que todas las instrucciones, documentación, manuales y ejemplos que provee al desarrollador de juegos están disponibles en nuestro idioma.

## Componentes básicos en un programa de Pilas

Son 3:

* Mundo
* Actor
* Motor

El mundo es el "universo" dentro del cual se desarrolla el juego que hagamos. Se encarga de mantener el juego en funcionamiento e interactuar con el usuario. Para quien disfruta de los términos técnicos, el mundo en Pilas es un objeto singleton (los principiantes no deberían preocuparse por este concepto aún).

Los actores son los personajes y objetos que conforman el juego (en otros motores de búsqueda se suelen llamar "sprites"). Pilas ya trae varios incorporados, aunque podríamos agregar nuevos. Para quienes entienden un poco más de programación orientada a objetos, Actor es una clase dentro de Pilas.

El motor permite que pilas sea portable y multiplaforma. Pilas deelega la tarea de dibujar, emitir sonidos y controlar eventos a una biblioteca externa.


## Cómo usar Pilas en un programa Python

Al instalar Pilas tendremos un intérprete interactivo que viene con la instalación. Es decir, no necesitamos nada más. Pero también es posible usar Pilas desde el intérprete de Python.

En el código de nuestro programa se debe indicar que vamos a usar la biblioteca de Pilas. Esto se hace mediante la siguiente instrucción: <code>import pilasengine</code>

A continuación, es necesario indicarle a Pilas que empiece a funcionar. Para esto le damos la orden "iniciar", sin ningún parámetro: <code>pilasengine.iniciar()</code>

Esta orden ("iniciar"), además de poner todo en funcionamiento, hace que se "dibuje" en pantalla la ventana del juego, dentro de la cual se va a llevar a cabo toda la acción (como se ve, acá Pilas empieza a hacer su "magia", ya que no debemos preocuparnos por cómo lograr que aparezca una ventana en pantalla).

En este caso, **iniciar()** es una función que está incluida en Pilas y podemos utilizarla cuando la necesitemos, al igual que todas las demás funciones que Pilas nos provee. Es decir, sólo necesitamos saber para qué sirven y en de qué forma usarlas, sin que debamos conocer cómo están programadas o cómo trabajan internamente. Al hecho de utilizar una función suele nombrárselo como "invocación" o "llamada" de la función.

Pero, fuera de estos conceptos teóricos de programación, lo que nos importa es que, al resultado de esta función <code>pilasengine.iniciar()</code> lo podemos guardar en una variable, de la siguiente manera: <code>pilas = pilasengine.iniciar()</code> y, de esta manera, la variable llamada _pilas_ ahora puede usarse para hacer varias cosas en nuestro programa.

## Personajes

Un concepto importante en Pilas es del de "actores". Un **actor** en Pilas es un objeto que aparece en pantalla, tiene una posición determinada y se puede manipular. El motor ya incluye algunos personajes que se pueden usar para empezar. También el programador puede agregar los propios.

Para saber qué actores trae incluidos, podemos indicarle a Pilas que busque sus actores y nos brinde un listado:

<pre><code>pilas.actores.listar_actores()</code></pre>

En este caso, estamos refiriéndonos a los actores incluidos en Pilas de la siguiente forma:

<pre><code>pilas.actores</code></pre>

Y a ellos les estamos dando una instrucción:

<pre><code>listar_actores()</code></pre>

Esto nos da el indicio de que, cada vez que nos refiramos a **pilas.actores** estaremos hablando de los actores que tenemos disponibles para trabajar. Y, además, podremos darles órdenes mediante _funciones_.

## Ejecutar un juego

Es muy importante incluir, al final del programa, la orden <code>pilas.ejecutar()</code>. La función **ejecutar()** se encarga de mantener al juego en funcionamiento, mostrando la ventana y permitiendo que el jugador pueda interactuar con ella. Más técnicamente, esta función se encarga de actualizar lo que va pasando en el juego para que, cada vez que suceda algo, se muestre en pantalla. La documentación oficial de Pilas indica que: _"esta función es necesaria cuando se crea un juego en modo no-interactivo"_.

> **Información extra: ¿Qué significa para Pilas el "modo no-interactivo" (también llamado "modo normal")?**
> Pilas soporta dos modos de funcionamiento. El modo interactivo es el que normalmente se usa en el intérprete de Pilas y el que se suele ver en demostraciones y ejemplos. Concretamente, permite ir escribiendo código mientras la simulación está en funcionamiento. En cambio, en el modo normal se programa el juego y luego se lo ejecuta. Esto normalmente se hace escribiendo el código en un archivo con extensión .py que empiece con la llamada a la función _iniciar()_ que se menciona más arriba y que finalice con la llamada a _pilas.ejecutar()_.

## Estructura de un programa Python usando el motor Pilas

Recapitulando algunos detalles: para indicarle a Python que use las bibliotecas de Pilas necesitamos una instrucción "import", para iniciar el juego se debe dar la orden "iniciar()" y para que todo se ejecute correctamente se usa la instrucción "ejecutar()". Entonces, podemos deducir que el código del juego quedará comprendido entre las instrucciones "iniciar()" y "ejecutar()":

<pre><code>import pilasengine
pilas = pilasengine.iniciar()
<CÓDIGO DEL JUEGO>
pilas.ejecutar()</code></pre>

Un detalle interesante es que a la función **iniciar()** se le pueden pasar parámetros. Particularmente, podemos indicarle de qué tamaño (en pixels) queremos que sea la ventana que va a dibujar en pantalla para mostrar el juego, y qué título debe mostrar esa ventana:

<pre><code>pilasengine.iniciar(ancho=620, alto=540, titulo='Nombre del juego')</code></pre>

> **Para investigar:** ¿Qué otros parámetros admite la función iniciar()?

> Importante: para quienes hayan actualizado desde una versión vieja a una versión de Pilas Engine más nueva deberán tener en cuenta algunos cambios en el código. [En esta página se encuentra un listado completo](http://pilas-engine.com.ar/#/docs/guia_conversion).
