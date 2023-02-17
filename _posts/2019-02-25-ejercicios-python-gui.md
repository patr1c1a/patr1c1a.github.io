---
layout: post
title: Ejercicios básicos en Python, usando interfaz gráfica
date: 2019-02-25 19:00:00
categories: ejercicios python
tags: gui algoritmos python tkinter principiantes
published: true
---

A continuación se encuentra una serie de ejercicios básicos de programación, incluidos dentro de pequeños programas.
Es el mismo tipo de ejercicios que podrían resolverse en consola, pero con interfaces gráficas simples.

El lenguaje de base es Python 3, con el framework Tkinter para las interfaces gráficas ("GUI"). Tkinter se incluye con la instalación de Python, por lo que no debería ser necesaria su instalación por separado. Para verificar que funciona correctamente, abrir una consola o terminal y ejecutar el siguiente comando:
> python -m tkinter

Cada uno de los ejercicios consta de dos archivos (incluidos en un único archivo comprimido): **programa.py** y **operaciones.py**. El primero (programa.py) no debe ser modificado, ya que contiene el código que controla las propiedades de la interfaz gráfica.

**Para la resolución de cada ejercicio, descargar el archivo correspondiente y descomprimir *programa.py* y *operaciones.py* en la misma carpeta. A continuación, abrir *operaciones.py* y completar el código de acuerdo a la consigna. Finalmente, ejecutar programa.py, lo cual puede hacerse desde una terminal, usando el comando *python programa.py* (o reemplazar *python* por el comando que usemos en nuestra máquina para ejecutar el intérprete). La interfaz gráfica interactiva permitirá visualizar el resultado de los ejercicios.**


### 1
Dadas las variables a = 41 y b = 5, escribí las instrucciones necesarias para obtener el resultado de su suma, su resta, su multiplicación, el cociente, el cociente entero y el resto de la división entre a y b.

[Descargar el archivo]({{ site.url }}/assets/ejercicios-python-gui_01.zip)


### 2
Utilizá las operaciones matemáticas más apropiada para obtener, del número 25849 almacenado en la variable num:
<br>a) Solo el último dígito (9)
<br>b) Los dos últimos dígitos (49)
<br>c) Los 3 últimos dígitos (849)
<br>d) Todos los dígitos, excepto el último (2584)
<br>e) El primer dígito (2)
<br>f) Los dos primeros dígitos (25)

[Descargar el archivo]({{ site.url }}/assets/ejercicios-python-gui_02.zip)


### 3
Dadas las variables *nombre = "Francisco"* y *apellido = "Gimenez"*, ¿cómo harías para mostrarlas de las siguientes formas?
<br>a) Las dos cadenas concatenadas, apellido y nombre, separadas por un espacio. Ejemplo: "Gimenez Francisco"
<br>b) Las dos cadenas concatenadas y separadas por ", ". Ejemplo: "Gimenez, Francisco"
<br>c) La frase "¡Bienvenido, Francisco Gimenez!" (usando los valores de las variables *nombre* y *apellido*)
<br>d) Nombre y apellido, separados por un espacio y completamente en mayúsculas. Ejemplo: "FRANCISCO GIMENEZ"

[Descargar el archivo]({{ site.url }}/assets/ejercicios-python-gui_03.zip)


### 4
Teniendo las siguientes variables:
<br>cadena1 = "El que lee"
<br>cadena2 = " mucho"
<br>cadena3 = " y anda mucho,"
<br>cadena4 = " y sabe mucho."
<br>cadena5 = " ve mucho"
<br>cadena6 = "Esta es una frase de Don Quijote"

Resolver:
<br>a) Construir la cadena "frase de Don Quijote: El que lee mucho y anda mucho, ve mucho y sabe mucho." a partir de las variables dadas.
<br>b) ¿En qué posición de la cadena anterior está la palabra "anda"?
<br>c) Usar una operación que de como resultado la primera posición en que aparece la letra "e" en cadena1.
<br>d) Usar una operación que de como resultado "DON QUIJOTE" a partir de cadena6.
<br>e) Obtener True o False (o bien 1 o 0) para saber si cadena2 contiene algún espacio.
<br>f) Usar una operación que de como resultado la posición de "o" en cadena4[:6] y observar qué sucede al no encontrarla.
<br>g) Mostrar cuántos espacios tiene la cadena construida en el inciso a.

[Descargar el archivo]({{ site.url }}/assets/ejercicios-python-gui_04.zip)


### 5
Si tenemos la cadena frase='Hasta la persona más pequeña puede cambiar el curso del futuro', indicá operaciones para obtener:
<br>a) La cadena 'más pequeña' a partir de la variable frase.
<br>b) Los primeros 5 caracteres de frase.
<br>c) Los últimos 6 caracteres de frase.
<br>d) Los caracteres ubicados en las posiciones pares de frase.
<br>e) La cadena 'o repra' a partir de frase leída en forma inversa.
<br>f) Cuántas ocurrencias de la letra 'a' existen en frase (incluir la 'a' con y sin acentos)

[Descargar el archivo]({{ site.url }}/assets/ejercicios-python-gui_05.zip)


### 6
Dadas las cadenas:
<br>str1 = '   Quizá haya enemigos de mis opiniones,    '
<br>str2 = ' pero yo mismo  puedo ser también enemigo de mis opiniones.  '
<br>str3 = ', si espero un rato,'
<br>a) Mostrar el carácter que se encuentra en la posición 7 de cada cadena, separados por un espacio.
<br>b) Usar una operación que obtenga el carácter que se encuentra en la última posición de str3.
<br>c) Eliminar los blancos a izquierda y derecha de str1.
<br>d) Obtener una rebanada de str1 que contenga la palabra "quizá" (con la "q" en minúscula), al mismo tiempo que se eliminan los espacios en blanco a la izquierda.
<br>e) Armar la expresión 'Quizá haya enemigos de mis opiniones, pero yo mismo, si espero un rato, puedo ser también enemigo de mis opiniones.'
<br>f) Obtener el texto 'si espero UN RATO' a partir de str3.

[Descargar el archivo]({{ site.url }}/assets/ejercicios-python-gui_06.zip)
