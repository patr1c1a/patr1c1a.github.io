---
layout: post
title: Función zip en Python para iterar en simultáneo
date: 2023-11-15 12:00:00 -0300
categories: python
tags: zip, iteraciones
published: true
---

La función zip en Python combina elementos de dos o más iterables en tuplas. Crea un iterador que genera tuplas donde los i-ésimos elementos de cada iterable se agrupan juntos. Es útil para combinar datos de múltiples iterables de manera sincronizada, por ejemplo cuando necesitamos iterar los dos al mismo tiempo.

![Funcion zip en Python]({{ site.url }}/assets/2023-11-15-python-zip.png)


&nbsp;

{% include accesibilidad.html %}

Python: Recorrer dos iterables en simultáneo usando zip

La función zip recibe dos iterables y forma tuplas con pares de elementos, en el orden en que aparecen.

Ejemplo:

```python
nums1 = [1,3,5]
nums2 = [2,4,6]
resultado = zip(nums1, nums2)
print(list(resultado))
```

Salida: 

```
[(1, 2), (3, 4), (5, 6)]
```

Esto permite iterar en simultáneo:

```python
nums1 = [1,3,5]
nums2 = [2,4,6]
for a, b in zip(nums1, nums2):
    print(a, b)
```

Salida:

```
1 2
3 4
5 6
```

La longitud estará dada por el iterable con menor cantidad de elementos:

```python
nums1 = [1,3,5,7]
nums2 = [2,4]
for a, b in zip(nums1, nums2):
    print(a, b)
```

Salida:

```
1 2
3 4
```

</div></details>
<br />&nbsp;

### [Código Python para ejecutar](https://www.jdoodle.com/ia/QFf){:target="_blank"}

{% include codeEditorNew.html id="QFf?stdin=0&arg=0&rw=1" %}

<br />&nbsp;

<hr />
