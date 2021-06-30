---
layout: post
title: Desafío Python número 8
date: 2019-11-29 21:00:00
categories: desafios python
tags: challenge funciones
published: true
---

Desafío Python número 8.

En este caso, debemos generar casos de prueba para un algoritmo y corregirlo. 

No debemos confiarnos si un algoritmo funciona como esperamos en los casos más "obvios": es necesario hacer varias pruebas para mejorarlo todo lo posible. 

▶️ [Video: cómo probar una función en Python](https://www.youtube.com/watch?v=ZJP0Z5-sbeY){:target="_blank"}


<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />Una posible solución al desafío: las dos últimas invocaciones retornaban un resultado incorrecto con la versión errónea del algoritmo. En la versión corregida dada en la solución, las cuatro invocaciones retornan lo esperado.
<br />&nbsp;
<div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3q8F){:target="_blank"}
  </div>  

{% include codeEditor.html id="3q8F?stdin=0&arg=0&rw=1" %}
  
<br />😀 ¿Se te ocurrieron otras formas de mejorar el algoritmo? Deja tu comentario debajo.
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-11-29-desafio-python-8-solucion.png)
  </div>

</details>

<br />
<br />
**Desafío Python** 👇

![Desafío Python número 8]({{ site.url }}/assets/2019-11-29-desafio-python-8.png)

{% include accesibilidad.html %}

La función a continuación intenta definir si dos secuencias tienen los mismos elementos únicos. Pero el algoritmo no siempre funciona correctamente. ¿En qué casos no funciona y cómo debería corregirse?

```python
def mismosElementos(L1, L2):
    elementos = set()
    for numero in L1:
        elementos.add(numero)
    for numero in L2:
        elementos.discard(numero)
    return len(elementos) == 0
```

Estas invocaciones retornan True y False, como se esperaría:

`mismosElementos( [1,2,2,3], [1,1,1,2,3] )`

`mismosElementos( [1,2,3], [1,1,3] )`

Pero, ¿podrías indicar otros ejemplos que no retornen el resultado correcto? ¿Cómo corregirías el algoritmo para que los ejemplos dados retornen el resultado esperado?

Resolución:

Estos ejemplos son dos casos que retornan el resultado incorrecto (True y True cuando ambas deberían retornar False, ya que no tienen los mismos elementos únicos)

`mismosElementos( [1,2,2,3], [0,1,1,2,3] )`

`mismosElementos( [], [0,1,1,2,3] )`

Este algoritmo está corregido para que retorne lo que realmente pide la consigna (True si los elementos de ambas listas son iguales, False si no lo son):

```python
def mismosElementos(L1, L2):
  elementos1 = set()
  elementos2 = set()
  for numero in L1:
      elementos1.add(numero)
  for numero in L2:
      elementos2.add(numero)
  return elementos1 == elementos2
```


</div></details>
