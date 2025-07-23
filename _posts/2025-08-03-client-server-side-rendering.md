---
layout: post
title: Cómo funcionan Client y Server Side Rendering en desarrollo web
date: 2025-08-03 15:00:00 -0300
categories: conceptos
tags: web rendering
published: true
---

🌎 Hoy las páginas web pueden generar su contenido en el servidor o directamente en tu navegador. Este cambio en cómo se construyen aplicaciones web permitió crear experiencias más dinámicas e interactivas, pero también trajo nuevos desafíos para la velocidad y el SEO.

Entender Client Side Rendering y Server Side Rendering es clave para la programación web actual.

![Client y Server Side Rendering en desarrollo web]({{ site.url }}/assets/2025-08-03-client-server-side-rendering.png)


&nbsp;

{% include accesibilidad.html %}

Cómo funcionan Client y Server Side Rendering en desarrollo web

¿Qué significa "renderizar" una página web? Es generar el contenido visible de la página (texto, imágenes, etc.) a partir del código.

Se puede renderizar:
- En el cliente: el contenido se genera en el navegador y el servidor envía archivos estáticos.
- En el servidor: el servidor genera el HTML completo antes de enviarlo al navegador.

Hoy se combinan SSR y CSR para lograr mejor SEO, velocidad y experiencia de usuario.

Client Side Rendering (CSR)
- Todo el contenido se genera en el navegador con JavaScript.
- El servidor envía solo archivos estáticos (HTML mínimo + JS). Ejemplo: aplicaciones creadas con React, Angular o Vue sin SSR.
- La página tarda más en mostrar contenido porque debe esperar a que se cargue y ejecute el JS.

Server Side Rendering (SSR)
- El servidor genera el HTML completo antes de enviarlo al navegador.
- El navegador muestra la página ya lista, sin esperar al JavaScript.
- El JS se usa después para agregar interactividad si es necesario.
- Mayor carga en el servidor (cada visita implica renderizado).

Algunos frameworks están diseñados principalmente para CSR (ejemplo: React sin Next.js). Otros permiten SSR, CSR o híbridos, según cómo se configure el proyecto (Next.js en React, Nuxt.js en Vue, SvelteKit en Svelte).


</div></details>
<br />&nbsp;
<hr />
