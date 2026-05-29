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

[Google Threat Intelligence](https://cloud.google.com/blog/topics/threat-intelligence){:target="_blank"} acaba de confirmar algo que muchos veníamos anticipando: un grupo criminal utilizó inteligencia artificial para descubrir una vulnerabilidad de tipo "zero-day" y generar un exploit funcional que incluso burlaba la autenticación de dos factores (2FA).

## ¿Qué pasó?

Criminales usaron IA para:

- Descubrir una vulnerabilidad desconocida,
- Crear código que burlaba el 2FA,
- Preparar un ataque masivo.

Google lo detuvo a tiempo.

El código generado por IA tenía patrones muy claros que la delataban: comentarios educativos excesivos, formato tipo libro de texto y hasta un puntaje CVSS inventado (una alucinación típica de los modelos). Esto nos da una pista de cómo detectar este tipo de código en el futuro.

## ¿Por qué es diferente?

Esta vez la IA no solo ayudó… Descubrió un "zero-day" y generó el exploit completo. Es la primera vez confirmada que criminales lo logran.

Este caso marca un antes y un después: ya no solo hablamos de IA para phishing o automatizar ataques conocidos. Ahora estamos viendo a la IA participando activamente en la creación de nuevas armas cibernéticas.

## ¿Qué es un "Zero-day" o "día cero"?

Es una vulnerabilidad desconocida por el fabricante de software: nadie la ha descubierto aún, por lo tanto no tiene parche. Y es una de las armas más peligrosas en ciberseguridad.

## El juego cambió

- Los zero-day serán más fáciles de crear.
- Herramientas open-source en riesgo.
- La IA acelera tanto el ataque como la defensa.

Como desarrolladores, esto nos obliga a ser más rigurosos que nunca:

- Revisar con atención el código generado por IA,
- No confiar ciegamente en herramientas de IA para lógica crítica,
- Priorizar seguridad en el diseño desde el primer día.

El futuro de la ciberseguridad ya no depende solo de humanos vs humanos… ahora es "humanos + IA" vs "humanos + IA".

[Fuente](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access){:target="_blank"}
