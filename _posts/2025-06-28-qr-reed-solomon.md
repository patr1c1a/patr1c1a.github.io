---
layout: post
title: ¿Por qué un QR dañado sigue funcionando?
date: 2025-06-28 12:00:00 -0300
categories: otros
tags: qr algoritmos correccion_errores
published: true
---

El algoritmo Reed-Solomon usa la matemática para recuperar datos aunque falten partes, mediante operaciones con números especiales llamados "códigos" para detectar y corregir errores, tratando los datos como si fueran partes de un polinomio. Así puede reconstruir los valores que faltan.

No solo es útil en los códigos QR: también se usa en CDs, DVDs, Blu-Ray, transmisiones espaciales, Ethernet y comunicación satelital.

Al momento de la lectura, si faltan datos, se resuelve un sistema de ecuaciones polinómicas para reconstruirlos.


![Por qué un QR dañado sigue funcionando]({{ site.url }}/assets/2025-06-28-qr-reed-solomon.png)


&nbsp;

{% include accesibilidad.html %}

¿Por qué un QR dañado sigue funcionando?

El algoritmo Reed-Solomon permite recuperar datos aunque falten partes. Un QR podría leerse aunque hasta un 30% esté cubierto o borrado.

El algoritmo añade bloques de información extra llamados "códigos de corrección", que se intercalan con los datos reales. Si faltan datos, estos bloques permiten reconstruir el mensaje original sin errores.

Cada QR define un nivel de corrección: L (7%), M (15%), Q (25%), H (30%).

Los niveles inferiores de corrección son útiles cuando queremos que el QR almacene más datos, porque mientras mayor es la corrección, menos espacio queda para la información.

Código Python que genera un QR conteniendo una url, con nivel de corrección H:

```python
import qrcode

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('https://www.youtube.com/c/ProgramacionDesdeCero')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")
```


</div></details>
<br />&nbsp;
<hr />
