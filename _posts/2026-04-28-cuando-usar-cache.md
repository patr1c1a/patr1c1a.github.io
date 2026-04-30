---
layout: post
title: Cuándo usar cache (y cuándo no)
date: 2026-04-28 16:00:00
categories: design
tags: system_design cache arquitectura
published: true
---

A veces notamos que cada request a nuestra API tarda más de lo que nos gustaría. Revisamos un endpoint y encontramos que, cada vez que alguien hace una consulta puntual, el sistema va a la base de datos y vuelve. No parece grave… hasta que pensamos en muchos usuarios haciendo exactamente lo mismo al mismo tiempo.

En ese punto aparece la típica idea: "¿y si agregamos cache?". Suena razonable, pero también deberíamos preguntarnos: ¿esto realmente mejora algo en todos los casos? ¿o hay situaciones donde incluso puede complicar más las cosas?

El problema es que esa decisión suele tomarse casi por reflejo, sin detenerse demasiado a mirar el contexto. Y ahí es donde muchos sistemas empiezan a volverse más complejos sin una mejora clara.

En el video tomo un ejemplo concreto de un sistema que consulta productos y lo llevo a una situación real, mostrando exactamente qué es lo que suele pasarse por alto cuando aparece la idea de "poner cache".

{% include youtubePlayer.html id="idVQxi06JL0" %}
