---
layout: post
title: Algoritmo para invertir un número entero
date: 2023-10-02 12:00:00 -0300
categories: java, ejercicios
tags: matematica, numeros, algoritmos
published: true
---

Este algoritmo trabaja con operaciones matemáticas simples para separar los dígitos de un número e invertir su posición.

![Algoritmo para invertir un numero entero, pasos 1 y 2]({{ site.url }}/assets/2023-10-02-invertir-numero-java-img1.png)

![Algoritmo para invertir un numero entero, paso 3]({{ site.url }}/assets/2023-10-02-invertir-numero-java-img2.png)

![Algoritmo para invertir un numero entero, pasos 4 y 5]({{ site.url }}/assets/2023-10-02-invertir-numero-java-img3.png)

![Algoritmo para invertir un numero entero, en Java]({{ site.url }}/assets/2023-10-02-invertir-numero-java-img4.png)


&nbsp;

{% include accesibilidad.html %}

Algoritmo para invertir un número entero, paso a paso

Ejemplo: 4752 se convierte en 2574

Paso 1: Empezamos con una variable que guardará el número invertido, inicialmente en 0: `invertido = 0`

Paso 2: Tomamos el último dígito del número (dividiendo por 10 y quedándonos con el módulo): `ultimo_digito = numero % 10`

Ejemplo: 4752÷10=475,2

El resto de la división es 2. Esto es porque la columna de la decena (50) puede dividirse por 10 sin resto, al igual que la columna de la centena (70) y que la unidad de mil (40). El resto de la división será 2, ya que la columna de la unidad no puede dividirse por 10.

Paso 3: Agregamos el último dígito al invertido. Para ello, multiplicamos al invertido por 10 para que la unidad pase a ser la decena, la decena pase a ser la centena, etc. y de esta forma se agrega una nueva columna de unidad, en 0. Entonces sumamos el último dígito: `invertido = (invertido * 10) + ultimo_digito`

Ejemplo: si invertido fuera 25 y quisiéramos agregar el 7 al final: 25*10=250 y 250+7=257

Paso 4: Ahora eliminamos el último dígito del número (dividiendo por 10 y quedándonos con la parte entera) porque ya fue procesado: `numero = numero / 10` 

Ejemplo: 4752÷10=475,2

La parte entera de la división es 475.

Paso 5: Se repite este proceso hasta que el número sea 0: `while numero > 0`

Como guardamos el resultado de la operación "pisando" el valor del número original, cuando solo haya quedado un dígito a procesar, la parte entera de la división será 0: 4÷10=0,4

Implementación en Java:

```java
int invertirNumero(int numero){
      int invertido = 0;
      while (numero > 0) {
        int ultimo_digito = numero % 10;
        invertido = (invertido * 10) + ultimo_digito;
        numero = numero / 10;
      }    
      return invertido;
    }
```

</div></details>
<br />&nbsp;

### [Código Java para ejecutar](https://jdoodle.com/a/6CkG){:target="_blank"}

{% include codeEditor.html id="6CkG?stdin=0&arg=0&rw=1" %}

<br />&nbsp;

<hr />
