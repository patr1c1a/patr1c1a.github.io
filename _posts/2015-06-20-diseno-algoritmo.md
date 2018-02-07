---
layout: post
title: Diseño de un algoritmo
date: 2015-06-20 19:00:00
categories: conceptos
tags: algoritmos, resolucion_problemas
published: true
---


Diseñar un algoritmo es armar una solución para un problema o desafío a superar.

Imaginemos que el desafío es construir una mesa. Entonces empezamos a planificar qué herramientas y materiales podemos usar y qué estrategias aplicar para construir la mesa con esas herramientas y materiales que tenemos disponibles.

Como herramientas y materiales podríamos decidir usar un martillo de cierto tamaño, una sierra, lija de determinado grosor, clavos, pegamento, madera de un tipo particular. Esto sería equivalente a elegir el lenguaje de programación más adecuado, el IDE, el compilador, etc. Por ejemplo, el lenguaje podría ser Python, el IDE ser “IDLE”, y el compilador ser el de Python 3.4.

Las estrategias de construcción se pueden equiparar a la parte de armar el algoritmo. Primero vamos a empezar por el esqueleto (la estructura general) para después ir ahondando en los detalles. Es importante tener en cuenta que acá no vamos a ver los detalles de implementación, sino que vamos a expresar en lenguaje coloquial lo que queremos hacer.

* Empezamos por la estructura general: primero vamos a construir un esqueleto de la mesa, armando una tabla y cuatro patas con la madera, y después los vamos a unir. Por ahora no nos interesa demasiado cómo vamos a construir las patas o la tabla o cómo vamos a hacer para unirlas, pero sí sabemos cuál va a ser la estructura general de la mesa (por ejemplo: “quiero hacer una mesa redonda que tenga 50 centímetros de alto”). Esto se equipara a armar el programa principal: el “esqueleto” del programa. Probablemente nuestro programa principal necesite usar funciones que hagan determinadas cosas, pero todavía no importa demasiado cómo las hacen, solamente nos importa saber que eso en algún momento va a estar hecho y vamos a obtener el resultado. Es como decir “sé que voy a hacer una tabla y 4 patas, y que en algún momento las voy a tener hechas y las voy a usar en esta parte de la mesa para sostener la tabla, pero todavía no sé cómo, porque por ahora estoy armando la idea general de lo que quiero obtener”. En un programa, esto sería como decir “sé que acá va a haber un módulo que usará determinados datos, hará determinada operación con ellos y me devolverá un resultado de determinado tipo”, pero todavía no nos concentramos en cómo ese módulo hará esa operación para conseguir el resultado.

* Una vez que tenemos la estructura general, entonces sí empezamos a pensar en cómo hacer los detalles, por ejemplo: cómo cortar la madera, cómo darle la forma redonda para obtener la tabla, cómo lijar las patas para que tengan la porosidad adecuada, etc., para ir construyendo las partes que vamos a necesitar para finalmente encastrarlas y armar la mesa. Esto sería como construir los módulos o subprogramas, concentrándonos en cada uno de ellos y en las operaciones que cada uno hace y los datos que necesitan para trabajar y resultados que arrojan.

Al diseñar un algoritmo, siempre debemos cuidar de no perder de vista el problema que resuelve, porque terminaríamos con una solución inexacta. Esto es muy importante cuando se trabaja en equipo, o bien se trabaja para usuarios que no son humanos sino otras máquinas, y que esperan recibir un resultado determinado, en una forma muy bien definida, porque ese resultado luego es usado para solucionar otro problema.
