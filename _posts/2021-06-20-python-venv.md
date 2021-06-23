---
layout: post
title: Entornos virtuales en Python
date: 2021-06-17 12:00:00
categories: python
tags: venv
published: true
---

¿Sabías que Python permite instalar distintas versiones de módulos/paquetes para cada proyecto? Esto se logra con los entornos virtuales  😉.

![venv, entornos virtuales]({{ site.url }}/assets/2021-06-20-python-venv.png)
<hr />
<br />&nbsp;
Versión accesible (apta para lectores electrónicos):

> Entornos virtuales en Python
> Se trata de una herramienta que permite instalar módulos o paquetes en versiones específicas para cada proyecto, evitando así instalarlos de forma general para todos.
> De esta forma, si el proyecto "A" necesita la versión 2.4 de determinado paquete pero el proyecto "B" necesita la 2.5, cada uno puede usar la versión del paquete que requiere, en su propio entorno aislado.
> Una vez activo el entorno, los paquetes se instalan normalmente, con pip install <paquete>
> Comandos:
> Instalación de la herramienta:
> pip install virtualenv
> Crear entorno virtual "mi_entorno" en el directorio actual:
> python -m venv mi_entorno
> Activar "mi_entorno" para empezar a trabajar en él:
> UNIX / MAC: source mi_entorno/Scripts/activate
> Listar paquetes instalados en el entorno activo:
> pip list
> Desactivar el entorno (para dejar de usarlo):
> deactivate

