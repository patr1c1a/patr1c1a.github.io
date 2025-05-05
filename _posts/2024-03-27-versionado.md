---
layout: post
title: Versionado del software
date: 2024-03-27 21:00:00 -0300
categories: conceptos otros
tags: versionado major minor patch
published: true
---

Asignar de forma correcta y ordenada un número de versión a nuestro software es crucial para controlar actualizaciones, coordinar desarrolladores y permitir a usuarios migrar entre versiones.

El método de versionado más común es el ["versionado semántico", cuya especificación puede verse aquí](https://semver.org/lang/es/){:target="_blank"}.

![Versionado de software]({{ site.url }}/assets/2024-03-27-versionado.png)


&nbsp;

{% include accesibilidad.html %}

Versionado del software

Sirve para hacer seguimiento de cambios en el código, mediante números de versión.

Formato más usual: `mayor.menor.parche` (ejemplo: `1.6.2`).

Este formato se llama "versionado semántico".

- "Mayor": Cambio importante que puede romper la compatibilidad.
- "Menor": Nueva funcionalidad agregada.
- "Parche": Correcciones de errores o mejoras menores.

Por qué es importante un buen versionado:

- Permite controlar y documentar los cambios y nuevas funcionalidades.
- Facilita volver a una versión anterior si se introducen errores.
- Ayuda a coordinar el trabajo de los desarrolladores.
- Posibilita producir actualizaciones periódicas de forma organizada.
- Permite a los usuarios actualizarse a las últimas versiones.

Algunas buenas prácticas:

- Seguir un esquema de versionado coherente.
- Documentar bien los cambios en cada nueva versión.
- Mantener compatibilidad hacia atrás en la misma versión mayor.
- Usar un sistema de control de versiones (ejemplo: Git).

</div></details>
<br />&nbsp;

<hr />
