---
layout: post
title: Ejercicio con strings
date: 2019-09-03 21:00:00
categories: ejercicios python java c++
tags: entrevista trabajo
published: true
---

Una pregunta que puede aparecer en una entrevista laboral para el puesto de desarrollador, y algunas respuestas (aunque no las únicas) posibles.

Un detalle a tener en cuenta es que, en Java, concatenar cadenas en un bucle con `+=` no es eficiente para textos largos, porque cada concatenación crea un nuevo objeto String (las cadenas son inmutables). Para código de producción se suele usar StringBuilder. Pero para un ejercicio como este, la concatenación con `+=` suele ser suficiente.

▶️ [Video: strings en Python](https://www.youtube.com/watch?v=xAigyL6Lz2s){:target="_blank"}

![Problema de entrevista laboral]({{ site.url }}/assets/2019-09-03-problema-entrevista-strings.png)

&nbsp;

{% include accesibilidad.html %}
PROBLEMA DE PROGRAMACIÓN

Escribir una función para invertir un string. Puede usarse cualquier lenguaje, pero debe evitarse el uso de funciones predefinidas para invertir strings.

ALGUNAS POSIBLES SOLUCIONES:

Solución en C++:

```cpp
std::string invertir(std::string s) {
    std::string invertido = "";
    for (int i = s.length()-1; i >= 0; i--) {
        invertido += s[i];
    }
    return invertido;
}
```

Solución 1 en Python:

```python
def invertir(s):
    invertido = ""
    for c in s:
        invertido = c + invertido
    return invertido
```

Solución 2 en Python:

```python
def invertir(s):
  invertido = ""
  for i in range(len(s) -1, -1, -1):
     invertido += s[i]
  return invertido
```

Solución en Java:

```java
public static String invertir(String s) {
  String invertido = "";
  for (int i = s.length()-1; i>=0; i--) {
     invertido += s.charAt(i);
  }
  return invertido;
}
```

</div></details>

&nbsp;
