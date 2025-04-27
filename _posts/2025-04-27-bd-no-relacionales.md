---
layout: post
title: Bases de Datos relacionales, conceptos esenciales
date: 2025-04-27 09:00:00 -0300
categories: bd
tags: bd nosql mongodb redis dynamobd neo4j cassandra
published: true
---

Aunque a veces se las llama NoSQL, las bases de datos no relacionales agrupan distintos modelos de organización de datos. Acá te cuento sobre los más usados.

"NoSQL" es el nombre común que se usa para la mayoría de las bases de datos no relacionales modernas, pero originalmente significaba "Not Only SQL" (no solo SQL), porque algunas de esas bases sí permiten hacer consultas tipo SQL o parecidas.


![Bases de Datos no relacionales]({{ site.url }}/assets/2025-04-27-bd-no-relacionales.png)


&nbsp;

{% include accesibilidad.html %}

Bases de datos no relacionales
No organizan los datos en tablas tradicionales de filas y columnas, sino que utilizan otros modelos de organización más flexibles, adaptados a diferentes tipos de datos.

TIPOS PRINCIPALES DE BASES DE DATOS NO RELACIONALES:

- Bases de datos orientadas a documentos: Almacenan información en documentos estructurados (como en formato JSON o BSON). Agrupan los documentos en colecciones. Ejemplo: MongoDB.
- Bases de datos clave-valor: Cada dato se guarda como un par “clave : valor”. Son muy rápidas para buscar datos simples. Ejemplos: Redis, DynamoDB.
- Bases de datos de grafos: Representan los datos mediante nodos y relaciones (aristas). Son ideales para redes sociales, mapas de rutas, etc. Ejemplo: Neo4j.
- Bases de datos orientadas a columnas: Organizan los datos por columnas en lugar de filas. Son eficientes para grandes volúmenes de datos y consultas analíticas. Ejemplo: Apache Cassandra.


</div></details>
<br />&nbsp;
<hr />
