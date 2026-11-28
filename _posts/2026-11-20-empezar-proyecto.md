---
layout: post
title: Cómo empezar tu proyecto de software cuando no sabés por dónde
date: 2026-11-20 20:00:00
categories: arquitectura
tags: proyecto portfolio
published: true
---

[![Cómo empezar tu proyecto de software]({{ site.url }}/assets/2026-11-20-empezar-proyecto.png){: width="40%" }]({{ site.url }}/assets/2026-11-20-empezar-proyecto.png){: .thickbox title="Cómo empezar tu proyecto de software" }

## Paso 1: Definir qué vas a construir

Qué problema resuelve tu proyecto, quién será el usuario, qué necesita hacer ese usuario.

**Ejemplo:** "Quiero una aplicación web para registrar mis gastos personales, clasificarlos por categoría y consultar cuánto gasté en cada mes."

## Paso 2: Describir las funcionalidades en lenguaje natural

Explicá las funcionalidades que debe tener el proyecto y cómo debe comportarse cada una, tanto en situaciones habituales como cuando algo no sale según lo esperado.

**Ejemplo:** Para registrar un gasto el usuario ingresa importe, fecha, categoría y descripción. El importe acepta decimales y debe ser mayor que cero. La categoría debe existir previamente. Se permite ingresar un gasto sin descripción. Se deben rechazar gastos sin fecha, importe o categoría.

## Paso 3. Identificar qué puede condicionar la implementación

* **Presupuesto:** ¿cuánto puedo pagar en servicios y herramientas?
* **Infraestructura:** ¿dónde se ejecutará cada parte?
* **Datos:** ¿qué guardo, dónde y por cuánto tiempo?
* **Usuarios:** ¿hay autenticación? ¿datos sensibles?
* **Dependencias externas:** ¿consumo APIs o servicios de terceros?
* **Mantenimiento:** ¿quién actualiza y mantiene el proyecto?

## Paso 4. Usar IA para revisar la planificación antes de escribir código

Pedile que:

* Te haga preguntas sobre el proyecto.
* Detecte requisitos ambiguos o incompletos y casos límite que no contemplaste.
* Detecte conflictos con tus restricciones y riesgos de seguridad.
* Proponga alternativas técnicas con sus ventajas y desventajas.
* Sugiera una arquitectura y un plan de implementación.

El resultado de estos 4 pasos es tu guía para construir el proyecto.

## Conclusiones

Es tentador escribir una idea general en Codex o Claude Code y pedirle que construya una aplicación. Pero eso deja lugar a que sea la IA quien tome las decisiones faltantes y a que después tengamos que invertir tiempo y tokens en corregir el rumbo. Sí, podemos pedirle que se detenga y nos pregunte cuando falte definir algo, pero entonces estaremos decidiendo a medida que construimos, y eso impide ver "el panorama completo" y detectar inconsistencias antes de empezar.

Si no sabés qué decisión técnica es más conveniente, podés pedirle a la IA que compare alternativas y explique sus consecuencias, pero es importante que seas vos quien decide y que tengas en claro por qué se usa cada cosa. Además, una decisión técnicamente correcta no necesariamente será la mejor para tu proyecto. Si es un proyecto que vas a "deployar" (es decir, ponerlo en funcionamiento para acceder a él, normalmente a través de internet), tendrás que tener en cuenta los costos y los límites de cada servicio (aunque uses servicios gratuitos).

El documento que construyas con el resultado de los 4 pasos de esta publicación es lo que normalmente se llama "especificación". Pero esa especificación inicial es una guía, no un contrato inmutable. A medida que probás el proyecto, podés descubrir requisitos que no habías contemplado. En esos casos, actualizás las especificaciones y continuás trabajando.
