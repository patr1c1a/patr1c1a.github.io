---
layout: post
title: POO - ¿cómo diseñarías estas clases?
date: 2025-06-22 09:00:00 -0300
categories: poo
tags: modelado clases
published: true
---

En este ejercicio podríamos pensar diferentes formas de modelar las clases, que dependerán de cada caso y de la información que se necesite manejar de cada una.

El Viaje probablemente necesite saber qué auto lo realizó, y el Auto podría también conocer sus viajes, pero no es obligatorio si ya existe un gestor (Flota). En esto podríamos aplicar el principio de responsabilidad única ("SRP" o "Single Responsibility Principle"), al determinar que el Auto no es responsable de registrar viajes, porque la Flota (o podría ser "la empresa") es quien organiza y gestiona. Esto nos ayuda a tener una baja dependencia entre objetos, porque el Auto no necesita saber quién lo gestiona ni qué hace con él.

De un Auto podríamos tener atributos como: patente, marca, modelo. Mientras que de un Viaje podríamos querer conocer cosas como el Auto que lo hizo, distancia, duración, fecha, etc. Y la Flota, por ser la entidad gestora del sistema, podría tener como atributos a los autos (lista de objetos Auto) y viajes (lista de objetos Viaje).

![POO - Modelado de clases]({{ site.url }}/assets/2025-06-22-ejercicio-poo.png)


&nbsp;

{% include accesibilidad.html %}

POO: ¿cómo diseñarías estas clases?

Queremos llevar el registro de viajes realizados por autos de una flota. Cada viaje tiene una distancia y una duración. Debemos poder calcular la velocidad promedio de un viaje.
¿Cómo distribuirías las responsabilidades?

Errores comunes: 
- Colocar método calcular_velocidad_promedio() en la clase Auto. La velocidad es parte del viaje, no del auto.
- Incluir un atributo Viaje en el objeto Auto. Un auto no tiene un viaje, sino que participa en muchos.

Buen diseño de clases:
- Auto: representa solo al vehículo.
- Viaje: conoce distancia, duración y el auto que lo realizó. Puede calcular la velocidad promedio.
- Flota: gestiona los viajes y los autos (tiene una lista de cada cosa).

Así se reduce el acoplamiento, aumenta la cohesión y se centraliza el control en la clase que tiene sentido que coordine a las demás (la Flota).


</div></details>
<br />&nbsp;
<hr />
