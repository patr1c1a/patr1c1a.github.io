---
layout: post
title: ¿Cuándo se instancian los objetos?
date: 2026-02-17 16:00:00
categories: poo
tags: clases instancias objetos poo
published: true
---

A todos nos pasa: cuando nos empiezan a explicar que una clase es un "molde" y de ahí salen los objetos, nos imaginamos que inmediatamente esos objetos existen en el sistema. Pero, en sistemas complejos y con muchas partes, no todo objeto existe "desde siempre".

Algunos objetos están desde que el sistema se inicia. Por ejemplo, en un editor de texto tipo "Word" o "LibreOffice Writer" podríamos pensar en el menú principal, el documento actual, el área de texto, el historial de cambios... Que necesitan estar cargados desde el inicio para que el programa funcione.

Pero otros objetos se crean solo cuando se los necesita. Siguiendo el ejemplo del editor de texto, podría ser algún objeto "GuardadoEnProceso" que contiene los datos cuando se inicia la operación de guardar. Antes de empezar a guardar, no tendría sentido que eso existiera. O cuando vamos a buscar texto dentro del documento podría generarse un objeto "Busqueda" que solo tiene razón de ser cuando se está buscando algo, y en otras situaciones no existe.

¿Se te ocurren otros ejemplos?

{% include youtubePlayer.html id="yJBa1uWCGiM" %}
