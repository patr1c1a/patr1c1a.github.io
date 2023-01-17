---
layout: post
title: Entornos virtuales en Python
date: 2021-06-17 12:00:00
categories: python
tags: venv
published: true
---

¿Sabías que Python permite instalar distintas versiones de módulos/paquetes para cada proyecto? Esto se logra con los entornos virtuales 😉.

Un detalle más: si usamos bash en Windows (por ejemplo, desde Git Bash o la terminal de VSCode) es posible que, para activar nuestro entorno virtual, debamos poner el comando con un punto y un espacio delante: `. mi_entorno/Scripts/activate`

. mi_entorno/Scripts/activate

![venv, entornos virtuales]({{ site.url }}/assets/2021-06-20-python-venv.png)

{% include accesibilidad.html %}
Entornos virtuales en Python

Se trata de una herramienta que permite instalar módulos o paquetes en versiones específicas para cada proyecto, evitando así instalarlos de forma general para todos.

De esta forma, si el proyecto "A" necesita la versión 2.4 de determinado paquete pero el proyecto "B" necesita la 2.5, cada uno puede usar la versión del paquete que requiere, en su propio entorno aislado.

Una vez activo el entorno, los paquetes se instalan normalmente, con pip install <paquete>.
 
Comandos:

`venv` viene incluido en la instalación de Python 3.

Crear entorno virtual "mi_entorno" en el directorio actual: `python -m venv mi_entorno`

Activar "mi_entorno" para empezar a trabajar en él:
- UNIX / MAC: `source mi_entorno/Scripts/activate`
- WINDOWS CMD: `mi_entorno\Scripts\activate.bat`

  
Listar paquetes instalados en el entorno activo:
`pip list`

Desactivar el entorno (para dejar de usarlo):
`deactivate`
</div></details>
<hr />
