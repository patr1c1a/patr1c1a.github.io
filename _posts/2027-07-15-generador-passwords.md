---
layout: post
title: Cómo crear un generador de contraseñas seguras
date: 2025-07-15 13:00:00 -0300
categories: python
tags: secrets passwords
published: true
---

¡Usemos Python para escribir nuestro propio generador de contraseñas!

Esta es una versión básica, pero podemos hacer varias mejoras, como permitir que la contraseña solo empiece con una letra, diferenciar mayúsculas de minúsculas, usar solo ciertos símbolos, garantizar al menos un carácter de cada tipo... ¿Cómo las implementarías? ¿Se te ocurren otras?


💻 [Código ejecutable](https://paiza.io/projects/Jwz-W0w8G4ULQmqgTjzQRg){:target="_blank"}



![Cómo crear un generador de contraseñas seguras]({{ site.url }}/assets/2027-07-15-generador-passwords.png)


&nbsp;

{% include accesibilidad.html %}
Cómo crear un generador de contraseñas seguras en Python

Combinando letras, números y símbolos se pueden crear contraseñas difíciles de adivinar. En Python podemos usar el módulo secrets y la función secrets.choice para elegir caracteres al azar de una secuencia.

¿Por qué no usamos el módulo random?

random es pseudoaleatorio: parece aleatorio pero en realidad es predecible si se conoce la semilla y el algoritmo usados:

```python
import random

random.seed(123)
print(random.choices(range(1,70)))
```

El ejemplo anterior siempre imprime 4.

El módulo secrets genera datos criptográficamente seguros y es preferible cuando se necesitan datos sensibles (como contraseñas, tokens, etc.).

Generador:

```python
import string
import secrets
 
def generar_password(longitud=12):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    todos = letras + numeros + simbolos
 
    password = ""
 
    for i in range(longitud):
        c = secrets.choice(todos)
        password += c
 
    return password
 
# Ejemplo de uso:
print(generar_password(16))
```

- secrets.choice() retorna un elemento al azar de la secuencia que le pasemos como argumento.
- string.ascii_letters incluye todas las letras mayúsculas y minúsculas.
- string.digits incluye los números del 0 al 9.
- string.punctuation incluye símbolos como !@#$%^&*().


</div></details>
<br />&nbsp;
<hr />
