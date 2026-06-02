---
layout: post
title: ¿IA creando ataques nuevos?
date: 2026-05-12 16:00:00
categories: ia
tags: google seguridad 
published: true
---

![Zero Day creado por IA]({{ site.url }}/assets/2026-05-12-google-ia-descubre-zero-day.png){: width="40%" }

## ¿La IA ya está ayudando a crear ataques cibernéticos de nueva generación?

[Google Threat Intelligence](https://cloud.google.com/blog/topics/threat-intelligence){:target="_blank"} acaba de confirmar algo que muchos expertos venían anticipando: un grupo criminal utilizó inteligencia artificial para descubrir una vulnerabilidad de tipo "zero-day" y generar un exploit funcional (que incluso burlaba la autenticación de dos factores o "2FA").

## ¿Qué pasó?

Por primera vez se confirma que los atacantes fueron capaces de usar IA para descubrir una vulnerabilidad desconocida, crear código que burle el 2FA y preparar un ataque masivo. Aunque Google lo detuvo a tiempo.

Se pudo saber que el código era generado por IA porque había ciertos patrones que lo delataban, como una excesiva cantidad de comentarios "educativos", un formato tipo "libro de texto" y hasta la inclusión de un puntaje CVSS inventado (esto una alucinación típica de los modelos). Esas son pistas que permiten detectar este tipo de código creado por IA generativa.

## ¿Por qué este caso es diferente?

Esta vez la IA no solo ayudó sino que descubrió un ataque de tipo "zero-day" y generó el exploit completo que los atacantes pensaban usar. Es la primera vez que se confirma algo así.

Por eso este caso marca un antes y un después: ya no solo hablamos de IA para phishing o automatizar ataques conocidos sino que ahora estamos viendo a la IA participando activamente en la creación de nuevas "armas cibernéticas".

## Ataques tipo "Zero-day" o "día cero"

Un ataque se considera de "día cero" cuando la vulnerabilidad es desconocida por el fabricante del software: nadie la ha descubierto aún, por lo tanto no tiene parche posible. Es una de las armas más peligrosas en ciberseguridad.

## El juego cambió

La IA hará a los "zero-day" más fáciles de crear, lo que pone a las herramientas open-source especialmente en riesgo. Aunque la IA acelera tanto el ataque como la defensa. Y, como desarrolladores, esto nos obliga a ser más rigurosos que nunca:

- Revisar con atención el código generado por IA,
- No confiar ciegamente en herramientas de IA para lógica crítica,
- Priorizar seguridad en el diseño desde el primer día.

El futuro de la ciberseguridad ya no depende solo de humanos vs humanos… ahora es "humanos + IA" vs "humanos + IA".

[Fuente](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access){:target="_blank"}
