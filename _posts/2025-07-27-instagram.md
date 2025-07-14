---
layout: post
title: ¿Sabías que Instagram empezó con Python?
date: 2025-07-27 15:00:00 -0300
categories: otros
tags: instagram
published: true
---

Incluso las apps más grandes del mundo empezaron con una arquitectura base sencilla y bien diseñada. Antes de soñar con sistemas de millones de usuarios, tenemos que dominar los fundamentos: cómo funcionan los frameworks, las bases de datos, el backend y el procesamiento asíncrono. Es ese conocimiento sólido lo que nos permitirá luego crear proyectos que realmente puedan crecer sin límites.

La arquitectura inicial de Instagram usó un stack simple pero poderoso. Hoy, en Meta, combina sistemas distribuidos avanzados con infraestructura 100% propia.

![Instagram empezó con Python]({{ site.url }}/assets/2025-07-27-instagram.png)


&nbsp;

{% include accesibilidad.html %}

¿Sabías que Instagram empezó con Python? 

Cuando Instagram se creó, en 2010, sus fundadores eligieron Python + Django para el backend.

¿Por qué Python + Django?
- Sintaxis clara y legible → desarrollo rápido.
- Gran comunidad y bibliotecas maduras.
- Django incluye todo para crear apps web seguras: ORM, autenticación, migraciones, administración.

En sus inicios era una arquitectura monolítica con servicios de infraestructura básica de AWS.

- Lenguaje y framework: Python 2.5 (luego 2.7). Django 1.2.5.
- Base de datos: PostgreSQL (Amazon RDS para PostgreSQL, en AWS).
Servidor web y WSGI: Gunicorn como servidor WSGI para correr la app Django. nginx como proxy inverso y servidor de archivos estáticos.
- Frontend: Aplicación iOS escrita en Objective-C (no tenían aplicación Android en el lanzamiento inicial).
- Almacenamiento: Amazon S3 para imágenes.
- Cache: memcached.
- Background tasks: Celery con RabbitMQ como message broker.

Hoy es una arquitectura distribuida, con múltiples lenguajes, buscando rendimiento (C++, Go) y productividad (Python, React), además de otros lenguajes (Kotlin, Swift).

- Frameworks y bibliotecas: Django (con modificaciones propias). - Thrift para RPC. Celery para tareas asíncronas.
- Bases de datos: PostgreSQL (BD principal). Cassandra para escalabilidad horizontal. TAO para consultas de relaciones. Haystack para almacenar imágenes. Memcached y Redis para cache.
- Infraestructura y DevOps: data centers propios de Meta (ya no usan AWS). Load balancers propios. Contenedores basados en cgroups/LXC y orquestación interna. Sistemas de deployment y CI/CD internos.
- Machine Learning / AI: Modelos en PyTorch para feeds, recomendaciones y detección de contenido.


</div></details>
<br />&nbsp;
<hr />
