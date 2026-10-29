---
layout: post
title: Lo que todo programador debe saber sobre git
date: 2025-08-13 15:00:00 -0300
categories: profesional
tags: git commit pull_request
published: true
---

📌 ¿Te cuesta organizarte con Git cuando trabajás en equipo?

Este es el flujo básico para que puedas clonar, crear ramas, hacer commits y subir cambios sin romper nada. Ideal si estás empezando con Git y necesitas dejar de temerle a los conflictos o al famoso "subí cambios directo a `main` y rompí todo" 😲.

![Lo que todo programador debe saber sobre git]({{ site.url }}/assets/2025-08-13-git-flujo-basico.png)

&nbsp;

{% include accesibilidad.html %}
Lo que todo programador debe saber sobre git

¿Qué es Git? Un sistema de control de versiones que registra cambios en archivos y permite trabajar en equipo sin sobrescribir el trabajo de otros.

Este flujo es para Git en terminal (CLI) y proyectos que usan Pull Requests (PR) para revisión antes de fusionar a main/master.

Este es el flujo básico para programar en equipo:

Antes de empezar: clonar el repositorio remoto con `git clone <url>`. Copia todo el proyecto y su historial a la máquina local.

1. Crear una rama nueva con `git checkout -b <nombre-rama>`. Para trabajar en una tarea sin afectar el código de otros.

2. Agregar los cambios al área de staging con `git add <archivo>` ó `git add .`. Prepara los archivos para el commit.

3. Hacer un commit con `git commit -m "Descripción"`. Guarda un registro de los cambios con un mensaje descriptivo.

4. Enviar la rama al repositorio remoto con `git push origin <nombre-rama>`. Así, otros pueden ver los cambios.

Ahora, todo está listo para crear un "Pull Request" (PR) y que, al fusionar la rama con la principal, los cambios pasen a ella.

</div></details>
<br />&nbsp;
<hr />
