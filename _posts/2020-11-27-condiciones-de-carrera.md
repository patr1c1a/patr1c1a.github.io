---
layout: post
title: Condiciones de carrera o "race conditions"
date: 2020-11-27 12:00:00
categories: conceptos java
tags: semáforos mutex race
published: true
---

Cuando nuestra aplicación require el uso de "threads" (o "hilos") podemos encontrarnos con el temido problema de las condiciones de carrera. En algunos casos, la depuración del código para encontrar el error puede causarnos muchos dolores de cabeza.

En el siguiente ejemplo es posible observar un código Java donde 3 hilos compiten por acceder a un recurso compartido, arrojando un resultado diferente con cada ejecución del programa.

[Click acá para ver el ejemplo](https://jdoodle.com/a/3pNp){:target="_blank"}.

![Race conditions]({{ site.url }}/assets/2020-11-27-condiciones-de-carrera.png)

{% include accesibilidad.html %}
	
Las condiciones de carrera se producen cuando el resultado de un programa depende de la secuencia en que se ejecuten sus instrucciones.

Suelen darse en aplicaciones multi-hilo, cuando diferentes hilos acceden a un mismo recurso compartido.

Ejemplo:

```
if (x == 7) {
  y = x-1;
}
```

Si otro hilo modifica el valor de x después de haberse ejecutado `if (x == 7)` pero antes de ejecutar `y = x-1`, el valor de y podría no ser 6.

Para lidiar con estos problemas suelen usarse técnicas como los semáforos o la exclusión mutua en una sección crítica de memoria ("mutex"). Pero esto puede traer otros inconvenientes, como el "deadlock" o la inanición.

Concepto de proceso: informalmente, un proceso es un programa en ejecución (un programa podría tener varios procesos, pero se consideran secuencias de ejecución distintas).

Concepto de hilo o "thread": son la unidad más pequeña de utilización de la CPU. Dentro de un proceso, varios hilos pueden compartir recursos y ejecutarse de manera concurrente.

</div></details>

<hr />

### Código de ejemplo:

{% include codeEditor.html id="3pNp?stdin=0&arg=0&rw=1" %}

