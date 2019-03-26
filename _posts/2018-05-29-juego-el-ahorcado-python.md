---
layout: post
title: Juego en terminal - El Ahorcado (Python)
date: 2018-05-29 19:12:00
categories: python
tags: paradigma_imperativo juegos proyectos
published: true
---

# Desafío

El desafío consiste en programar un juego en terminal de texto, utilizando Python 3. Se trata de una versión de "El ahorcado" muy simplificada, apta para principiantes. Se utilizan conceptos como: estructuras de control, entrada/salida de datos, listas, conjuntos.

Primero necesitarás [descargar el archivo](/assets/2018-05-29-juego-el-ahorcado-proyecto.zip). Este archivo contiene dos cosas:
* el desafío, que es un archivo .py para completar (**funciones.py**) con indicaciones para que escribas tu código.
* el programa principal con la estructura planteada (**ahorcado.py**).
* el código de las funciones completo (¡no vale "espiarlo" antes de intentar el desafío!).


## El juego

El juego del ahorcado consiste en tomar una palabra al azar y darle al usuario la posibilidad de que adivine letras hasta completar la palabra. Tiene 6 intentos para arriesgar letras. Por cada letra incorrecta, se resta un intento. Cuando se queda sin intentos, pierde. Si adivina todas las letras, gana. También, en cualquier momento del juego, puede arriesgar la palabra completa y, si la acierta, el juego finaliza y el usuario gana; pero si la palabra es incorrecta el juego finaliza y el usuario pierde.


## Características del programa

El juego comienza mostrando un menú con 3 opciones: cargar palabras, jugar, salir. Es necesario cargar manualmente las palabras a utilizar durante el juego.

Cuando el usuario decide jugar, cuenta con 6 intentos para arriesgar letras. Sólo puede completar la palabra arriesgando letras (no puede arriesgar la palabra completa en cualquier momento).

Si arriesga una letra que ya había arriesgado anteriormente, ese intento no cuenta y se le vuelve a pedir una letra. Cuando el usuario ingresa su opción, si la letra existe en la palabra, se muestra en el lugar correspondiente y se contabiliza como letra ya utilizada. Si la letra no existe en la palabra, se resta un intento, pero también se cuenta a la letra como ya utilizada. Si la letra no existe en la palabra y, además, quedaba un solo intento, el juego termina.

No se distinguen mayúsculas o minúsculas (todas son convertidas a una forma estándar). Se distinguen vocales acentuadas o con diéresis.

El juego termina cuando:
* No quedan más intentos (pierde).
* El usuario acierta todas las letras, una a una (gana).


## Ejecución

Para probar el juego se deben descomprimir los archivos en una misma carpeta y luego ejecutar con Python 3 el programa **ahorcado.py**. Tal como está, el programa utilizará el archivo _funciones.py_, por lo que no se ejecutará correctamente hasta haber completado las funciones faltantes. Para probar el programa completo se debe cambiar, en _ahorcado.py_, la primera línea por lo siguiente:
> from funciones_completo import *


## Código

El código que se provee para completar tiene partes ya resueltas y otras son funciones que se deben implementar. Cada una tiene su documentación. El código existente no debe modificarse.

Sólo se debe agregar el código indicado en el archivo funciones.py.

## Consigna

Completar el programa con las siguientes funciones:

<pre><code>cargarPalabras:
Parámetros: lista
Retorno: lista (con las palabras disponibles para jugar)
Qué hace: En un bucle, solicita al usuario que ingrese palabras y las va agregando a la lista.
Por cada palabra se eliminan los espacios en blanco a izquierda y derecha.
La palabra se pasa a mayúsculas antes de insertarse en la lista.
La carga termina con una condición de corte que se informa al usuario.</code></pre>

<pre><code>progresoDelJuego:
Parámetros: string (palabra en juego), conjunto con las letras ya arriesgadas.
Retorno: string donde las letras adivinadas se muestran y las no adivinadas se reemplazan por el carácter "_".
Qué hace: forma un string donde, por cada letra de la palabra en juego, verifica si esa letra ya fue adivinada. En ese caso la coloca en el string a formar. En caso contrario, coloca un "_".</code></pre>

<pre><code>leerLetra:
Parámetros: conjunto con las letras ya arriesgadas.
Retorno: letra arriesgada.
Qué hace: En un bucle le pide al usuario que ingrese una letra para adivinar.
La letra se convierte a mayúscula porque las palabras están todas en mayúsculas.
También se eliminan los espacios a izquierda y derecha y se continúa sólo si el string leído tiene 1 solo carácter (si es una sola letra).
Si la letra ya había sido ingresada anteriormente, se le informa al usuario y se le vuelve a pedir una letra.
Cuando el usuario ingresa una letra válida, se retorna.</code></pre>

<pre><code>palabraCompleta:
Parámetros:
Retorno: True si ya se adivinaron todas las letras de la palabra en juego, False en caso contrario.
Qué hace: Verifica cada letra de la palabra en juego y retorna False si encuentra una letra que está en la palabra y que no fue arriesgada por el jugador.
Si todas las letras de la palabra en juego fueron arriesgadas por el jugador, entonces retorna True porque el jugador ya adivinó la palabra completa.</code></pre>


### Código a completar

**ahorcado.py (no debe modificarse)**

<pre><code>from funciones import *
listado=[]
while (True):
    print("Seleccionar opción deseada")
    print("1. Cargar palabras")
    print("2. Jugar")
    print("3. Salir")
   opcion=int(input())
   if opcion==1:
       listado=cargarPalabras(listado)
    elif opcion==2:
       letrasAdivinadas=set()
       intentosRestantes=6
       palabra=seleccionarPalabra(listado)
       print("La palabra tiene ", len(palabra), " letras.")
       while intentosRestantes > 0:
           if palabraCompleta(palabra, letrasAdivinadas):
               print("Ganaste!")
               break
           mostrar=progresoDelJuego(palabra, letrasAdivinadas)
           print(mostrar)
           letra=leerLetra(letrasAdivinadas)
           letrasAdivinadas.add(letra)
           if letra not in palabra:
               intentosRestantes-=1
               print("NOP! Intentos restantes: ", intentosRestantes)
           else:
               print("SIP!")
   elif opcion==3:
       break</code></pre>

**funciones.py**

<pre><code>import random
def seleccionarPalabra(listadoPalabras):
    return listadoPalabras[random.randint(0, len(listadoPalabras)-1)]
    
#AGREGAR ACÁ LAS FUNCIONES DE LA CONSIGNA</code></pre>


## Mejoras posibles

El desafío terminado logra un juego con la funcionalidad básica, al que podrían agregársele algunas mejoras. ¿Te animás a investigarlo e implementarlas por tu cuenta?

* Impedir que el juego empiece si no hay palabras cargadas.
* Dar la posibilidad de adivinar la palabra completa en cualquier punto del juego.
* Evitar que se ingresen números o símbolos cuando se adivina una letra.
* Con cada letra adivinada, mostrar el dibujo del ahorcado (con caracteres) según la cantidad de intentos restantes.
* Permitir al usuario elegir el nivel de dificultad. Por ejemplo, para el nivel 1 se usan palabras de hasta 6 letras, para nivel 2 entre 6 y 11 letras, para nivel 3 más de 11 letras.
* Cargar las palabras desde un archivo de texto, en vez de que el usuario las ingrese manualmente.
