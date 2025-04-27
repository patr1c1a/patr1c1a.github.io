---
layout: post
title: Bases de Datos relacionales, conceptos esenciales
date: 2025-04-16 09:00:00 -0300
categories: bd
tags: bd relacional tabla pk fk
published: true
---

El modelo relacional es un enfoque para organizar y almacenar datos en una base de datos (relacional), representándolos en tablas relacionadas. Entender qué son las entidades, las claves primarias y las claves foráneas es fundamental para construir bases de datos sólidas y bien estructuradas.


![Conceptos de Bases de Datos relacionales]({{ site.url }}/assets/2025-04-26-conceptos-bd.png)


&nbsp;

{% include accesibilidad.html %}

Bases de Datos: conceptos esenciales

ENTIDADES Y TABLAS

- Entidad: un objeto, concepto o evento del que queremos guardar información (ej.: Cliente, Producto, Compra).
- Tabla: representación de entidad en la base de datos (su estructura podría compararse a una hoja de Excel).

FILAS Y COLUMNAS

- Fila (registro): conjunto de datos que describe a un solo caso de la entidad (ej.: si la entidad es Cliente, podrían ser los datos del cliente Juan Perez).
- Columna (campo): una característica de la entidad (ej.: de Cliente podrían ser dni, nombre, email…). Se define con un tipo de dato (int, bool, etc.).

Clave primaria

- Identifica de manera unívoca a cada fila (ej.: un número al que llamamos “Id”). No se repite ni puede estar vacía.

RELACIONES ENTRE TABLAS (clave foránea)

- 1 a 1: un cliente tiene solo un DNI.
- 1 a muchos: un cliente puede hacer muchas compras.
- Muchos a muchos: un estudiante puede tomar muchos cursos y un curso tiene muchos estudiantes (requiere tabla intermedia).


</div></details>
<br />&nbsp;
<hr />
