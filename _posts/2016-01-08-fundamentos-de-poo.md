---
layout: post
title: Fundamentos de la Programación Orientada a Objetos
date: 2016-01-08 19:00:00
categories: poo
published: true
---

Hay ciertos principios que caracterizan a la Programación Orientada a Objetos y a la estructura que se le da a las soluciones de software diseñadas dentro de este paradigma.

Cuando se modela la realidad para captarla en un sistema de software, deben respetarse estos principios si se desea obtener un diseño correctamente orientado a objetos.

&nbsp;

## Abstracción:

Permite descomponer un problema y reducir su complejidad. Al diseñar la solución a un problema, se deberá pensar en qué objetos (con sus atributos y métodos) la conforman. La abstracción consiste en incluir sólo los elementos que son importantes en la situación que se está modelando y dejar afuera aquellos que no influyen de manera relevante. De la misma forma, al diseñar cada uno de los objetos, se incluirán sólo sus características esenciales: aquellas que lo diferencian de los demás objetos.

_Ejemplo:_

Si se estuviera modelando el sistema de recursos humanos de una empresa, con sus diferentes tipos de empleados, tal vez exista una clase llamada "Empleado Administrativo". Los objetos instanciados a partir de esta clase deberán tener las características que sean importantes para el sistema: nombre, legajo, antigüedad, etc. Pero hay características que, aunque el empleado las tenga, podrían no ser relevantes para esta solución: estatura, música preferida, comidas a la que es alérgico... Por supuesto, esto depende de los requisitos del sistema a diseñar (si, por ejemplo, en la empresa desearan registrar la comida a la que es alérgico cada empleado porque tienen un servicio de catering, entonces este atributo se volvería relevante).

Asimismo, habrá acciones que interesan respecto de este empleado, como realizar cobranzas, facturación, etc., y serán estas las acciones que se deberán modelar, y no otras.

De esta manera, al diseñar se eligen los atributos y métodos pertinentes al objeto modelado, dejando afuera los que no aportan a la solución.

## Encapsulamiento:

Consiste en incluir dentro de cada clase del modelo todos los recursos que necesita para funcionar (atributos y métodos). Es importante determinar qué características (atributos) definen a un objeto y cuáles no son parte de él, así como qué comportamientos (métodos) deben ser propios del objeto y cuáles no. En el ejemplo del empleado administrativo, será importante incluir datos como el nombre, el legajo, etc., ya que éstos no pueden faltar.

Los atributos y métodos siempre se desprenderán de la situación a modelar, aplicando la abstracción.

Podría decirse que el _encapsulamiento_ complementa a la _abstracción_: mediante la abstracción se toman sólo los atributos y responsabilidades que se necesita modelar de cada objeto; mediante el encapsulamiento se asegura de que a ningún objeto le falte ningún atributo o responsabilidad que deba contemplarse.

El encapsulamiento parece un concepto fácil de aplicar en teoría, pero puede generar muchas dudas a la hora de diseñar. Cuando se modela una solución, se debe velar por que cada objeto modelado contenga todos los atributos y acciones que lo caracterizan dentro de sí mismo, sin necesidad de acceder a otros objetos para obtenerlos.

El encapsulamiento se relaciona intrínsecamente con los conceptos de cohesión y acoplamiento. La primera implica agrupar el código que se refiere a la realización de una misma tarea y, el segundo impide que un objeto realice las tareas de otro o necesite de otro para realizar las propias. Aunque hay casos en que cierto grado de acoplamiento es indispensable, por la naturaleza de los objetos modelados (ya que seguramente éstos tendrán cierta relación entre sí), es deseable producir el menor acoplamiento posible.

## Ocultamiento:

Muchas veces se incluye al ocultamiento como encapsulamiento, pero en realidad son dos conceptos diferentes.

Los objetos se comunicarán entre sí ejecutando métodos ("enviándose mensajes"), sin conocer "desde afuera" cómo es que el objeto receptor procesa la información, ni cómo el objeto está compuesto. Esto significa que es necesario que los objetos no revelen su composición (atributos y métodos) completamente. Es decir, desde otros objetos no debería saberse que la clase "EmpleadoAdministrativo" tiene un atributo "nombre" de tipo "String", ni debería ser necesario deducir "desde afuera" cómo un método realiza el cálculo de un sueldo. El objeto sólo debe revelar a su exterior (otras clases) cuáles son los métodos que desea que otros objetos utilicen de él, y qué datos reciben y devuelven.

En definitiva, los métodos hacen de intermediarios entre los objetos para que éstos interactúen, pero dando a conocer la menor cantidad de información posible al objeto que los invoca.

Un buen ocultamiento es clave para generar una alta cohesión y bajo acoplamiento entre objetos.

## Herencia:

Cuando se modelan objetos, es posible definir características comunes a varios de ellos.

_Ejemplo:_

Si se diseña el sector de recursos humanos de una empresa, los objetos "Empleado", podrían tener como atributos su nombre, fecha de nacimiento, legajo, domicilio, etc. Pero probablemente cada tipo de empleado tenga características propias que no comparte con otros, por ejemplo, un empleado de ventas podría tener bonificaciones de acuerdo a sus ventas mensuales, pero un empleado administrativo no las tendrá. Así, podría hacerse una especialización, desprendiendo sub-categorías del objeto inicial "Empleado": Ventas, Administración, Ejecutivos, etc.

Así, la herencia permite que las clases puedan descomponerse en otras más específicas, "heredando" las características comunes pero luego manteniendo para sí mismas las que no comparten. De esta manera, suele llamarse "superclase" a la clase más general, y "subclase" a las clases más específicas.

En el ejemplo anterior, cada uno de los tipos de empleados sería una subclase que hereda los atributos comunes de la clase "Empleado" (si no hubiera nada que los diferencie de la superclase, no habría necesidad de herencia). A la vez, dentro de una subclase, podrían desarrollarse otras subdivisiones: de la clase Empleado podría desprenderse la subclase Comercialización y de ella podrían desprenderse Administrativo y Ventas. Cada uno de ellos, además de tener las características generales de su superclase, tendrá características propias. Cada subclase heredará los mismos atributos y métodos que todas las subclases de las cuales hereda.

Algunos lenguajes, como C++, permiten herencia múltiple (es decir, que una clase herede de dos o más superclases a la vez). Java no tiene esta funcionalidad, aunque puede emularse mediante otras técnicas.

Otro concepto de interés es el de "**clase abstracta**". Se trata de clases que no pueden instanciarse (es decir, no se pueden obtener objetos de ese "molde"), porque están destinadas sólo a ser heredadas. En el ejemplo de la clase "Empleado", podría considerarse a ésta como clase abstracta, para que sólo se permita crear objetos de un tipo de empleado determinado, y no del tipo genérico. Entonces, la clase abstracta sólo sirve para agrupar características comunes sin tener que repetir código en cada una de las subclases.

Además de clases abstractas, pueden crearse también métodos abstractos. Estos métodos se utilizan cuando todas las subclases necesitan el mismo método pero lo calculan de diferente manera. Por ejemplo, un método para calcular el sueldo del empleado sería común a todos ellos (ya que todos cobrarán un sueldo), pero el vendedor incluirá los bonos por ventas mensuales, el sueldo de un ejecutivo tal vez dependa del valor de las acciones de la empresa, etc.

Estos métodos abstractos sólo están declarados (es decir, sólo se incluye la firma del método) pero no implementados en la clase abstracta ("Empleado" en este ejemplo). La implementación corresponderá dentro de cada subclase, la cual tendrá el código específico para calcular el método de la manera en que lo necesita.

Los métodos abstractos sólo pueden incluirse en clases abstractas y las subclases deben obligatoriamente implementarlos. El método en cada subclase hará sus propios cálculos, independientemente de las otras, pero en las dos el método tendrá la misma firma: el mismo valor de retorno y los mismos parámetros.

Por ejemplo, si se tiene a la clase "Empleado" como abstracta, a la clase "Comercialización" como abstracta y a la vez como subclase de "Empleado", y a las clases "Administrativo" y "Ventas" como subclases de "Comercialización", podría entonces incluirse en "Comercialización" un método abstracto para calcular la remuneración, pero sin implementarlo, para que las clases "Administrativo" y "Ventas" calculen las remuneraciones de maneras diferentes.

![herencia]({{ site.url }}/assets/2016-01-08-fundamentos-de-poo-img1.png)


## Polimorfismo:

Permite que una misma representación incluya varias implementaciones. Cada objeto de una subclase se considera, a la vez, un objeto de la superclase. En Java, el polimorfismo se ve reflejado en la herencia de clases, la sobrecarga y la sobreescritura de métodos (en otros lenguajes, como Python, también existe la sobrecarga de operadores).

_Ejemplo:_

Tomando el ejemplo anterior, los objetos de tipo "Administrativo" son a la vez objetos "Comercialización" y también objetos "Empleado". Entonces, los objetos de tipo "Comercialización" tendrán todas las características de los objetos de tipo "Empleado" (los atributos "nombre", "fecha de nacimiento", "domicilio") y también características propias (por ejemplo, un atributo booleano llamado "esPasante" que indica si el empleado está sujeto a un régimen de pasantía o no). De la misma forma, un objeto de tipo Ventas tendrá todos las características de los objetos de tipo Empleado y los de tipo Comercialización (nombre, fecha de nacimiento, domicilio, esPasante) y las suyas propias (por ejemplo, un atributo llamado "porcentaje" que indique el porcentaje que le corresponde sobre las ventas que realice).
  
Podría visualizarse esto en forma de subconjuntos:

![polimorfismo]({{ site.url }}/assets/2016-01-08-fundamentos-de-poo-img2.png)
