---
layout: post
title: Qué es POO (Programación Orientada a Objetos)
date: 2016-01-07 19:00:00
categories: poo
tags: objetos
published: true
---

## Los objetos

La Programación Orientada a Objetos (abreviada usualmente como "POO" o, en inglés, "OOP") es un paradigma de programación basado en "objetos", que contienen atributos que los caracterizan así como métodos (acciones que pueden realizar estos objetos) para interactuar.

Un objeto refleja algo de la vida real, un elemento del universo que se desea representar. Para esto cuenta con características propias (atributos), que tendrán un estado o un valor determinado. Además, tiene comportamientos y responsabilidades propios, los cuales se implementan mediante "métodos". Mediante los objetos se intenta "modelar" aquellos elementos que componen una solución de software, por lo que pueden crearse objetos muy diversos a la medida de las necesidades. Por ejemplo, si se está diseñando un programa para gestionar las ventas de una empresa, probablemente haya objetos como "Artículo", "Venta", "Cliente", "Vendedor", etc.

Un concepto importante en la programación orientada a objetos es la responsabilidad de cada uno de ellos: al definir la realidad que se desea modelar (por ejemplo, un sistema para un almacén, un hospital, etc.) se determinan los objetos que la componen y a cada uno de ellos se le asignan acciones (métodos). Un objeto correctamente modelado tendrá un comportamiento bien definido y adecuado a su naturaleza. Por ejemplo, si se está modelando un almacén que cuenta con un empleado que se encarga de vender y uno encargado de cobrar, no se debería asignar el cobro al vendedor, ya que no es su responsabilidad.

Los objetos se relacionan entre sí, cada uno desempeñando un rol y con ciertas responsabilidades. Un objeto puede provee un servicio o ejecutar acciones que son usadas por otros objetos, y esto es realizado a través de sus métodos.

Los métodos son muy similares a las funciones utilizadas en la programación imperativa, ya que pueden recibir parámetros y retornar un valor. La diferencia es que un método pertenece a un objeto particular, por lo que la invocación deberá hacerse a partir de ese objeto.



## El nacimiento de un objeto: las Clases

Una clase es un "molde" para crear objetos con una misma estructura. A partir de una clase pueden obtenerse objetos. Todos los objetos obtenidos mediante una clase tendrán los mismos atributos y los mismos métodos. A cada objeto obtenido de este "molde" se lo llama "instancia" de esa clase.

Lo que diferencia a dos instancias de una misma clase son los valores que contienen sus atributos. Los valores concretos que adopte el objeto durante su "existencia" darán un "estado" a ese objeto.

Los nombres de las clases comienzan con la primera letra en mayúscula. Además, no pueden contener espacios ni caracteres especiales (como tildes). Esto es una convención que se suele seguir, aunque el lenguaje de programación que utilicemos permita lo contrario.

El usuario programador puede crear tantas clases como sea necesario. Además, los lenguajes de programación orientados a objetos habitualmente contienen librerías con clases ya implementadas y listas para usar (es el caso de la clase String en Java).

Al instanciar un objeto (es decir, crear un objeto a partir de una clase) normalmente se le da un nombre, ya que este objeto no es otra cosa que una variable. Al ser los objetos variables que contienen más de un dato (sus atributos y sus métodos) se implementan como punteros. Es decir, un objeto será una variable que contendrá la dirección de memoria donde los datos están alojados.

_Ejemplo 1:_

Una clase llamada "Ventana" podría representar una ventana de un programa.
  
Sus atributos podrían ser: _ancho_, _alto_ y _color_, y sus métodos _minimizar_, _maximizar_, _cerrar_ y _estaActiva_.
  
Cada uno de los métodos estará programado de manera que permitirá realizar una acción. Una buena práctica es que el nombre del método indique claramente la acción que éste realiza.
  
Los métodos de _minimizar_, _maximizar_ o _cerrar_ la ventana probablemente necesiten más datos para trabajar, entonces no recibirán ningún parámetro ni devolverán ningún dato, ya que su única función es la de efectuar una acción. El método _estaActiva_ podría definirse como de tipo booleano, devolviendo "true" o "false" según la ventana esté o no activa en la pantalla del usuario al momento en que el método es ejecutado.
  
Ahora supongamos que este programa puede tener más de una ventana funcionando a la vez. Entonces podrían hacerse dos instancias diferentes de la clase Ventana. Entonces, se podría crear el objeto (instancia de Ventana) llamado _ventana1_, que tenga como valores: _ancho = 750; alto = 600; color = white_; y el objeto _ventana2_, con los siguientes valores: _ancho = 500; alto = 450; color = grey_. Es decir, ventana1 y ventana2 tienen los mismos atributos, pero en cada instancia los atributos tienen distintos valores (estado del objeto).
  
Ambos objetos tendrán los métodos minimizar, maximizar, cerrar y estaActiva, que funcionarán de igual manera para ambos.


## Los miembros de un objeto: atributos y métodos

### Atributos

Los atributos son las características que hacen a la naturaleza de un objeto y lo diferencian del resto. En la implementación (es decir, al escribir el código), el concepto de "atributo" puede asimilarse al de "variable": un espacio de memoria que permite almacenar un valor de determinado tipo.

Los atributos que conforman un objeto pueden ser de distintos tipos, incluso, otros objetos. En algunos lenguajes, como Java, un atributo puede ser de un tipo primitivo (números enteros o en punto flotante, caracteres ascii, booleanos, etc.) u otro objeto. Los tipos primitivos son tipos de datos definidos en el lenguaje y no pertenecen a ninguna clase (ya que no son "objetos"). Los atributos que son del tipo de algún objeto, internamente, se manejan con _punteros_ (el atributo será un puntero con la dirección de memoria donde el objeto al que hace referencia se encuentra alojado).

Además, pueden crearse contenedores o colecciones de objetos. Cada lenguaje provee diferentes maneras de agrupar objetos: arreglos, listas, conjuntos, mapas, etc.

_Ejemplo 2:_

Un objeto para representar un vuelo en una aerolínea podría obtenerse de una clase llamada "Vuelo" y tener como atributos que lo caracterizan a los siguientes: código, origen, destino, avión, tripulación, pasajeros, etc.
  
Algunos de estos atributos podrían ser datos primitivos (_código_ podría ser de tipo entero, _origen_ y _destino_ de tipo string) o bien un objeto de alguna clase (el _avión_ podría representarse mediante un objeto, ya que seguramente tendrá más de un atributo y no basta con un tipo primitivo para este dato) o contenedores de objetos (la _tripulación_ seguramente será una colección de tripulantes, representando a cada tripulante mediante un objeto, y los _pasajeros_ serán otra colección, representando a cada pasajero como un objeto).
  
Así, de esta clase "Vuelo" se instanciará un objeto por cada vuelo que la aerolínea realice, y cada uno tendrá su propio código, lugar de origen y destino, su propia tripulación y sus propios pasajeros.

### Métodos

Un método es alguna acción que se ejecuta en el programa. Están contenidos dentro de clases y dan funcionalidad a los objetos. Las acciones que un objeto realiza son llevadas a cabo mediante métodos, que se asemejan a los procedimientos y funciones de la programación estructurada y pueden recibir datos (parámetros) y devolver otros, o bien no recibir ni devolver nada. Tanto los parámetros como los datos que el método devuelve pueden ser de tipo primitivo u objetos.

Ul método podría requerir determinados datos para trabajar (por ejemplo, si el método ejecutara la acción de sumar, necesitaría los valores a sumar entre sí) y podría devolver un resultado (en el caso de la suma, devolverá el valor resultante de la operación). También es posible encontrar métodos que no reciban ni devuelvan información (por ejemplo, un método que se dedique a escribir un determinado valor en una base de datos). A la información que un método recibe se la llama "parámetro", y son simplemente nombres de variables (u objetos) con su tipo. Cuando el método devuelve un valor determinado, se dice que el tipo de ese valor es el "tipo" del método (en el caso de un método "suma" que devuelve un valor entero, podría decirse que el método "suma" es de tipo entero).

En muchos lenguajes, como Java o Python, el retorno de un valor se realiza mediante la palabra clave "return". Por ejemplo: return resultado. Cuando el valor retornado es nulo (es decir, no existe), puede utilizarse alguna palabra clave como "void" (Java), o nada.

Por convención, los nombres de los métodos se colocan como verbos en minúscula y con cada palabra intermedia comenzando en mayúscula (como los nombres no pueden contener espacios, se colocan las palabras a continuación unas de otras). Además, no pueden contener caracteres especiales, como tildes o símbolos.

Dentro de un método también pueden existir variables locales, que sólo son conocidas en el ámbito de ese método. Estas variables pueden ser de tipos primitivos u objetos.

_Ejemplo 3:_

<span class="ejemplo">Método en Java que recibe dos parámetros String y retorna String</span>:

<pre><code>public String unirFrases (String frase1, String frase2){ 
   String fraseCompleta = " "; 
   fraseCompleta = frase1 + " " + frase2; 
   return fraseCompleta; 
}</code></pre>

Un método puede invocarse (ejecutarse) desde el mismo objeto que lo contiene o desde afuera (otros objetos). Normalmente, para invocar un método se comienza por el nombre del objeto al que pertenece, seguido de un punto y luego el nombre del método con sus argumentos entre paréntesis, de la siguiente manera: <code>objeto.metodo(argumento1, argumento2); </code>

_Ejemplo 4:_

Supongamos que existe una clase "Estudiante" con un atributo "legajo" y otro atributo "carrera", y que tiene un método que permite asignarle un valor al atributo "carrera", llamado "asignarCarrera", que recibe como parámetro un string y no retorna nada.
  
Si se instancia un objeto de tipo "Estudiante" llamado estudiante1 (este será el nombre de la variable) y se desea asignarle un valor al atributo "carrera", entonces podría llamarse al método de la siguiente forma: <code>estudiante1.asignarCarrera("diseño gráfico");</code>

![gráfico de objeto]({{ site.url }}/assets/2016-01-07-programacion-orientada-a-objetos-img1.png)

## Para terminar.. la definición de Steve Jobs

En 1994 Steve Jobs dio una entrevista para la revista Rolling Stone donde le pidieron que describiera de manera sencilla la programación orientada a objetos. Esta fue su respuesta:

_"Los objetos son como las personas. Son cosas vivientes y que respiran, que tienen conocimiento dentro de ellos sobre cómo hacer cosas y además tienen memoria para recordar cosas. Y en vez de interactuar con ellos a un muy bajo nivel, interactúas con ellos a un nivel muy alto de abstracción, de la misma forma que nosotros lo estamos haciendo en este momento._

_Aquí hay un ejemplo: si yo soy tu objeto lavandería, podrías darme tu ropa sucia y enviarme un mensaje que diga '¿Podrías lavar esta ropa, por favor?'. Yo casualmente sé cuál es la mejor lavandería de San Francisco. Y además hablo inglés y tengo dólares en mis bolsillos. Entonces salgo, paro un taxi y le digo al conductor que me lleve a ese lugar de San Francisco. Hago que laven tu ropa, me vuelvo a subir al taxi y vuelvo aquí. Te doy tu ropa limpia y te digo 'Aquí tienes tu ropa limpia'._

_Tu no tienes idea de cómo lo hice. no conoces la lavandería. Tal vez incluso hables francés y no puedas parar un taxi, no puedas pagarlo, no tengas dólares en tus bolsillos. Sin embargo, yo sabía cómo hacer todo eso. Y tu no tuviste que saber nada. Toda la complejidad estaba escondida dentro mío, y pudimos interactuar a un alto nivel de abstracción. Eso es lo que son los objetos. Ellos encapsulan complejidad, y las interfaces de esa complejidad están a alto nivel."_
