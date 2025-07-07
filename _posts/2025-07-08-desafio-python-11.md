---
layout: post
title: Desafío Python número 11
date: 2025-07-08 18:00:00 -0300
categories: desafios python
tags: referencia max id
published: false
---

Sin ejecutarlo, ¿sabrías decir qué imprime cada `print` del código? Es importante saber que la función `max` devuelve el mayor valor cuando se le pasan dos o más argumentos, y en este caso está recibiendo tres listas con el mismo contenido. Por su parte, `id` es una función que devuelve la referencia (dirección de memoria) del objeto que se le pase como argumento.



<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ La respuesta correcta es la d: False, True, True
<br />
<br />✏️ Explicación: max() devuelve el mayor valor de los argumentos que se le pasan, y en este caso se le pasaron tres listas iguales: [1,2,3], pero cada una guardada en una variable diferente (es decir que son tres objetos, con tres direcciones de memoria, aunque los tres tengan el mismo contenido). Cuando hay elementos iguales, max simplemente devuelve el primero de ellos (de izquierda a derecha) que tenga el valor máximo. Por eso la variable d es una referencia a la lista guardada en a y la variable e es una referencia a la lista guardada en c. 
<br />
<br /><div markdown="1">💻 [Código ejecutable](https://paiza.io/projects/RAYYfBTFpelhoTPD_0KWxA){:target="_blank"}
  </div>
{% include codeEditor_paiza.html id="RAYYfBTFpelhoTPD_0KWxA" %} 
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2025-07-08-desafio-python-11-solucion.png)
  </div></details>

<br />
<br />
**Desafío Python** 👇
<br />
![Desafío Python número 11]({{ site.url }}/assets/2025-07-08-desafio-python-11.png)

{% include accesibilidad.html %}

Desafío Python

¿Qué imprime este programa?

```python
a = [1,2,3]
b = [1,2,3]
c = [1,2,3]
d = max(a,b,c)
e = max(c,b,a)
print(id(d) == id(e))
print(id(d) == id(a))
print(id(e) == id(c))
```

Opciones:

a) False, False, True

b) True, True, True

c) True, False, True

d) False, True, True

</div></details>
