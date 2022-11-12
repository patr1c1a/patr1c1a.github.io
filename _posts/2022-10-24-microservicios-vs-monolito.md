---
layout: post
title: Microservicios vs. monolito
date: 2022-10-24 22:00:00 -0300
categories: conceptos
tags: microservicios monolito
published: true
---

Una de las primeras grandes aplicaciones en usar microservicios fue Netflix, en 2009, cuando notó problemas para mantener la creciente demanda en su arquitectura monolítica. Imaginen una aplicación con tantos usuarios, donde se produjera un bug severo que provocara la interrupción del servicio completo 😨.

Hoy la arquitectura de la mayoría de las grandes aplicaciones está conformada por microservicios que trabajan como módulos independientes y facilitan el mantenimiento, la utilización de integración continua, la ampliación de las funciones, etc.


![Microservicios vs. "monolito"]({{ site.url }}/assets/2022-10-24-microservicios-vs-monolito.png)


{% include accesibilidad.html %}

Microservicios vs. "monolito"

Una aplicación monolítica es una unidad donde todas las partes están en una misma base de código. Es fácil de desarrollar y de testear, y puede haber varias copias de la misma aplicación en distintos servidores. Es una arquitectura ideal para proyectos simples.

Los microservicios son varias aplicaciones interconectadas que se desarrollan de manera independiente. Pueden estar escritas en diversos lenguajes y usar distintas tecnologías. Son más fáciles de desplegar, mantener, actualizar y escalar.

</div></details>




<hr />
