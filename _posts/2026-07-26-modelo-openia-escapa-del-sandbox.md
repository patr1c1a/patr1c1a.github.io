---
layout: post
title: Una IA "escapó" y robó información... ¿Es así?
date: 2026-07-26 16:00:00
categories: ia
tags: openai chatgpt huggingface
published: true
---

![Modelo de OpenAI escapa del sandbox]({{ site.url }}/assets/2026-07-26-modelo-openia-escapa-del-sandbox.png){: width="40%" }

## Qué pasó en realidad

El fin de semana del 11 de julio de 2026, la empresa Hugging Face detectó un ingreso indebido a sus sistemas. Lo curioso es que no lo había hecho un humano sino un agente de inteligencia artificial: provenía de pruebas que estaba llevando adelante OpenAI.

## La prueba de ciberseguridad

OpenAi estaba haciendo ciertas pruebas sobre sus modelos, concretamente unas relacionadas a "benchmarks" de ciberseguridad.

Los modelos estaban dentro de un entorno de pruebas con limitaciones (lo que comúnmente se llama "sandbox"). Pero, para medir la capacidad ofensiva OpenAI decidió desactivar algunas medidas de seguridad que normalmente evitarían que los modelos cometan actividades de alto riesgo.

Entonces, el "sandbox" ya no pudo contener al modelo. Y el modelo tenía un objetivo: pasar la prueba de ciberseguridad que le habían asignado.

## El modelo solo tenía un objetivo

Lo que el modelo buscaba era cumplir el objetivo: pasar la prueba con la mejor puntuación posible. Y puso manos a la obra.

E hizo lo que haría un alumno tramposo: empezó a buscar las respuestas a los desafíos, en lugar de intentar resolverlos por sí solo.

Para eso, buscó cómo salir del sandbox y logró encontrar una vulnerabilidad de tipo "zero-day" que nadie conocía hasta el momento.

Su proceso de razonamiento le llevó a la conclusión de que la empresa Hugging Face probablemente tendría en algún sistema las respuestas a los desafíos que le habían planteado, entonces enfocó ahí sus esfuerzos. Consiguió unas credenciales que le permitían el acceso y finalmente encontró lo que buscaba.

## No intervinieron humanos

Lo novedoso del suceso es que la IA no tuvo ninguna dirección humana para hacer todo esto. Fue una cadena de acciones que ella misma razonó, planificó y ejecutó.

Pero todo era porque buscaba cumplir con el objetivo que le habían dado.

Entonces, ¿las máquinas están buscando liberarse? Esa afirmación me parece digna de cualquier medio sensacionalista, pero no describe de ninguna manera lo que sucedió acá.

---

**Fuentes:**

- [OpenAI](https://openai.com/index/hugging-face-model-evaluation-security-incident/){:target="_blank"}
- [Hugging Face](https://huggingface.co/blog/security-incident-july-2026){:target="_blank"}
