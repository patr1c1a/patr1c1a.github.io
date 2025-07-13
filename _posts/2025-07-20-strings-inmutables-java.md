---
layout: post
title: ¿Por qué los strings son inmutables en Java?
date: 2025-07-20 14:30:00 -0300
categories: java
tags: strings
published: true
---

Entender la inmutabilidad de los Strings en Java ayuda a optimizar memoria y evitar errores al manipularlos.

💡 Guarda esta información para tu repaso de Java y no te olvides de compartirlo con quien esté estudiando este tema.


![Por qué los strings son inmutables en Java]({{ site.url }}/assets/2025-07-20-strings-inmutables-java.png)


&nbsp;

{% include accesibilidad.html %}
¿Por qué los strings son inmutables en Java?

Que un String sea inmutable significa que no se puede cambiar su valor una vez creado. Cualquier operación que parece modificarlo (como reemplazar letras o cambiar a mayúsculas) en realidad crea un nuevo String con el resultado.


```java
String s = "Hola";
s.toUpperCase(); // No cambia s
System.out.println(s); // Imprime "Hola"

s = s.toUpperCase(); // Ahora s apunta al nuevo String "HOLA"
System.out.println(s); // Imprime "HOLA"
```

Java se asegura de que sean inmutables: la clase String es final, no se puede extender. Y su campo interno es final y privado:

```java
private final char value[];
```

Pero, ¿por qué los Strings son inmutables?

- Seguridad: Si un String se usa como contraseña o URL, su valor no puede ser cambiado en otro lugar del programa.
- "Thread safety" (seguridad en multihilo): Como no pueden cambiar, se pueden compartir entre hilos sin causar errores ni necesitar sincronización.
- "String Pooling": Java guarda strings idénticos en un lugar especial de memoria llamado pool de strings para ahorrar espacio. Si fueran mutables, cambiar un string afectaría a todas las variables que compartan ese mismo valor.


</div></details>
<br />&nbsp;
<hr />
