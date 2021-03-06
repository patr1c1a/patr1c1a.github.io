---
layout: post
title: Ejercicios básicos en Python, usando GUI
date: 2019-02-25 19:00:00
categories: ejercicios python
tags: resolución_problemas algoritmos python
published: true
---

A continuación se encuentra una serie de ejercicios básicos de programación, incluidos dentro de pequeños programas de ejemplo.
Es el mismo tipo de ejercicios que podrían resolverse en consola, pero con interfaces gráficas simples.

El lenguaje de base es Python 3, con el framework TkInter para las interfaces gráficas ("GUI"). TkInter se incluye con la instalación de Python, por lo que no debería ser necesaria su instalación por separado. Para verificar que funciona correctamente, abrir una consola o terminal y ejecutar el siguiente comando:
> python -m tkinter

Cada uno de los ejercicios consta de dos archivos (disponibles en un único archivo comprimido): **programa.py** y **operaciones.py**. El primero (programa.py) no debe ser modificado, ya que contiene el código que controla las propiedades de la vista.

**Para la resolución de cada ejercicio, descargar el archivo correspondiente y descomprimir *programa.py* y *operaciones.py* en la misma carpeta. A continuación, abrir *operaciones.py* y completar el código de acuerdo a la consigna. Finalmente, ejecutar programa.py.**


### 1
Dadas las variables a = 186 y b = 24, escribí las instrucciones necesarias para obtener el resultado de su suma, su resta, su multiplicación, el cociente, el cociente entero y el resto de la división entre a y b.

[Descargar el archivo]({{ site.url }}/assets/tp1-ej5_GUI.zip)


### 2
Utilizá las operaciones matemáticas más apropiada para obtener, del número 16823,
<br>a) Sólo el último dígito (el 3)
<br>b) Los dos últimos dígitos (el 23)
<br>c) Los 3 últimos dígitos (el 823)
<br>d) Todos los dígitos, excepto el último (1682)
<br>e) El primer dígito (el 1)
<br>f) Los dos primeros dígitos (el 16)

[Descargar el archivo]({{ site.url }}/assets/tp1-ej7_GUI.zip)


### 3
Dadas las variables str1 = "Juan" y str2 = "Pérez", ¿cómo harías para mostrar...
<br>a) Las dos cadenas concatenadas, mostrando apellido y nombre? Ejemplo: "Pérez Juan"
<br>b) Las dos cadenas concatenadas pero separadas por ", "? Ejemplo: "Pérez, Juan"
<br>c) nombre y apellido
<br>d) "¡Bienvenido, Juan Pérez!"

[Descargar el archivo]({{ site.url }}/assets/tp1-ej11_GUI.zip)


### 4
Teniendo las siguientes variables:
<br>\>>> cadena1 = "¡Bienvenidos!"
<br>\>>> cadena2 = " esto es"
<br>\>>> cadena3 = " IPI"
<br>\>>> cadena4 = " lo más divertido"
<br>\>>> cadena5 = " de primer año"
<br>\>>> cadena6 = " ..."
Resolver:
<br>a) Construir la cadena "Bienvenidos esto es de primer año lo más divertido... IPI".
<br>b) ¿En qué posición de la cadena anterior está la palabra "primer"?
<br>c) Buscar la primera posición en que aparece la letra "e" en cadena1.
<br>d) Si buscás la letra "n" en cadena1, ¿qué resultado dará? ¿Por qué?
<br>e) Obtener True o False para saber si cadena6 contiene espacios.
<br>f) ¿Qué resultado se obtiene al buscar la letra "d" en cadena4[:6]? ¿Por qué?
<br>g) ¿Cuántos espacios tiene la cadena construida en el punto a?

[Descargar el archivo]({{ site.url }}/assets/tp1-ej12_GUI.zip)


### 5
Si tenemos la cadena texto = 'No sé bien qué día es hoy', indicá cómo obtener:
<br>a) La cadena 'qué día' a partir de la variable texto.
<br>b) Los primeros 5 caracteres de texto.
<br>c) Los últimos 5 caracteres de texto.
<br>d) Los caracteres ubicados en las posiciones pares de texto.
<br>e) La cadena 'ye né' a partir de texto.
<br>f) Cuántas ocurrencias de la letra 'e' existen en texto (incluir la 'e' con y sin acentos)

[Descargar el archivo]({{ site.url }}/assets/tp1-ej17_GUI.zip)


### 6
Dadas las cadenas:
<br>a = '  Python es un lenguaje amigable para empezar a aprender programación   '
<br>b = '        nociones básicas de  '
<br>a) ¿Cuál es la longitud de la cadena a?
<br>b) ¿En qué posición se encuentra  la palabra 'amigable'?
<br>c) ¿Cómo harías para obtener una rebanada de la cadena a que contenga la palabra "Programación" (con la "p" en mayúscula)
<br>d) ¿Cómo harías para eliminar los blancos a izquierda y derecha de b?
<br>e) ¿Cómo harías para armar la expresión 'Python es un lenguaje amigable para empezar a aprender nociones básicas de programación'?
<br>f) Convertí la cadena 'amigable' a mayúsculas y cambiala en la expresión del punto e). Deberá quedar: 'Python es un lenguaje AMIGABLE para empezar a aprender nociones básicas de programación'

[Descargar el archivo]({{ site.url }}/assets/tp1-ej19_GUI.zip)
