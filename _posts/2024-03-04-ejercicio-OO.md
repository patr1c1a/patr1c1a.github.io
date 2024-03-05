---
layout: post
title: Diseño de objetos - ejercicio básico
date: 2024-03-04 21:00:00 -0300
categories: poo, ejercicios
tags: objetos modelado
published: true
---

El diseño orientado a objetos es un paradigma de programación que organiza el código en unidades reutilizables llamadas "objetos". Aprender a modelar correctamente es importante para aplicar correctamente la programación orientada a objetos, facilitando la reutilización de código y el mantenimiento.

![Ejercicio básico de OO]({{ site.url }}/assets/2024-03-04-ejercicio-OO1.png)
![Ejercicio básico de OO - solución]({{ site.url }}/assets/2024-03-04-ejercicio-OO2.png)


&nbsp;

{% include accesibilidad.html %}

Diseño de objetos - ejercicio básico

Suponiendo un sistema simple para gestionar una biblioteca, identificar:
a) Posibles tipos de objetos involucrados (ej.: libro, socio).
b) Describir algunos "atributos" y "responsabilidades" que podría tener cada uno.
c) ¿Cómo se relacionan esos objetos entre sí? Describir esas relaciones en términos de "tiene" y "usa" (ej.: "un socio usa un libro").

Una posible solución:

Tipos de objetos: libro, socio, estantería, biblioteca.

Atributos:

- Libro: título, autor, año de publicación, ISBN, género, copias disponibles, copias totales.
- Socio: número de socio, nombre, teléfono, email, lista de libros que tomó prestados.
- Estantería: número, ubicación, capacidad, lista de libros que tiene.
- Biblioteca: libros, estanterías, socios.

Responsabilidades:

- Libro: ver detalles, verificar disponibilidad, reservar para un socio.
- Socio: ver detalles, solicitar libro en préstamo, devolver libro, ver libros leídos.
- Estantería: ver libros, agregar libro, eliminar libro.
- Biblioteca: agregar/eliminar libro, agregar/eliminar estantería, agregar/eliminar socio, buscar libro, buscar autor.

Responsabilidades:

- La biblioteca tiene libros.
- La biblioteca tiene estanterías.
- La biblioteca tiene socios.
- Una estantería tiene libros.
- Un socio usa un libro.

</div></details>
<br />&nbsp;

<hr />
