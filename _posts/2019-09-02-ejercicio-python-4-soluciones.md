---
layout: post
title: Ejercicio con listas y 4 soluciones en Python
date: 2019-09-02 21:00:00
categories: ejercicios python
tags: arreglos
published: true
---

Un mismo problema, 4 formas diferentes de resolverlo. ¿Se te ocurre alguna otra?

El problema es: "nums es una lista no vacía de números enteros donde cada elemento aparece dos veces, excepto uno. Se debe encontrar el elemento que no se repite."

Para pensar: ¿cómo afectaría a la complejidad algorítmica si, en la primera alternativa, se reemplaza la lista por un conjunto?

<br />
<br />![Enunciado]({{ site.url }}/assets/2019-09-02-ejercicio-python-4-soluciones-01.png)
<br />
<br />![Alternativa 1]({{ site.url }}/assets/2019-09-02-ejercicio-python-4-soluciones-02.png)
<br />
<br />![Alternativa 2]({{ site.url }}/assets/2019-09-02-ejercicio-python-4-soluciones-03.png)
<br />
<br />![Alternativa 3]({{ site.url }}/assets/2019-09-02-ejercicio-python-4-soluciones-04.png)
<br />
<br />![Alternativa 4]({{ site.url }}/assets/2019-09-02-ejercicio-python-4-soluciones-05.png)


{% include accesibilidad.html %}
EJERCICIO CON LISTAS y  4  soluciones  en  Python

"nums es una lista no vacía de números enteros donde cada elemento aparece dos veces, excepto uno. Se debe encontrar el elemento que no se repite."

Ejemplo 1:

- Entrada: [2,2,1]
- Salida: 1

Ejemplo 2:

- Entrada: [4,1,2,1,2]
- Salida: 4

ALTERNATIVA 1: usando otra lista

1. Iterar por todos los elementos en nums.
2. Si algún número en nums es nuevo en la lista, agregarlo. Si algún número ya estaba en la lista, eliminarlo.
3. Retornar el único elemento que queda.

```python
def numero_no_repetido(nums):
    sin_duplicados = []
    for i in nums:
        if i not in sin_duplicados:
            sin_duplicados.append(i)
        else:
            sin_duplicados.remove(i)
    return sin_duplicados.pop()
```

Complejidad algorítmica: O(n^2)

ALTERNATIVA 2: usando una tabla hash

1. Iterar por todos los elementos en nums.
2. Si tabla_hash tiene una clave con el elemento, extraerlo usando pop. Si no, agregar un par clave/valor.
3. Al final solo quedará un elemento. Obtenerlo con popitem.

```python
def numero_no_repetido(nums):
    tabla_hash = {}
    for i in nums:
        try:
            tabla_hash.pop(i)                
        except:
            tabla_hash[i] = 1
    return tabla_hash.popitem()[0]
```

Complejidad algorítmica: O(n)

ALTERNATIVA 3: usando un enfoque matemático

Al duplicar la suma de los elementos distintos y restarle la suma total, todos los pares se cancelan y solo queda el elemento único: 2 * (a + b + c) - (a + a + b + b + c) = c

```python
def numero_no_repetido(nums):
    return 2 * sum(set(nums)) - sum(nums)
```

Complejidad algorítmica: O(n)

ALTERNATIVA 4: mediante manipulación de bits

- Si aplicamos XOR entre el 0 y un bit, retornará ese bit: a ⊕ 0 = a
- Si aplicamos XOR entre dos bits iguales, retornará 0: a ⊕ a = 0
- Entonces: a ⊕ b ⊕ a = (a ⊕ a) ⊕ b = 0 ⊕ b = b

```python
def numero_no_repetido(nums):
    a = 0
    for i in nums:
        a ^= i
    return a
```

Complejidad algorítmica: O(n)

</div></details>
