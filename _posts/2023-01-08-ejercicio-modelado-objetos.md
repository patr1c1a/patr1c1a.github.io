---
layout: post
title: Ejercicio de modelado de objetos, con UML
date: 2023-01-08 20:00:00 -0300
categories: ejercicios poo
tags: uml objetos
published: true
---

El modelado de clases con UML es útil para representar diseños orientados a objetos. Y estos diseños pueden tener distintas interpretaciones o soluciones alternativas, dependiendo de las necesidades. ¿Se te ocurre alguna forma diferente de modelar este ejercicio?

![Ejercicio de modelado de objetos, con UML]({{ site.url }}/assets/2023-01-08-ejercicio-modelado-objetos.png)



&nbsp;

{% include accesibilidad.html %}

EJERCICIO: modelado de objetos

Crear un modelo de clases para una aplicación que permite solicitar viajes en coche. De cada viaje se conoce: fecha, punto de inicio (dirección donde recoger al pasajero), punto de llegada y pago. El pago tiene un monto y una o más formas, que pueden ser: tarjeta de crédito, efectivo o billetera virtual.

Resolución:

Clase: Viaje. Atributos privados: fecha (tipo Date), inicio (tipo String), llegada (tipo String), pago (tipo Pago). Métodos públicos: reservarViaje (parámetro: pago de tipo arreglo de Pago; retorna bool); cancelarViaje (retorna bool); iniciarViaje (retorna bool); finalizarViaje (retorna bool).

Clase: Pago (abstracta). Atributo privado: monto (tipo Double).

Clase: Efectivo. Hereda de Pago.

Clase: Tarjeta. Hereda de Pago. Atributos privados: tipo (tipo String), titular (tipo String), numero (tipo long), codigo (tipo int), vencimiento (tipo Date).

Clase: BilleteraVirtual. Hereda de Pago. Atributos privados: tipo (tipo String), titular (tipo String), cvu (tipo long).

</div></details>




<hr />
