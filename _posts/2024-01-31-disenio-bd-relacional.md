---
layout: post
title: Diseño de bases de datos relacionales
date: 2024-01-31 13:00:00 -0300
categories: bd
tags: entidades relaciones relacionales bd
published: true
---

¿Cómo se construye la columna vertebral de un sistema informático? Al menos cuando se usan bases de datos relacionales. Tendremos que llevar adelante un análisis detallado para no dejar afuera a ninguno de los elementos esenciales.

![Diseño de BD relacionales]({{ site.url }}/assets/2024-01-31-disenio-bd-relacional.png)


&nbsp;

{% include accesibilidad.html %}

Diseño de bases de datos relacionales

El primer paso es entender los requerimientos: qué hará el sistema, qué datos se necesita modelar, cómo se relacionan, qué campos se requieren y qué tipo de valores aceptan, qué sucede cuando algún dato se elimina, restricciones, etc. Todo esto se traducirá en entidades, atributos, relaciones...

ENTIDAD: Una "cosa" del mundo real, que puede distinguirse de otras. Ej.: paciente, coche, departamento.

ATRIBUTOS: Características de una entidad. Ej.: para Empleado podrían ser: nombre, legajo, ingreso. Un atributo acepta un tipo de valores. Cada entidad se identifica por uno -o un grupo- de atributos ("clave primaria").

RELACIONES: Cuando un atributo de una entidad se vincula con otra entidad. Ej.: Curso con Estudiante. Estos atributos se llaman "clave foránea".

CARDINALIDAD: indica con cuántos objetos se relaciona un atributo. Ej.: suponiendo entidades Jugador y Equipo, donde Equipo tiene un atributo que representa a sus jugadores y solo puede tener entre 5 y 7 jugadores. La cardinalidad puede ser: 1.1 ("uno a uno", donde un objeto de una entidad se relaciona con exactamente un objeto de otra), 1.N ("uno a muchos"), 0.1 ("cero a uno"), 0.N ("cero a muchos"), N.N ("muchos a muchos"). N.N es un caso especial para representar en una base de datos.


</div></details>
<br />&nbsp;

<hr />
