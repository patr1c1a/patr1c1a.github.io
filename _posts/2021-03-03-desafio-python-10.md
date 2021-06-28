---
layout: post
title: Desafío Python número 10
date: 2021-03-03 12:00:00
categories: desafios python
tags: tuplas iteraciones
published: true
---
¡Nuevo desafío Python!

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ EL PROBLEMA ESTÁ EN LA LÍNEA 1: la segunda tupla solo tiene 2 elementos, por lo que se arroja el siguiente error al intentar "desempaquetar" durante la iteración:
*ValueError: not enough values to unpack (expected 3, got 2)*. La iteración falla pues se intenta desempaquetar usando tres variables -nombre, edad, pais- y la segunda tupla tupla no tiene suficientes elementos.
<br />
<br />✏️ Para solucionarlo, deberíamos agregar un valor a la segunda tupla. Para que sea semánticamente correcto, debería agregarse un número en la posición 1 de la segunda tupla.
<br />&nbsp;
<br /><div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3pSN){:target="_blank"}
  </div>
{% include codeEditor.html id="3pSN?stdin=0&arg=0&rw=1" %}
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2021-03-03-desafio-python-10-solucion.png)
  </div></details>

<br />
<br />
**Desafío Python** 👇
<br />
![Desafío Python número 10]({{ site.url }}/assets/2021-03-03-desafio-python-10.png)

{% include accesibilidad.html %}
	
El siguiente código tiene un error:

```python
estudiantes = [("Ana", 23, "Colombia"), ("Marco", "Perú"), ("Leonela", 21, "México")]
for nombre, edad, pais in estudiantes:
    print(f"Nombre: {nombre}, Edad: {edad}, País: {pais}")
``` 

¿Pudiste detectarlo? ¿Cómo lo solucionarías?
</div></details>



