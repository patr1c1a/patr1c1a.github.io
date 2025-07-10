---
layout: post
title: Cómo crear un generador de contraseñas seguras
date: 2025-07-15 13:00:00 -0300
categories: python
tags: secrets passwords
published: true
---

¡Usemos Python para escribir nuestro propio generador de contraseñas!

- string.ascii_letters incluye todas las letras mayúsculas y minúsculas.
- string.digits incluye los números del 0 al 9.
- string.punctuation incluye símbolos como !@#$%^&*() dependiendo del sistema operativo.
- random.choices selecciona k elementos al azar con reemplazo (pueden repetirse).

Esta es una versión básica, pero podemos implementar varias mejoras, como permitir que la contraseña solo empiece con una letra, diferenciar mayúsculas de minúsculas, permitir solo ciertos símbolos y no otros, garantizar al menos un carácter de cada tipo seleccionado... ¿Cómo las implementarías? ¿Se te ocurren otras?


💻 [Código ejecutable](https://paiza.io/projects/Jwz-W0w8G4ULQmqgTjzQRg){:target="_blank"}



![Cómo crear un generador de contraseñas seguras]({{ site.url }}/assets/2027-07-15-generador-passwords.png)


&nbsp;

{% include accesibilidad.html %}
Cómo crear un generador de contraseñas seguras

Combinando letras, números y símbolos se pueden crear contraseñas difíciles de adivinar. En Python podemos usar el módulo random y la función random.choices para elegir caracteres al azar de un conjunto definido.

```python
import string
import secrets

def generar_password(longitud=12, usar_letras=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ""
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debe elegir al menos un tipo de carácter.")

    password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return password

# Ejemplo de uso:
print(generar_password(longitud=10))
```

¿Qué mejoras le harías?


</div></details>
<br />&nbsp;
<hr />
