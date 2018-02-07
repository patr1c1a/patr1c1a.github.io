---
layout: post
title: Buenas prácticas de programación
date: 2015-10-23 19:00:00
categories: conceptos
tags: buenas_prácticas
published: true
---

Las buenas prácticas diferencian a los buenos programadores de los malos programadores. Son ciertas reglas o lineamientos acordados de manera informal por la industria del software para producir código de alta calidad.

Es altamente aconsejable adoptarlas desde los comienzos, ya que los malos hábitos no son sencillos de desterrar una vez adquiridos.

Esta es una lista, no taxativa, de algunas sugerencias ampliamente aceptadas en el ámbito profesional:

## Identificadores representativos

Se deben aplicar en los nombres de variables, funciones, tipos de dato, etc.

Los identificadores representan datos reales, por ende, son más fáciles de interpretar si se usan nombres reales.


## Identificadores consistentes

Utilizar un mismo estilo de nombre, sin mezclar. Por ejemplo, elegir entre escribir los nombres como unaVariable, una_variable ó UnaVariable.

Algo que también puede hacerse es cambiar el estilo por cada tipo de identificador: variables, constantes, funciones, tipos de datos. Por ejemplo, las constantes suelen escribirse con sus identificadores completamente en mayúsculas, por ejemplo: INT_MAX.

## Formato consistente

Usar sangría ("indentación") siempre de la misma forma (con espacios o con tabulaciones) y alineando de la misma manera las líneas de código que componen cada bloque.

Usar consistentemente los espacios y las líneas en blanco (por ejemplo, después de cada módulo, dejar siempre la misma cantidad de líneas en blanco).


## Evitar variables globales

Causan ambigüedad al no poder predecirse el valor que tendrán en determinado punto de la ejecución del programa, ya que su valor puede cambiarse desde cualquier parte del código. Este problema se intensifica a medida que las líneas de código aumentan y cuando más de un programador trabaja en él.

Además, las variables globales obstaculizan la legibilidad del código, al referir a datos que no se encuentran dentro del módulo que las usa, y dificultan las pruebas o detección de errores.

Por último, generan acoplamiento en el código.

No se deben confundir las _variables_ globales con constantes o definiciones de tipo, que suelen utilizarse de manera global y esto es correcto.


## Documentación

Así como cualquier producto tiene un manual de instrucciones, el código debe tener también descripciones sobre cómo usarlo correctamente. El usuario del código, habitualmente, será un programador, ya sea un tercero o el mismo programador que lo escribió (teniendo en cuenta que, pasado cierto tiempo, será muy difícil recordar por qué y con qué intención se escribió el código de determinada manera).

Además, existen herramientas que son capaces de generar archivos o apartados de documentación de manera automática, a partir de la documentación incluida en el código.

Normalmente, al documentar un módulo se incluye: nombre, propósito, descripción, autor original, cambios hechos, autor de los cambios.

También es buena práctica incluir, junto a la documentación, casos de prueba ("test cases") que permitan validar el código ante cualquier modificación que se haga. Para que sean correctos, los casos de prueba deben validar el código con datos válidos, datos inválidos, datos límite (el primer o el último valor admitido), sin datos, y cualquier otra posibilidad que pueda incluirse.


## Comentarios

Su utilidad es similar a la de la documentación.

Se deben evitar obviedades (por ejemplo, decir "se asigna un valor a la variable" cuando el código claramente muestra una asignación). Un buen comentario aclara _qué_ hace el código y _por qué_ se decidió hacerlo de esa manera.

Cuando se trabaja en equipo, los comentarios deben hacerse en un idioma que resulte neutral para todos los integrantes (por ejemplo, inglés, si el equipo incluye integrantes que no son de habla hispana).


## Agrupar los literales en un único lugar

Evitar "desparramar" valores literales a lo largo de todo el código permite hacer modificaciones centralizadas. Por esto, los literales deben, preferentemente, ubicarse en una única sección del código y referirse a ellos simbólicamente desde cada lugar donde se necesiten.

A la práctica de colocar valores literales cuando podrían haberse usado referencias se la llama "hard-coding".

Por ejemplo, si se utiliza un valor fijo en un cálculo que debe hacerse en varias partes del código, es conveniente que ese valor se declare como constante y luego se utilice el nombre de la misma cada vez que sea necesario. De esta manera, llegado el caso de realizar una modificación, será suficiente con hacerla en un solo punto del código.


## Modularización

Las tareas deben subdividirse.

Modularizar permite que el código sea reusable, no sólo dentro del mismo programa sino en otros programas que requieran funcionalidad similar.

Los módulos deben ser atómicos, es decir, realizar sólo una tarea. Es preferible invocar a más de un módulo que abarcar varias tareas en uno.

Además de la reutilización, una buena modularización permite aislar problemas más fácilmente.



## Simplicidad y claridad

Evitar la complejidad innecesaria que hace que un código sea menos legible. No sólo lo hace ilegible para terceros, sino para el propio programador, cuando necesita volver a utilizar ese código tiempo después de haberlo escrito.

La complejidad podría estar, no sólo en el algoritmo, sino en la forma de escribirlo: a veces, es mejor escribir algunas líneas más antes que abreviar demasiado.



## Comprobar validez de datos "externos"

Asumir que el usuario puede proporcionar datos en un formato diferente al esperado por el programa. El usuario puede ser un humano o incluso otro programa u otra máquina, y la incongruencia puede ser causada por error o por malicia.

Se debe evitar que el programa se detenga o quede inconsistente, para que pueda continuarse trabajando sin alteraciones.



## Mensajes de error adecuados

En pos de la usabilidad, es necesario no "aturdir" al usuario con mensajes de error que le brinden información que él no sabe cómo interpretar. Pero, a la vez, los detalles de un error deben quedar almacenados en alguna parte, accesibles para la persona con el conocimiento técnico para lidiar con ese error. Por ejemplo, podrían almacenarse en algún "log".



## Portabilidad

Permite ejecutar el mismo código en diferentes entornos.

Por eso, se deben evitar las rutas absolutas (que hacen referencia al sistema de archivos de una máquina en particular), indicar literalmente direcciones IP, nombres de usuarios o contraseñas, utilizar librerías que sólo corren en determinado sistema operativo, etc.


## No dar por sentado el formato de salida de los datos

Cuando un módulo o expresión retorna algún valor, éste podría tener diferentes fines, dependiendo del uso que se le de al programa.

No siempre un programa es utilizado por un usuario humano, sino que podría resultar que el usuario sea otro programa, que utiliza los datos para continuar procesándolos. Por esto, los datos pueden tener diferente fin: a veces se necesitará imprimirlos, a veces enviarlos a través de una red (en diversos formatos), otras veces los datos de salida de un programa serán la entrada de otro.


## Bajo acoplamiento

El grado de acoplamiento indica la interdependencia entre módulos, es decir, en qué medida dependen de la implementación o estado interno del otro.

La transitividad puede utilizarse como medida del acoplamiento: suponiendo que un módulo A invoca al módulo B y éste invoca al módulo C, el módulo A debería "conocer" lo menos posible el funcionamiento del módulo C. Mientras más requiera A conocer de C, más acoplados estarán.

Cuanto mayor sea el acoplamiento, mayor será la dificultad al modificar o reemplazar algún módulo, y mayor será la dificultad para probar su funcionamiento.

La posibilidad de aislar lo más posible los módulos también facilita el trabajo en equipo sin necesidad de comprender todo el resto del código y sin riesgo de que una modificación altere el trabajo que está haciendo otra persona.


## Alta cohesión

Todo agrupamiento de datos debe tener sentido. Todo lo que se agrupe de alguna manera (por ejemplo, en una estructura de datos o en un archivo) debe tener una cercana interrelación.

Esto permite un fácil reemplazo de módulos y un buen orden en el código.


## Con las buenas prácticas se logra que el código tenga:

  * Legibilidad
  * Eficiencia: utilización óptima de los recursos.
  * Robustez y confiabilidad: tolerancia a fallas.
  * Mantenibilidad: facilidad para corregir errores.
  * Adaptabilidad: ante requerimientos cambiantes o nueva funcionalidad.
  * Conformidad con estándares: por ejemplo, para comunicarse con otro programa.
  * Usabilidad: utilizar más fácilmente el código.
  * Menor costo de desarrollo: evaluado en tiempo y dinero.
