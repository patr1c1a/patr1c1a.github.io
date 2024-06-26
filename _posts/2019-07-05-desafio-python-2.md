---
layout: post
title: Desafío Python número 2
date: 2019-07-05 21:00:00
categories: desafios python
tags: funciones listas
published: true
---
¿Podrías decir qué retorna la llamada a esta función, con el argumento dado? Para saberlo, deberás analizar el algoritmo de la función. Para ayudarte a resolverlo, pueden serte útiles estos videos: 

▶️ [Video: Listas en Python](https://www.youtube.com/watch?v=TEHBEGj1MSU){:target="_blank"}

▶️ [Video: Ejercicios resueltos con listas en Python (1)](https://www.youtube.com/watch?v=0NTaCJQUE1I){:target="_blank"}

▶️ [Video: Ejercicio resuelto con listas en Python (2)](https://www.youtube.com/watch?v=8fKMHKvDieU){:target="_blank"}

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />La opción correcta es la c.
<br />
<br />✏️ Explicación:
<br />✅ Opción c): este algoritmo retorna una lista con los elementos de la secuencia pasada por parámetro, excepto los elementos duplicados consecutivos. El parámetro puede ser cualquier secuencia (un string, una lista, una tupla...).
<br />Para ello, se almacena en una lista el primer elemento de la secuencia y se comienza a recorrer desde el segundo elemento en adelante, mediante la rebanada secuencia[1:]. Por cada elemento de la secuencia, se verifica si es igual al último elemento de la lista, el cual se encuentra en la posición len(lista)-1. Si son diferentes, significa que el elemento que se está evaluando es diferente del anterior, entonces se lo agrega en la lista (si son iguales, significa que el elemento tiene un duplicado consecutivo en la secuencia, y en ese caso no se hace nada).
<br />🚫 Opciones incorrectas:
<br />a): en esta lista aparecen todos los caracteres del string, por lo que no se eliminan duplicados consecutivos.
<br />b): esta lista elimina la letra "a" inicial, lo cual no se corresponde con el algoritmo, porque "a" y "A" son dos caracteres diferentes. Además, elimina una sola ocurrencia de la "h", de la que se encontraban 3 ocurrencias en el string pasado por parámetro.
<br />
<div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3pVx){:target="_blank"}
  </div>
{% include codeEditor.html id="3pVx?stdin=0&arg=0&rw=1" %}
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-07-05-desafio-python-2-solucion.png)
  </div></details>

<br />
<br />
**Desafío Python** 👇
![Desafío Python número 2]({{ site.url }}/assets/2019-07-05-desafio-python-2.png)

{% include accesibilidad.html %}

```python
def funcion(secuencia):
    lista = [secuencia[0]]
    for elemento in secuencia[1:]:
        if elemento != lista[len(lista)-1]:
            lista.append(elemento)
    return lista
```

¿Qué retorna la llamada funcion('aA7577hhhA')?

a. ['a','A','7','5','7','7','h','h','h','A']

b. ['A','7','5','7','h','h','A']

c. ['a', 'A', '7', '5', '7', 'h', 'A']
</div></details>
