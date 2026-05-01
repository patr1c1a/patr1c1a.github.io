---
layout: post
title: La IA ayudó a descubrir un bug en Linux desde 2017
date: 2026-05-01 16:00:00
categories: ia
tags: ia linux bug
published: true
---

![Bug en Linux]({{ site.url }}/assets/2026-05-01-ia-bug-linux.png){: width="40%" }

## Un error escondido por 9 años

Una IA ayudó a descubrir una vulnerabilidad crítica en Linux… y es un bug que estuvo oculto durante 9 años en el kernel. Se trata de CVE-2026-31431 (“Copy Fail”) y afecta prácticamente a todas las distribuciones desde 2017.

No significa que la IA “haya hackeado Linux sola”. Lo que sí se sabe es que herramientas basadas en IA se están usando para analizar código y detectar patrones que humanos pueden pasar por alto, especialmente en sistemas gigantes como el kernel.

## Por qué es tan grave

Lo que hace a esta vulnerabilidad especialmente peligrosa no es solo el impacto, sino lo simple que es explotarla: no requiere técnicas complejas ni condiciones especiales. La mayoría de los ataques de escalación de privilegios en Linux requieren condiciones muy específicas: timing perfecto, configuraciones particulares o información interna del sistema. Este no.

Acá alcanza con tener un usuario común. Desde ahí, el atacante puede aprovechar una falla lógica en cómo el kernel maneja ciertas operaciones, y modificar una pequeña parte de la memoria en RAM. ¿El resultado? La próxima vez que se ejecuta un programa clave del sistema, ese usuario obtiene acceso como root (control total).

Es decir que este ataque funciona siempre, en cualquier Linux moderno. Incluso con un script de solo 732 bytes.

## Qué hace el ataque

- El atacante usa una función interna de Linux;
- Logra modificar memoria en RAM;
- Apunta a un programa del sistema;
- La próxima vez que se ejecuta, entra como root.

Y hay un detalle importante: esto no modifica archivos en disco. Todo ocurre en memoria, lo que lo hace mucho más difícil de detectar. Si analizás el sistema después, los archivos parecen intactos. Además: Los contenedores no aíslan este problema (comparten memoria con el host).

## ¿A quiénes afecta?

Afecta entornos como servidores compartidos, CI/CD y cloud. Y puede escalar desde un acceso mínimo a control total.

Ya existe un parche así que, si usás Linux, actualizar el kernel es una prioridad.

## Fuente

[Copy Fail: 732 Bytes to Root on Every Major Linux Distribution - Xint.io](https://xint.io/blog/copy-fail-linux-distributions){:target="_blank"}
