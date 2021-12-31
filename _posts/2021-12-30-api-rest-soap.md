---
layout: post
title: APIs REST vs. SOAP
date: 2021-12-30 12:00:00
categories: conceptos
tags: api rest soap
published: true
---


Sé que he estado un tiempo sin publicar pero no quería despedir el año sin compartirles algún nuevo material ☺.

Aquí, un pequeño resumen sobre APIs REST y SOAP. Estas no son las únicas formas de construir una API, pero sí dos de las más populares. Aunque REST sea la que ha ganado más terreno, existen aún muchas APIs SOAP.

![APIs REST y SOAP]({{ site.url }}/assets/2021-12-30-api-rest-soap.png)


{% include accesibilidad.html %}
APIs: REST vs. SOAP

Ambos permiten la transmisión de datos en internet, algo fundamental para construir aplicaciones web.

REST:

PRINCIPIOS:

Arquitectura cliente-servidor.

El servidor no guarda el estado.

Posibilidad de guardar datos en cache.

Separación en capas, con responsabilidades separadas.

Interfaz uniforme.

Otras caracteristicas:

Corre sobre HTTP.

La información se presenta como «recursos» (llamados «endpoints») accesibles mediante una URI.

Usualmente retorna la información en formato JSON, pero puede usar otros.

Más liviano que SOAP.


SOAP:

Independiente del lenguaje.

Adopta principios ACID: «atomicidad», «consistencia», «aislamiento», «durabilidad».

Mayores niveles de seguridad.

No permite cache.

Puede operar sobre distintos protocolos: HTTP, SMTP, TCP, UDP.

La información se retorna como XML.

Mientras que REST se construye en base a los datos (recursos), SOAP se construye en base a funcionalidad.

Requiere más ancho de banda que REST.
</div></details>
<hr />
