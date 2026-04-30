---
layout: post
title: ¡Claude Code vulnerado!
date: 2026-04-09 16:00:00
categories: ia
tags: claude seguridad
published: true
---

![Claude Code vulnerado]({{ site.url }}/assets/2026-04-09-claude-code-vulnerado.png){: width="40%" }

El 31 de marzo, cuando se lanzaba la versión 2.1.88 de [Claude Code](https://code.claude.com){:target="_blank"}, el usuario de X "Fried_rice" anunció que se había filtrado el código. Eran 512.000 líneas de código en alrededor de 2.000 archivos, conteniendo referencias a funcionalidad deshabilitada, oculta o inactiva.

## Cómo sucedió exactamente

Lo que pasó fue que incluyeron, accidentalmente, un archivo de mapeo que no debía incluirse en el paquete de instalación de Claude Code (que la propia empresa publica en el [registro de npm](https://docs.npmjs.com/cli/v8/using-npm/registry){:target="_blank"}).

Cuando los desarrolladores compilan y preparan el código para producción, usualmente se "empaquetan" y condensan varios archivos. Y por eso se necesita un archivo de "mapeo" que "traduzca" esa versión condensada del código al código fuente original. Pero en este caso el "mapa" no era solo eso: aparentemente contenía también el código completo.

Por si fuera poco, también se incluía la URL de un archivo zip que contenía todo el código fuente con su estructura de carpetas, que estaba ubicado en un "bucket" R2 público de Cloudflare, al que todo internet tenía acceso (aparentemente, configurado así por comodidad del equipo de desarrollo).

## Pero, ¿qué se descubrió en ese código?

Los curiosos no tardaron en indagar en el material filtrado y publicar algunos hallazgos curiosos e interesantes. Algunos de ellos, sobre la manera en que Claude Code funciona. Otros, sobre funcionalidad que no está activa (tal vez porque la empresa está aún desarrollándola o porque fue descartada y quedó obsoleta).

Algunas de las cosas que se descubrieron son:

- Una especie de "mascota" que se llama "Buddy" y funciona con un sistema gacha. Tiene personalidad propia, nombre, especie y rareza. Aparentemente es una especie de "asistente" que podría comentar sobre la conversación.
- El modo "KAIROS / sueño", activo incluso cuando la ventana de Claude Code se cierra. Revisa conversaciones pasadas para mantener una "memoria" entre sesiones y evalúa si necesita hacer alguna acción.
- Hay varios dominios web "pre-aprobados" de los que puede extraer contenido sin límites: AWS, GitHub, MDN, Django... Para los demás sitios hay un máximo de 125 caracteres que puede mostrar.
- Cambiar de modelo en medio de una conversación "mata" la cache de prompts. Esto hace que se gasten más tokens, al haber perdido la información en cache.

## ¿Se filtraron datos de usuarios o datos de entrenamiento del modelo?

El código filtrado es solo la CLI de Claude Code. No se filtraron datos de entrenamiento del LLM, de servidores backend ni información sensible de usuarios.

## Algunos usuarios resguardaron copias del código

Por supuesto, Anthropic hizo retirar el código del dominio público. Pero ya muchos usuarios habían hecho copias. Se pueden encontrar varias aún disponibles, como los repos "[claw-code](https://github.com/ultraworkers/claw-code){:target="_blank"}" del usuario ultraworkers en github, o "[claude-code](https://github.com/yasasbanukaofficial/claude-code/){:target="_blank"}" del usuario yasasbanukaofficial.
