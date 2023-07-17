---
layout: post
title: ¿Qué significa que el código sea "Pythónico"?
date: 2023-07-22 21:00:00 -0300
categories: python
tags: pythonic pythonico estilos legibilidad
published: false
---

Si queremos escribir código Python que luzca profesional, debemos prestar atención a que nuestro estilo sea "Pythónico". Es decir, que aproveche las herramientas que el lenguaje provee para que nuestros algoritmos sean más elegantes y simples.

En los tres ejemplos que se muestran vemos cómo el primero, si bien es sintácticamente correcto, se parece a un algoritmo que podría haber sido escrito con algún otro lenguaje. Sin embargo, las opciones 2 y 3 son propias de Python.

En la opción 2 se generan [listas por comprensión]({% post_url 2021-01-18-python-listas-comprension %}) donde los elementos son datos booleanos correspondientes a cada carácter del string "s" e indican si ese carácter cumple o no con la condición pedida (`isalnum()` verifica si es alfanumérico, `isalpha()` verifica si es alfabético, `isdigit()` verifica si es un dígito, `islower()` verifica si es una letra minúscula y `isupper()` verifica si es una letra mayúscula). Luego se imprime el resultado de la operación de pertenencia usando el operador `in`.

La opción 3 también comienza de manera similar a la opción 2 pero aprovecha la función `any()`, que devuelve True si alguno de los elementos de la secuencia que se le pasa como argumento es True.


![¿Qué significa que el código sea "Pythónico"?]({{ site.url }}/assets/2023-07-22-codigo-pythonico.png)


&nbsp;

{% include accesibilidad.html %}

¿Qué significa que el código sea "Pythónico"?

Que el código tenga un estilo "Pythónico" significa que aprovecha las facilidades de Python para una mayor simpleza y legibilidad.

Dado un string s, imprimir 5 líneas con True o False según lo siguiente:
- si s tiene algún carácter alfanumérico,
- si s tiene algún carácter alfabético,
- si s tiene algún dígito,
- si s tiene alguna letra minúscula,
- si s tiene alguna letra mayúscula.

Veamos tres opciones que resuelven esta consigna...

Opción 1:

```python
alfanum = alfa = digito = minuscula = mayuscula = False
for c in s:
    if c.isalnum():
        alfanum = True
    if c.isalpha():
        alfa = True
    if c.islower():
        minuscula = True
    elif c.isupper():
        mayuscula = True
    elif c.isdigit():
        digito = True
print(alfanum, alfa, digito, minuscula, mayuscula, sep="\n")
```

Opción 2:

```python
print(True in [c.isalnum() for c in s])
print(True in [c.isalpha() for c in s])
print(True in [c.isdigit() for c in s])
print(True in [c.islower() for c in s])
print(True in [c.isupper() for c in s])
```

Opción 3:

```python
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
```

La primera solución es algo "genérica". Las opciones 2 y 3 muestran código más "Pythónico".

</div></details>


<hr />
