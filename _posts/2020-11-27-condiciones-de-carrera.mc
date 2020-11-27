---
layout: post
title: Condiciones de carrera o "race conditions"
date: 2020-11-27 12:00:00
categories: conceptos
tags: semáforos mutex race
published: true
---

Aunque las condiciones de carrera no son exclusivas de la programación concurrente, es donde usualmente corremos el riesgo de encontrarnos con este problema. En algunos casos, la depuración del código para encontrar el error puede tornarse muy compleja.

En el siguiente ejemplo es posible observar un código Java donde 3 hilos compiten por acceder a un recurso compartido, arrojando un resultado diferente con cada ejecución del programa.

[Click acá para ver el ejemplo](https://repl.it/@programacionde1/race-condition-ejemplo#Main.java){:target="_blank"}.

![Race conditions]({{ site.url }}/assets/2020-11-27-condiciones-de-carrera.png)
