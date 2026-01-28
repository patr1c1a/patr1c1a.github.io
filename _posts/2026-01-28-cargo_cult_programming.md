---
layout: post
title: Cargo Cult Programming, cuidado al copiar código o patrones
date: 2026-01-28 16:00:00
categories: otros
tags: patrones cargo_cult 
published: true
---

En programación, hay situaciones donde copiamos cosas "porque es lo correcto", pero aun así algo no cierra.

Pasa en proyectos personales que crecen, y sobre todo en trabajo en equipo, cuando heredás decisiones que "siempre se hicieron así". Pasa en entrevistas técnicas, cuando te preguntan por qué elegiste cierta solución. Pasa en bugs difíciles, donde un pequeño cambio rompe cosas inesperadas.

En muchos de esos casos pasa algo como esto: usamos código, estructuras, patrones o incluso procesos que no nacieron para nuestro problema, sino que fueron copiados porque venían de un libro, un tutorial o una empresa reconocida.

En el video hablo de este fenómeno y de la pregunta clave que suele faltar cuando programamos así.

**Algunos ejemplos muy comunes:**

- Copiás una estructura de un proyecto con varias capas, interfaces y abstracciones "porque es profesional". El proyecto es chico, pero modificar una función implica tocar cinco archivos. No hay un bug concreto… pero tampoco hay claridad. Ahí no falló el código: falló la decisión de copiar una solución sin preguntarse para qué existía.
- O, en un proyecto grupal, alguien decide que hay que trabajar "como en las empresas grandes" y entonces aparecen procesos, reglas y métricas que no solo entorpecen el trabajo sino que terminan generando fricción, demoras y errores evitables. Y entonces tardan siglos en tener lista una "user story" o contando líneas de código para evaluar si los desarrolladores hicieron un PR "de buena calidad".

En ambos casos, el problema no es el código en sí. Es algo más sutil.

Después de ver el video, suele aparecer una incomodidad interesante, por ejemplo:

- ¿Cómo sé si un patrón o una arquitectura están resolviendo mi problema o solo agregando complejidad?
- ¿En qué punto una “buena práctica” deja de ayudar y empieza a estorbar?

Si alguna de estas situaciones te resulta familiar, te recomiendo ver el video completo antes de sacar conclusiones.

{% include youtubePlayer.html id="52xKt0BgbJg" %}
