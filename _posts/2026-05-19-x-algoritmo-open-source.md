---
layout: post
title: X (Twitter) publicó su algoritmo
date: 2026-05-19 16:00:00
categories: otros
tags: twitter open_source
published: true
---

![X publicó su algoritmo]({{ site.url }}/assets/2026-05-19-x-algoritmo-open-source.png){: width="40%" }

## Ya podemos ver el código fuente del "Para ti"

X publicó parte del código de su sistema de recomendaciones y hay detalles técnicos bastante interesantes cuando lo miramos más de cerca.

Por ejemplo:

• el "feed" no se genera en un único paso, sino en varias etapas de filtrado y puntuación.
• hay mecanismos para evitar que una sola cuenta domine todo el contenido que se muestra.
• el sistema diferencia contenido de cuentas seguidas y cuentas no seguidas.
• algunas señales negativas (como bloquear o reportar) tienen un tratamiento especial dentro del algoritmo.
• y varias partes sensibles quedaron fuera del código publicado por "razones de seguridad".

También faltan componentes importantes como:

- moderación,
- sistema de anuncios,
- parámetros internos,
- y algunos servicios auxiliares.

Es decir: publicaron bastante más de lo que suele mostrar una red social grande… pero claramente no todo.

## Lo que más importa (según el código)

- Responder pesa mucho más que dar "me gusta",
- Bloquear/reportar afecta muchísimo,
- El algoritmo mide cuánto tiempo miramos algo.

Y además se usan modelos de IA para predecir la probabilidad de que interactúes con cada publicación.

## El "transformer" detrás de todo

El sistema incluye un modelo tipo “transformer”: una IA que analiza patrones de comportamiento para estimar qué publicaciones probablemente le interesen a cada usuario.

## ¿Por qué esto importa?

Es código real de un sistema de recomendación a gran escala.

Muchos imaginan “el algoritmo” como magia. Pero al final: son datos, probabilidades y muchísimo código.

[El código puede verse en Github](https://github.com/xai-org/x-algorithm){:target="_blank"}
