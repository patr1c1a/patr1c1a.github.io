---
layout: post
title: Fundamentos de la Programación Orientada a Objetos
date: 2016-01-08 19:00:00
categories: poo
tags: objetos resolución_problemas
published: true
---

Hay ciertos principios que caracterizan a la Programación Orientada a Objetos y a la estructura que se le da a las soluciones de software diseñadas dentro de este paradigma.

Cuando se modela la realidad para captarla en un sistema de software, deben respetarse estos principios si se desea obtener un diseño correctamente orientado a objetos.

&nbsp;

## Herencia:

Es posible que varios objetos tengan características comunes y entonces se podría concluir que son diferentes clases de un mismo "tipo". Entonces, se podría definir una "superclase" (también llamada "clase base" o "padre") que tenga los atributos y métodos comunes que todas las subclases (o "clases hijas") compartirán. La herencia representa una generalización: la superclase es más general y las subclases son más específicas. Cada subclase tendrá todos los atributos y métodos de la clase padre, además de poder tener los propios. Coloquialmente, suele representarse a la herencia con la relación "es un": si tenemos la clase Animal y la subclase Gato, entonces un objeto Gato "es un" Animal.

_Ejemplo:_

Si se diseña el sector de recursos humanos de una empresa, los objetos "Empleado", podrían tener como atributos su nombre, fecha de nacimiento, legajo, domicilio, etc. Pero probablemente cada tipo de empleado tenga características propias que no comparte con otros; por ejemplo, un empleado de ventas podría tener bonificaciones de acuerdo a sus ventas mensuales, pero un empleado administrativo no las tendrá. Así, podría hacerse una especialización, desprendiendo sub-categorías de la clase inicial "Empleado": Ventas, Administración, Ejecutivos, etc. Así, la herencia permite que las clases puedan descomponerse en otras más específicas, "heredando" las características comunes pero luego manteniendo para sí mismas las que no comparten.

En el ejemplo anterior, cada uno de los tipos de empleados sería una subclase que hereda los atributos comunes de la clase "Empleado" (si no hubiera nada que los diferencie de la superclase, no habría necesidad de tener subclases). A la vez, dentro de una subclase, podrían desarrollarse otras divisiones: de la clase Empleado podría desprenderse la subclase Comercialización y de ella podrían desprenderse Administrativo y Ventas. Cada uno de ellos, además de tener las características generales de su superclase, tendrá características propias. Cada subclase heredará los mismos atributos y métodos que todas las subclases de las cuales hereda.

Algunos lenguajes, como C++, permiten herencia múltiple (es decir, que una clase herede de dos o más superclases a la vez). Java no tiene esta funcionalidad, aunque puede emularse mediante otras técnicas.

Otro concepto de interés es el de "**clase abstracta**". Se trata de clases que no pueden instanciarse (es decir, no se pueden obtener objetos de ese "molde"), porque solo están destinadas a ser heredadas. En el ejemplo de la clase "Empleado", podría considerarse a ésta como clase abstracta, para que sólo se permita crear objetos de un tipo de empleado determinado, y no del tipo genérico. Entonces, la clase abstracta sólo sirve para agrupar características comunes sin tener que repetir código en cada una de las subclases.

Además de clases abstractas, pueden crearse también métodos abstractos. Estos métodos se utilizan cuando todas las subclases necesitan el mismo método pero lo calculan de diferente manera. Por ejemplo, un método para calcular el sueldo del empleado sería común a todos ellos (ya que todos cobrarán un sueldo), pero el vendedor incluirá los bonos por ventas mensuales, el sueldo de un ejecutivo tal vez dependa del valor de las acciones de la empresa, etc.

Estos métodos abstractos sólo están declarados (esto significa que solo se incluye la firma del método) pero no implementados en la clase abstracta ("Empleado" en este ejemplo). La implementación corresponderá dentro de cada subclase, la cual tendrá el código específico para calcular el método de la manera en que lo necesita.

Los métodos abstractos solo pueden incluirse en clases abstractas y las subclases deben obligatoriamente implementarlos. El método en cada subclase hará sus propios cálculos, independientemente de las otras, pero en ambas el método tendrá la misma firma: el mismo valor de retorno y los mismos parámetros.

Por ejemplo, si se tiene a la clase "Empleado" como abstracta, a la clase "Comercialización" como abstracta y a la vez como subclase de "Empleado", y a las clases "Administrativo" y "Ventas" como subclases de "Comercialización", podría entonces incluirse en "Comercialización" un método abstracto para calcular la remuneración, pero sin implementarlo, para que las clases "Administrativo" y "Ventas" calculen las remuneraciones de maneras diferentes.

![herencia]({{ site.url }}/assets/2016-01-08-fundamentos-de-poo-img1.png)



## Abstracción:

Existen dos enfoques para abstraer un diseño de objetos: desde el punto de vista del modelado se intenta incluir solo lo relevante en un objeto; mientras que desde el punto de vista arquitectural, se busca separar en capas con responsabilidades concretas.

Al modelar deberemos pensar en qué objetos (con sus atributos y métodos) conforman la solución al problema. La abstracción consiste en incluir sólo los elementos que son importantes en la situación que se está modelando y dejar afuera aquellos que no influyen de manera relevante. De la misma forma, al diseñar cada uno de los objetos, se incluirán sólo sus características esenciales: aquellas que lo diferencian de los demás objetos. El foco estará en simplificar objetos omitiendo detalles irrelevantes.

_Ejemplo:_

Si se estuviera modelando el sistema de recursos humanos de una empresa, con sus diferentes tipos de empleados, tal vez exista una clase llamada "Empleado Administrativo". Los objetos instanciados a partir de esta clase deberán tener las características que sean importantes para el sistema: nombre, legajo, antigüedad, etc. Pero hay características que, aunque el empleado las tenga, podrían no ser relevantes para esta solución: estatura, música preferida, comidas a la que es alérgico... Por supuesto, esto depende de los requisitos del sistema a diseñar (si, por ejemplo, en la empresa desearan registrar la comida a la que es alérgico cada empleado porque tienen un servicio de catering, entonces este atributo podria volverse relevante). Asimismo, habrá acciones que interesan respecto de este empleado, como realizar cobranzas, facturación, etc., y serán estas las acciones que se deberán modelar, y no otras. De esta manera, al diseñar se eligen los atributos y métodos pertinentes al objeto modelado, dejando afuera los que no aportan a la solución.

En cuanto al diseño arquitectural de la solución, es necesario dividir el sistema en componentes o capas con responsabilidades claras (ej: UI, lógica, datos), para que cada una se encargue de implementar la lógica necesaria de manera de no depender de las demás capas y exponer solo lo necesario. El foco estará en la organización del sistema en módulos independientes.

_Ejemplo:_

Si se necesita utilizar un servicio externo (una API) del clima para obtener el pronóstico, sería conveniente tener una capa que específicamente se dedicara a comunicarse con ese servicio y que expusiera "hacia afuera" los métodos necesarios (por ejemplo: para obtener pronóstico del día, pronóstico extendido de x cantidad de días, información de precipitaciones, historial, etc.). Otra capa diferente se encargaría de comunicarse con ella para llamar a esos métodos. Y tal vez otra capa más se encargaría de mostrarlos en pantalla de cierta forma que el usuario pueda interpretar.


## Encapsulamiento:

Consiste en incluir dentro de cada clase del modelo todos los recursos que necesita para funcionar (atributos y métodos) de modo que cada clase tenga sentido como una unidad lógica coherente. Es importante determinar qué características (atributos) definen a un objeto y cuáles no son parte de él, así como qué comportamientos (métodos) deben ser propios del objeto y cuáles no. En el ejemplo del empleado administrativo, será importante incluir datos como el nombre, el legajo, etc., ya que éstos no pueden faltar. Los atributos y métodos siempre se desprenderán de la situación a modelar.

Podría decirse que el _encapsulamiento_ complementa a la _abstracción_: mediante la abstracción en el modelado se toman solo los atributos y responsabilidades que se necesita incluir en cada objeto; mediante el encapsulamiento se asegura que a ningún objeto le falte ningún atributo o responsabilidad que deba contemplarse.

El encapsulamiento parece un concepto fácil de aplicar en teoría, pero puede generar muchas dudas a la hora de diseñar. Cuando se modela una solución, se debe velar por que cada objeto modelado contenga todos los atributos y acciones que lo caracterizan dentro de sí mismo, sin necesidad de acceder a otros objetos para obtenerlos.

El encapsulamiento se relaciona intrínsecamente con los conceptos de cohesión y acoplamiento. La primera implica agrupar el código que se refiere a la realización de una misma tarea y, el segundo impide que un objeto realice las tareas de otro o necesite de otro para realizar las propias. Aunque hay casos en que cierto grado de acoplamiento es indispensable, por la naturaleza de los objetos modelados (ya que seguramente éstos tendrán cierta relación entre sí), es deseable producir el menor acoplamiento posible.

_Ejemplo:_

Si se estuviera diseñando la gestión de usuarios de un sistema, seguramente sea necesario guardar la contraseña de acceso de forma encriptada. Pero no sería correcto que la clase Usuario se encargara de encriptar, porque es claro que esa no debería ser responsabilidad de un Usuario, sino de alguna otra clase (una que provea utilidades para trabajar con strings, por ejemplo). La clase Usuario solo debe gestionar datos de usuarios (nombre, email, contraseña encriptada) y, en todo caso, llamar al método de la clase correspondiente para obtener la encriptación. Suponiendo que el sistema tiene también una gestión de ventas, podría ser necesario encriptar los datos de pago de cada venta; pero si la encriptación estuviera dentro de la clase Usuario entonces se debería instanciar un Usuario del sistema solo para poder encriptar, o bien repetir el código de encriptación en la clase Venta (con el consecuente problema que se genera si en algún momento debe modificarse el algoritmo de encriptación a usar).

## Ocultamiento:

Muchas veces se confunde al ocultamiento con el encapsulamiento, pero en realidad son dos conceptos diferentes.

Los objetos se comunicarán entre sí ejecutando métodos ("enviándose mensajes"), sin conocer "desde afuera" cómo es que el objeto receptor procesa la información, ni cómo el objeto está compuesto. Esto significa que es necesario que los objetos no revelen su implementación completamente, escondiendo los detalles que no debería ser necesario conocer desde otras clases. Una clase solo debe revelar a su exterior (otras clases) la información que otras clases necesitarán para interactuar con ella. En definitiva, los métodos hacen de intermediarios entre los objetos para que éstos interactúen, pero dando a conocer la menor cantidad de información posible al objeto que los invoca.

_Ejemplo:_

En el modelado de un reproductor de audio, podría ser deseable tener una memoria cache que almacene internamente los archivos ejecutados recientemente, para no tener que volver a cargarlos cada vez que se los ejecuta. Desde otros objetos probablemente no interese saber que la clase maneja una cache ni saber cómo la implementa, pero al reproductor le sirve tenerla para poder ser más eficiente en su funcionamiento. Entonces la cache es un detalle interno de implementación que no debe exponerse hacia afuera.


## Polimorfismo:

Permite que una misma representación incluya varias implementaciones. Aunque el polimorfismo también tiene distintos enfoques:

- Subtipado: cada objeto de una subclase se considera, a la vez, un objeto de la superclase, y esto permite usar una clase hija cuando se espera un objeto de la clase padre.
- Sobreescritura de métodos ("override"): un método heredado puede redefinirse para tener una implementación diferente a la de la clase padre.
- Sobrecarga de métodos ("overload"): múltiples versiones de un método (el mismo nombre, pero distintos tipos o cantidad de parámetros).

_Ejemplo:_

Tomando el ejemplo de la clase Empleado y sus subclases, los objetos de tipo "Administrativo" son a la vez objetos "Comercialización" y también objetos "Empleado". Entonces, los objetos de tipo "Comercialización" tendrán todas las características de los objetos de tipo "Empleado" (los atributos "nombre", "fecha de nacimiento", "domicilio") y también características propias (por ejemplo, un atributo booleano llamado "esPasante" que indica si el empleado está sujeto a un régimen de pasantía o no). De la misma forma, un objeto de tipo Ventas tendrá todos las características de los objetos de tipo Empleado y los de tipo Comercialización (nombre, fecha de nacimiento, domicilio, esPasante) y las suyas propias (por ejemplo, un atributo llamado "porcentaje" que indique el porcentaje que le corresponde sobre las ventas que realice). Si lo visualizamos en forma de subconjuntos:

![polimorfismo]({{ site.url }}/assets/2016-01-08-fundamentos-de-poo-img2.png)

Entonces, podría usarse un objeto de tipo Administrativo cuando se requiere uno de tipo Empleado, puesto que un Administrativo "es un" Empleado. En algunos lenguajes es común definir algunos objetos usando una interfaz para declararlos y una clase concreta para instanciarlos: `List<String> lista = new ArrayList<String>();`.

En cuanto a la sobreescritura, se podría tener en la clase Empleado (superclase) una implementación del método `calcularSueldo()` y luego algunas de las clases hijas definir el mismo método `calcularSueldo()` con una implementación propia si se trata de un tipo de empleado que tiene una fórmula diferente al resto para calcularlo.

Siguiendo la misma línea, si durante los meses de mayor demanda y trabajo más intenso se requiere calcular el sueldo de los empleados teniendo en cuenta un bono extra, la clase Empleado podría tener el método `calcularSueldo()` para cuando no hay bonos y `calcularSueldo(double bono)` cuando sí lo hay (ambos métodos tienen el mismo nombre pero distinta "firma", ya que cambia la lista de parámetros).

En Java, el polimorfismo se ve reflejado en la herencia de clases, la sobrecarga y la sobreescritura de métodos pero, en otros lenguajes como Python, también existe la sobrecarga de operadores.
