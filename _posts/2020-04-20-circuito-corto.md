---
layout: post
title: Evaluación por circuito corto en operaciones lógicas
date: 2020-04-20 21:00:00
categories: conceptos
tags: booleanos logica condicionales
published: true
---


¿Qué sucede si tenemos una condición como if (A and B), donde B resulta ser un objeto nulo? Tener en cuenta el circuito corto permite evitar estos errores.

false and [cualquier cosa] ---> siempre resultará false.
true or [cualquier cosa] ---> siempre resultará true.

![circuito corto]({{ site.url }}/assets/2020-04-20-circuito-corto.png)
