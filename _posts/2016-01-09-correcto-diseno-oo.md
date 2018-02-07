---
layout: post
title: Pautas para un correcto diseño orientado a objetos
date: 2016-01-09 19:00:00
categories: poo
tags: resolución_problemas objetos
published: true
---

![ilustración]({{ site.url }}/assets/2016-01-09-correcto-diseno-oo-img1.png)

La primera etapa será la de análisis de la realidad a modelar. A esto se dedica puntualmente un _Analista de Sistemas_. Se debe recordar que un sistema existe independientemente de que esté o no informatizado, por ejemplo: el sistema de ingreso y alta de enfermos de un hospital. De esta manera se debe acotar el universo a la parte que se desea plasmar en el modelo orientado a objetos.

Luego, vendrá la fase de diseño de la solución propuesta. Una vez analizado el sistema a captar en dicha solución, se comienzan a plasmar sus partes en diferentes documentos ([diagramas UML](/poo/2016/01/08/uml.html), casos de uso, [especificación de requisitos (IEEE 830)](/assets/2016-01-09-correcto-diseno-oo-ieee830.doc), ["ConOps" (IEEE 1362)](/assets/2016-01-09-correcto-diseno-oo-ieee1362.doc), etc.)

Es necesario tener en cuenta en todo momento los principios de la POO para que el diseño sea el correcto, ya que un mal diseño conduce a programas difíciles de mantener, modificar y ampliar (problemas de escalabilidad). Para esto es necesario seguir determinadas pautas y buenas prácticas:


## Objetos correctamente identificados

Durante el análisis se detectarán los diferentes objetos que componen el sistema. En este aspecto se debe evitar incluir a un objeto como atributo de otro, en vez de modelarlo como objeto separado.

Una primera aproximación para determinar si algo es un objeto independiente o un atributo de otro objeto puede darse determinando si el mismo tiene más de un atributo que interese a la solución.

_Ejemplo:_

En un objeto "Carrera" que representa una carrera de una universidad, la cantidad de años de duración de la misma puede representarse simplemente mediante un número entero y no será necesario crear un objeto "Duración".

Pero también podría darse la situación en que un objeto tenga un único atributo e incluso así interese representarlo como objeto. Un caso en el que esto se da es cuando el objeto tiene un único atributo pero necesita realizar acciones propias. Otro caso importante se da pensando en la futura escalabilidad y ampliación del sistema.

Como una solución de software representa parte de la realidad y la realidad es cambiante, es necesario dejar "margen" para reflejar estos cambios. Con un buen diseño es posible insertar modificaciones y agregados fácilmente. Con un diseño inadecuado es posible que se deba descartar la solución actual y comenzar desde el principio a rediseñar todo.

_Ejemplo:_

Inicialmente podría incluirse la calificación de un alumno como atributo de otro objeto (por ejemplo, un objeto que represente las cursadas de cada alumno en cada materia). Pero también podría pensarse en que, a futuro, el sistema podría necesitar no sólo indicar la calificación como número (del 1 al 10 por ejemplo) sino un string que indique si ese número representa que el alumno aprobó o desaprobó, entonces podría necesitarse crear un objeto independiente, "Calificacion".

## Atributos correctamente distribuidos:

Al asignar los atributos y responsabilidades a cada objeto se debe tener especial cuidado en distribuirlos de la manera apropiada, es decir, sólo asignar a cada objeto los atributos y responsabilidades que le corresponden y no otros.

_Ejemplo:<_

Si se estuviera modelando un objeto “Estudiante”, se podrían tener como atributos los siguientes: nombre, apellido, dni, legajo, teléfono, dirección, email, carrera, etc. Un atributo que podría intentar agregarse en este caso podría ser el área o escuela a la que el estudiante pertenece. Pero esto depende de la carrera que estudie (si estudia informática, será del área de Tecnología) por lo que, en un correcto modelado, “área” no es un atributo propio del elemento Estudiante. Podría ser, por ejemplo, un atributo del objeto Carrera, con el cual el Estudiante se relaciona.


## Reutilización:

Si varias clases tienen atributos y métodos en común, puede pensarse en crear una superclase y hacer una herencia, incluso si los métodos que comparten tienen distinta implementación, es decir, si tienen el mismo nombre, mismos parámetros y mismo valor de retorno, pero difieren en el funcionamiento interno (esto lleva a una sobrecarga).

_Ejemplo:_

Si tres clases tienen un método para calcular un sueldo, pero en una se calcula sumando una comisión y en las demás no, este método podría colocarse en una superclase, con el cálculo común a todas, y que luego la subclase que requiera modificarlo lo implemente a su manera. Los métodos de la subclase reemplazan en su caso a los de la superclase (sobrecarga de métodos).


## División de responsabilidades:

Cada clase debe tener todas las responsabilidades que le corresponden, según el objeto de la realidad que modelen. Esto significa que no falten métodos que la clase necesite usar por sí misma, ni que incluya funcionalidad que corresponde a otras clases. Una clase se debe crear para representar a una única entidad u objeto de la realidad (por ejemplo, no sería correcto crear una clase "Empresa" que representara tanto a la empresa en su totalidad como también a cada uno de los departamentos que la componen). Una buena división de responsabilidades contribuye a un apropiado [encapsulamiento](/poo/2016/01/08/fundamentos-de-poo.html).

**Construcción de clases necesarias:**

Cuando una entidad es sencilla, se encuentra representada por un pequeño grupo de atributos y no posee responsabilidades propias ni se relaciona con demasiados objetos, el agregar una clase para representarla puede derivar en detrimento de la performance de la aplicación, además de complejidad innecesaria y un mayor costo de mantenimiento.

_Ejemplo:_

Si en una aplicación se debiera representar a un Perro y de éste sólo importa conocer su nombre, además de que no tiene responsabilidades (métodos) propias, no sería una buena práctica el agregar una clase especialmente para representarlo. Bastaría con agregar en la clase que se relaciona con la entidad "Perro" un atributo llamado "perro" de tipo String que represente el nombre del animal.

De todas formas, es fundamental encontrar un buen balance, ya que el resolver el problema con menos clases de las necesarias conduciría a una menor mantenibilidad, a clases más grandes e inmanejables y puede caerse en clases "multiuso" con responsabilidades que no les corresponden.

_Ejemplo:_

Si, en el ejemplo anterior, el objeto Perro fuera utilizado en muchas otras partes de la aplicación, podría evaluarse la posibilidad de colocar una clase especialmente para modelarlo.

Para identificar la real necesidad de cada clase podría ser útil, luego de finalizado el modelo, evaluar cómo sería el diseño si esa clase no existiera y cómo afectaría esto al resto del modelo. Si la funcionalidad de esa clase puede cumplirse dentro del contexto de otra clase, entonces es probable que sea superflua y pueda sustituirse por un atributo.

También puede darse la situación en que dos clases que se relacionan necesiten conocer un mismo dato.

_Ejemplo:_

Una Materia tiene varios Alumnos y un alumno puede inscribirse en varias Materias (es decir, una relación "muchos a muchos", en que ambas partes tienen la cardinalidad múltiple representada por * o _n_). En este caso, la responsabilidad de la calificación de cada estudiante en cada materia no puede colocarse en ninguna de las dos clases porque, si se colocara el atributo "calificacion" en la clase Estudiante, cada estudiante tendría una única calificación por todas las materias y, si se colocara el atributo en la clase "Materia", cada materia tendría la misma calificación para todos los estudiantes. En este caso, es necesario modelar una tercera clase (usualmente se da esta necesidad en las relaciones "muchos a muchos") que relacione a un estudiante, una materia y su calificación.


**Ocultamiento:**

Es importante proveer una interfaz adecuada para utilizar la clase "desde afuera" (es decir, desde otras clases), intentando revelar lo menos posible de la implementación interna. De esta forma, se evita que objetos externos manipulen los miembros de la clase.

Los métodos _getters_ y _setters_ son útiles para manipular el estado interno del objeto desde fuera de él. Por ejemplo, el almacenamiento de un atributo podría escribirse en una base de datos, en un archivo o sólo en la memoria, pero desde fuera de la clase no debería ser necesario lidiar con esto, ya que, si se dejara expuesta esta implementación, un cambio en el tipo de almacenamiento en esta clase provocaría una cadena de cambios en todas las demás clases que la utilizan.

Se debe reconocer también que no todos los atributos deberían tener getters y setters públicos, sino sólo aquellos que vayan a ser utilizados en el resto del programa. Esto se debe evaluar de acuerdo a la complejidad del programa. Cuando un atributo no va a ser nunca accedido desde fuera de su propia clase, sino sólo utilizado dentro de ella, el método getter y el método setter deberían ser privados, ya que ellos revelan el tipo de dato usado para representar al atributo y esto viola parcialmente el encapsulamiento. Por ejemplo, un atributo que guarda datos de conexión a una base de datos que únicamente su propia clase va a usar debería ser privado.

En cuanto a colecciones de objetos, es importante que no sólo se accedan mediante getters y setters, sino que se escriban métodos específicos para manejarlas, por ejemplo, para agregar o eliminar objetos de la colección. Esto es así porque, según el lenguaje de programación, cada tipo de contenedor o colección posee métodos específicos, que pueden tener diferentes nombres y recibir diferente cantidad y tipo de parámetros. Por ejemplo: en Java, para obtener el elemento que se encuentra en determinada posición en una colección de tipo _Vector_, se usa el método <code>elementAt(int indice)</code>, mientras que en una colección de tipo _ArrayList_ se usa <code>get(int indice)</code>.

Si se obligara al usuario de esta clase a saber qué método elegir para obtener un elemento de la colección, no sólo se estaría violando el ocultamiento (se devela qué tipo de colección se está usando) sino que el código sería inmantenible en caso de que se decidiera (por motivos de performance o lo que fuere) cambiar el tipo de colección usada, ya que todas las instrucciones usadas para agregar elementos deberían modificarse para utilizar el método correcto para el nuevo tipo de colección.

Entonces, en el caso de las colecciones, siempre es necesario crear métodos propios para las operaciones que se van a necesitar (por ejemplo, agregarElemento y eliminarElemento), que en su implementación utilicen los métodos provistos por la estructura escogida. Si necesitara cambiarse la estructura, simplemente se cambia una única línea dentro del método propio (en el ejemplo dado, se cambiaría </code>coleccion.elementAt(indice)</code> por <code>coleccion.get(indice)</code> si se estuviera trabajando con Vector y se deseara cambiar por ArrayList).
