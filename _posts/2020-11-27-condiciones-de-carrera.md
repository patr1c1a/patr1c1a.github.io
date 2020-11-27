---
layout: post
title: Condiciones de carrera o "race conditions"
date: 2020-11-27 12:00:00
categories: conceptos
tags: semáforos mutex race
published: true
---

Cuando nuestra aplicación require el uso de "threads" (o "hilos") podemos encontrarnos con el temido problema de las condiciones de carrera. En algunos casos, la depuración del código para encontrar el error puede causarnos muchos dolores de cabeza.

En el siguiente ejemplo es posible observar un código Java donde 3 hilos compiten por acceder a un recurso compartido, arrojando un resultado diferente con cada ejecución del programa.

[Click acá para ver el ejemplo](https://repl.it/@programacionde1/race-condition-ejemplo#Main.java){:target="_blank"}.

![Race conditions]({{ site.url }}/assets/2020-11-27-condiciones-de-carrera.png)
