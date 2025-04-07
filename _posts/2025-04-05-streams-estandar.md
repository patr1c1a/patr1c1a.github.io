---
layout: post
title: Streams estándar
date: 2025-04-06 09:00:00 -0300
categories: otros
tags: streams
published: true
---

Los "streams" estándar son una herencia de Unix en los años 70, pero hoy son universales. Todos los lenguajes los usan, y el sistema operativo les asigna los números 0 (stdin), 1 (stdout) y 2 (stderr) para identificarlos. Tener un canal específico para errores nos permite separarlos de la salida "normal" del programa.


![Streams estándar]({{ site.url }}/assets/2025-04-05-streams-estandar.png)


&nbsp;

{% include accesibilidad.html %}

"Streams estándar"

Son canales básicos que todo programa usa para comunicarse con el sistema, ya sea en terminal o en segundo plano.

0- stdin (Entrada): Datos que ingresa el usuario.

1- stdout (Salida normal): Resultados normales del programa.

2- stderr (Errores): Mensajes de error (no se mezclan con los resultados).

Ejemplo en Python:

```python
try:
    num = int(input("Número: "))  # stdin
    print(10 / num)               # stdout
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)  # stderr
```

En la terminal, se pueden redirigir errores a un archivo:

```bash
$ python programa.py 2> errores.log
```


</div></details>
<br />&nbsp;
<hr />
