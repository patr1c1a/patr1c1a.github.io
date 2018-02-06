---
layout: post
title: Caso práctico - Análisis y resolución de un problema
date: 2015-06-25 19:00:00
categories: ejercicios
published: true
---

El problema a resolver es el siguiente:

> Se debe escribir un programa que procese una secuencia de strings, cada uno de longitud 1 -es decir, caracteres- (estos strings pueden ser: letras mayúsculas, letras minúsculas, dígitos numéricos o símbolos). Los strings se leen de teclado y la lectura finaliza cuando se hayan procesado 50 strings. Al finalizar la lectura de strings, se debe informar por pantalla lo siguiente:
> <br />**a.** Si se ingresó más cantidad de letras mayúsculas que minúsculas o a la inversa. Si la cantidad es igual, también se debe informar. 
> <br />**b.** Cantidad de dígitos numéricos ingresados entre 1 y 8.
> <br />**c.** Cantidad de ocurrencias de cada una de las letras del abecedario (sin importar sin son mayúsculas o minúsculas y sin contar letras acentuadas). Por ejemplo, si la secuencia es: **a, 6, *, ?, A, u, a, 1** la cantidad de ocurrencias de la letra "a" será 3, mientras que la cantidad de ocurrencias de la letra "u" será 1.
> <br />**d. Cuál es la letra que apareció más cantidad de veces (sin importar si es mayúscula o minúscula).


Para poder escribir el código en el lenguaje en que se haya decidido trabajar, se debe hacer un análisis del problema y de las posibles técnicas para resolverlo. Las técnicas pueden depender de las herramientas que provea el lenguaje concreto que se usará, pero hay ciertas herramientas que son comunes a la mayoría de los lenguajes imperativos.

## A continuación se brinda un análisis posible:

* Se va a leer una secuencia de datos del teclado y, por cada uno de ellos, se debe procesar algo. Entonces va a ser necesaria una iteración que repita algunas instrucciones. Como se solicita que se lean 50 datos, se puede usar un **for** (otra opción sería un while que lleve un contador hasta 50). Al final de la lectura de datos se deben informar determinadas cosas. Todo lo que el enunciado pide que se muestre requiere que haya terminado la lectura de los datos, entonces estos resultados se informarán luego de finalizada la iteración (porque, si se informa dentro de la iteración, se estarían dando resultados parciales, no el resultado final que se tiene una vez leídos los 50 strings). Entonces, la iteración comprenderá la lectura de datos (es decir, de cada uno de los 50 strings) y el procesamiento de los mismos.
* **a.** Para saber si hay más mayúsculas que minúsculas, primero será necesario saber si lo que se leyó es una letra (ya que se leen strings de cualquier tipo) y, en ese caso, saber si es mayúscula o minúscula. Esto podría delegarse en alguna función que lo resuelva: por ejemplo, pasándole el string leído y unos contadores que la función incrementará si el carácter es mayúscula o minúscula, o no hará nada si el string no es una letra. Como hay que saber cantidades, es indispensable tener contadores (uno para mayúsculas y otro para minúsculas). Al final de la iteración se podrán comparar esos contadores para saber cuál tiene el número mayor o si son iguales (esto debe hacerse fuera de la iteración, porque se necesita el número total de mayúsculas y el total de minúsculas leídas).
* **b.** El algoritmo para averiguar la cantidad de dígitos numéricos entre 1 y 8 también podría delegarse en una función. Por ejemplo, que la función retorne True si el número está entre 1 y 8 o False si no lo está. Si la función retorna True, entonces incrementar un contador. Para saber si el string leído es un dígito entre el 1 y el 8, se puede usar un contenedor (conjunto, lista, tupla...) que contenga los dígitos en forma de string del 1 a 8 y verificar, por cada string leído, si éste está en ese contenedor.
* **c.** Para saber cuántas ocurrencias hay de algo, es necesario tener algún contador. Pero en este caso se piden ocurrencias de muchas cosas (particularmente, de todas las letras del abecedario). Sería impracticable tener una variable por cada letra porque, además de que el código se hace ilegible y difícil de escribir, también se complica mucho si el enunciado del problema varía (algo que suele suceder muy a menudo con los programas "reales") y se necesitara agregar más contadores. Entonces es necesario guardar todos esos contadores en alguna estructura. La estructura debería contener lo que se está contando (en este caso, cada letra) y la cantidad de ocurrencias (contador). Una estructura adecuada podría ser la de tipo "mapa" o "diccionario", donde cada elemento es un par _clave/valor_, donde la clave sea la letra en minúscula (porque cada letra es única, y la clave debe ser un dato único) y el valor, un número para contar la cantidad de cada letra. Como son contadores (es decir que la primera vez que se usen se va a incrementar el valor, y para eso se usa el valor anterior) es necesario inicializarlos en cero. Para esto habrá que recorrer la estructura asignandole 0 a cada valor del diccionario. Primero debemos ver si el carácter leído es una letra; si es así, entonces podemos convertirla a minúscula (para que haya consistencia y la letra "a" cuente igual que la "A") y usarla como clave para incrementar el contador correspondiente. Por ejemplo, si estuviéramos trabajando en Python y el diccionario se llamara "alfabeto", el dato leído estuviera guardado en la variable "carácter" y ya se determinó que es una letra minúscula, se puede acceder al contador con: _alfabeto[carácter]_. Al finalizar la carga de este contenedor, se debe iterar por el mismo para imprimir por pantalla las ocurrencias (pero esto último se hará por fuera de la iteración "for" principal).
* **d.** Gracias al inciso anterior, ahora tenemos un contenedor (un mapa o diccionario) donde se guardaron las ocurrencias de las letras, por lo que podríamos buscar ahí dentro cuál es la que apareció mayor cantidad de veces, mediante la búsqueda del mayor valor dentro de esa estructura. Como lo que se pide es saber cuál es la letra, al recorrer el contenedor, además de ir guardando el mayor valor debe guardarse a qué letra corresponde. Y debido a que ya tenemos una iteración por el contenedor, hecha en el inciso anterior para imprimir todas las ocurrencias, podría reutilizarse esa iteración para, a la vez que se imprimen las ocurrencias, se busque el mayor valor. Posteriormente, se imprime cuál fue la letra que ostentó ese mayor valor de ocurrencias.

## Código escrito en Python:
        
<pre><code>#funciones

def contarMayúsculasMinúsculas(carácter, mayúsculas, minúsculas):
    if carácter in "abcdefghijklmnñopqrstuvwxyzáéíóúü":
        return (mayúsculas,minúsculas+1)
    elif carácter in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ":
        return (mayúsculas+1,minúsculas)
    else:
        return (mayúsculas,minúsculas)

def entre1y8(carácter):
    if carácter in "12345678":
        return True
    else:
        return False

def contarOcurrencia(carácter, diccionario):
    carácter=carácter.lower()
    if carácter in "abcdefghijklmnñopqrstuvwxyz":
        diccionario[carácter]+=1
    return diccionario


#programa principal

mayúsculas=0
minúsculas=0
númerosEntre1y8=0
ocurrencias={}
for letra in "abcdefghijklmnñopqrstuvwxyz":
    ocurrencias[letra]=0
    
for i in range(3):
    carácter=input("Ingresar carácter de longitud 1: ")
    mayúsculas,minúsculas=contarMayúsculasMinúsculas(carácter, mayúsculas, minúsculas)
    if entre1y8(carácter):
        númerosEntre1y8+=1
    ocurrencias=contarOcurrencia(carácter, ocurrencias)

if mayúsculas&gt;minúsculas:
    print("Se ingresó mayor cantidad de mayúsculas")
elif mayúsculas&lt;minúsculas:
    print("Se ingresó mayor cantidad de minúsculas")
else:
    print("La cantidad de mayúsculas ingresadas fue igual a la cantidad de minúsculas")

letraMayorOcurrencia=""
mayorCantidad=0
print("Ocurrencias de cada letra: ")
for letra,cantidad in ocurrencias.items():
    print(letra,":",cantidad)
    if cantidad&gt;mayorCantidad:
        mayorCantidad=cantidad
        letraMayorOcurrencia=letra

print("Letra que apareció mas veces:", letraMayorOcurrencia)</code></pre>
        
