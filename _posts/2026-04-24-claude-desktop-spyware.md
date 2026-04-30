---
layout: post
title: El "spyware" de Claude Desktop para Mac
date: 2026-04-24 16:00:00
categories: ia
tags: ia claude mac
published: true
---

![Claude Desktop spyware]({{ site.url }}/assets/2026-04-24-anthropic-spyware.png)

Si instalaste Claude Desktop en tu Mac, también se instaló una puerta de acceso en tu navegador (sin preguntar, sin avisar, sin que pudieras decir que no).

Se llama "Native Messaging": un mecanismo que permite que una extensión del navegador ejecute programas en tu computadora, fuera de la protección del navegador. Anthropic dejó pre-configurada esta conexión para 7 navegadores (Chrome, Brave, Edge, Arc, Opera, Vivaldi, Chromium), aunque no los tengas en tu máquina.

## ¿Qué es exactamente?

Se trata de un archivo JSON + un binario.

Lo que hace es autorizar a tres extensiones específicas a activar una puerta de acceso, permitiendo acceder a la máquina incluso por fuera del _sandbox_ del navegador.

Una es la extensión oficial de Anthropic: la misma que ellos admiten es vulnerable a ataques de tipo _prompt injection_ en el ~11% de los casos, incluso con sus defensas activadas. Si algún software malicioso engaña a esa extensión, podría obtener acceso directo a tu máquina.

## Cómo saber si está instaldo en tu máquina

Si usas Mac y nunca instalaste una extensión de navegador de Anthropic, busca este archivo: `com.anthropic.claude_browser_extension.json`. Si está ahí, fue puesto sin tu consentimiento.

"¿Y si simplemente borro los archivos?". Pues no, porque Claude Desktop los regenera.

En Windows el mecanismo es diferente (usa el registro), pero el comportamiento probablemente sea similar. Linux no tiene Claude Desktop, así que no aplica.

## Fuentes

- [Reporte de Alexander Hanff (experto en seguridad que descubrió el problema)](https://www.thatprivacyguy.com/blog/anthropic-spyware/){:target="_blank"}
- [Sobre la seguridad de la extensión](https://claude.com/blog/claude-for-chrome){:target="_blank"}
