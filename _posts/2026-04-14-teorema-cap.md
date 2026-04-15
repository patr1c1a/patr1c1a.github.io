---
layout: post
title: Consistencia vs. Disponibilidad en "CAP"
date: 2026-04-14 16:00:00
categories: design
tags: system_design teorema_cap consistencia disponibilidad
published: true
---

En diseño de sistemas hay decisiones que definen el comportamiento completo de la aplicación.

Queda el último ticket para un concierto y dos personas intentan comprarlo al mismo tiempo. El sistema está distribuido en varios servidores y cada usuario está en un servidor diferente. Pero hay un problema: los servidores pierden conexión entre sí y entonces cada uno cree que todavía queda 1 ticket. ¿Qué harías?

- Opción 1: bloqueás la compra hasta que los servidores se pongan de acuerdo.
- Opción 2: dejás que ambos compren… pero vendés el mismo ticket dos veces.

Este tipo de situaciones aparecen en sistemas reales, entrevistas técnicas y productos que usamos todos los días.

¿Qué pesa más? ¿Que el sistema responda siempre o que los datos sean siempre correctos?

En este video te explico otro ejemplo de consistencia vs. disponibilidad:

{% include youtubePlayer.html id="mrlwJSWRUg8" %}
