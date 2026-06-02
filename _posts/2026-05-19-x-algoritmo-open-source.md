---
layout: post
title: X (Twitter) publicó su algoritmo
date: 2026-05-19 16:00:00
categories: otros
tags: twitter open_source
published: true
---

![X publicó su algoritmo]({{ site.url }}/assets/2026-05-19-x-algoritmo-open-source.png){: width="40%" }

## Ya podemos ver el código fuente del "Para ti" de la red social X

X decidió publicar parte del código de su sistema de recomendaciones. Ahora que podemos ver el código, hay detalles técnicos bastante interesantes que quedan al descubierto. Por ejemplo:

- el "feed" no se genera en un único paso, sino en varias etapas donde se aplican filtros y puntuaciones.
- hay mecanismos para evitar que alguna cuenta en particular domine todo el contenido que se muestra.
- el sistema diferencia contenido de cuentas seguidas y cuentas no seguidas.
- hay señales negativas (como bloquear o reportar) que reciben un trato especial dentro del algoritmo.

Varias partes sensibles quedaron fuera del código publicado por "razones de seguridad". Y también faltan componentes importantes, como moderación, sistema de anuncios, parámetros internos y algunos servicios auxiliares. Es decir que publicaron bastante más de lo que suele mostrar una red social grande… pero no todo.

## Lo que más importa (según el código) para decidir qué alcance tienen las publicaciones

- Responder pesa mucho más que dar "me gusta",
- Bloquear/reportar afecta muchísimo,
- El algoritmo mide cuánto tiempo miramos algo.

Y además se usan modelos de IA para predecir la probabilidad de que el usuario interactúe con cada publicación.

## El "transformer" detrás de todo

El sistema incluye un modelo tipo "transformer": una IA que analiza patrones de comportamiento para estimar qué publicaciones probablemente le interesen a cada usuario.

## ¿Cuál es la importancia de esto?

Lo que se publicó es código real de un sistema de recomendación a gran escala. Probablemente requiera conocimiento especializado para entenderlo, pero vale la pena "espiar" un poco cómo funciona.

Aunque no entendamos todo, seguramente algo interesante nos va a quedar para aumentar nuestro conocimiento, aunque más no sea una noción de la cantidad de lógica necesaria para que una red social tan grande funcione.

[El código puede verse en Github](https://github.com/xai-org/x-algorithm){:target="_blank"}
