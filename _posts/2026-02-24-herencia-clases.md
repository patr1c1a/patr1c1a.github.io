---
layout: post
title: Un ejemplo de herencia que suele aclarar poco...
date: 2026-02-24 16:00:00
categories: poo
tags: clases herencia objetos poo superclase
published: true
---

El ejemplo típico de herencia de clases suele usar "Animal" como superclase y "Perro" y "Gato" como subclases.

Y no está mal, pero si no se explica en el contexto de un sistema real, ese ejemplo se queda corto.

En muchas ocasiones se pone a la clase "Animal" con atributos del estilo de "nombre", "cantidad_de_patas", o "dueño", y comportamientos (o métodos) como "alimentar()" o "emitir_sonido()". Y, si bien esto podría tener sentido en la vida real, en el contexto de un programa puede confundir. ¿Qué es eso de querer saber cuántas patas tiene el animal? ¿O por qué me interesa hacer que el animal emita un sonido (ladre, maúlle, relinche, etc.)?

El problema de este ejemplo suele venir cuando se lo explica aislado, sin el contexto de un sistema. Pero si pensamos en un caso donde el programa requiera un animal, o un gato o un perro, entonces las piezas empiezan a encajar.

{% include youtubePlayer.html id="tgfEfSAvyiw" %}
