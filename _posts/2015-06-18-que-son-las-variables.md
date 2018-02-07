---
layout: post
title: Qué son las variables
date: 2015-06-18 11:00:00
categories: conceptos
tags: datos tipos variables
published: true
---


Probablemente uno de los primeros conceptos con que se encuentra cualquier novel programador es el de **variable**. La forma más sencilla de definirla es como un dato que puede variar. Normalmente se la contrapone al concepto de **constante**, que es lo opuesto: un dato que no podrá variar nunca.

> ¿Qué significa que un dato puede variar y otro no? Claramente este concepto no se refiere a que el programador escribirá un dato y nunca más podrá borrarlo (como si de pintura rupestre se tratara), sino que la posibilidad de variar -o no- se da durante la ejecución del programa. Como ejemplo podría darse la puntuación de un jugador en un videojuego: al iniciar el juego su puntuación será 0, pero al ir avanzando seguramente este número aumentará o disminuirá (de acuerdo al desarrollo del juego), haciendo que este dato sea _variable_. En cambio, el tamaño de la ventana del juego podría ser invariable (sin posibilidad de que el usuario lo modifique) y entonces ser _constante_.

Otra manera de definir a una variable es como una "caja" vacía en la que se guardará un dato, que luego puede cambiarse por otro similar. Es decir, esta "caja" representa un dato concreto del programa que estamos haciendo, y cada vez que necesitemos usar ese dato lo tomaremos de esa caja, sin importar cuál es su contenido. En el ejemplo de la puntuación de un videojuego podemos imaginar que la caja tiene un rótulo que dice "puntuación" y adentro está guardado el número que representa a esta puntuación, pero no importa si ese número es el 10, el 157 o el 2.345, sino que basta con conocer lo que ese número significa (la puntuación del jugador).

## Las variables en la memoria RAM

Si vamos concretamente a la **memoria RAM** de una computadora, las variables estarán guardadas en dicha memoria. Cada "espacio" o "ubicación" en la memoria es una "caja" donde puede guardarse sólo un dato o parte de un dato (pero nunca más de un dato a la vez). Estas ubicaciones de memoria se identifican mediante **direcciones** numéricas, generalmente expresadas en sistema hexadecimal (por ejemplo, la dirección 1A2F -el número 6703 en sistema decimal- podría ser una dirección de memoria). Las direcciones de memoria son correlativas.

> Muchas veces se identifica a las direcciones de memoria con un formato similar al siguiente: **0x1A2F**, donde "0x" indica que lo que sigue es un número hexadecimal.

![direcciones de memoria](/assets/2015-06-18-que-son-las-variables-img1.jpg)

Las computadoras modernas suelen almacenar 8 bits en cada espacio de memoria. Cuando se necesita almacenar algo que requiere más de 8 bits de tamaño, entonces se divide en varias direcciones y, si se requiere almacenar algo que puede representarse con menos de 8 bits (por ejemplo, el número 14, que en binario es el 1110), se rellena con ceros hasta abarcar los 8 bits mínimos (así, el 1110 queda almacenado como 00001110).

Lo que se almacena dentro de cada ubicación de memoria es un número binario (que es lo que la computadora conoce), por ejemplo: 01010010. Éste puede representar cualquier cosa: una letra, un número, un color, etc. La memoria sólo se encarga de almacenarlo y dejarlo ahí hasta que algún programa le indique que lo reemplace por otro dato, o bien hasta que se apague la computadora (ya que la RAM es memoria "volátil", lo que significa que sus datos sólo se guardan mientras tenga electricidad). De la interpretación se encargan luego los programas (que serán los que digan si ese 01010010 representa al número 82 en decimal, a la letra &#8216;R&#8217; o bien alguna otra cosa). La mayoría de lenguajes de programación tienen tipos de datos estructurados que nos ayudan a definir de qué tipo es cada dato almacenado en la memoria. Así, en muchos lenguajes podemos decir que las variables son de un determinado [tipo de dato](/conceptos/2015/06/18/tipos-de-datos.html).

> La conversión entre números decimales y binarios es inmediata mediante ciertos cálculos (fácilmente podemos deducir que el 01010010 es el 82 en sistema decimal), pero para definir que el número 01010010 es la letra "R" hay una tabla, llamada **ascii**, que fue creada para asociar cada carácter del alfabeto con un número que lo representa; de esta manera la computadora puede almacenar letras en el sistema que ella conoce: el de los números binarios.

Cuando un programa está en ejecución, el _sistema operativo_ gestiona el uso de la memoria y decide en qué parte guardar cada dato de este programa. Normalmente, la ubicación en la memoria va a depender de varios factores (por ejemplo, qué sectores de la memoria están libres en ese momento), y el programador no puede saber de antemano dónde quedará almacenado cada dato que su programa usa. En el ejemplo del videojuego: no podemos saber si la puntuación se guardará siempre en la misma dirección de la memoria y, lo más probable es que cada vez que el usuario inicie el juego la puntuación se almacene en direcciones diferentes. Además, cada lenguaje y cada compilador representa los datos de distinta manera: por ejemplo, el compilador Turbo Pascal representa los números enteros usando 16 bits (es decir, cada número ocupa 2 ubicaciones de memoria) mientras que GCC los representa mediante 32 bits (4 ubicaciones de memoria). Si el puntaje del jugador en el videojuego es un número entero y el programa se está escribiendo en lenguaje C, compilado con GCC, entonces ese puntaje abarcará 4 ubicaciones de memoria contiguas, identificadas por la dirección de la primera. Por ejemplo, si el puntaje es 76.132, este número en binario es el 10010100101100100, que ocupa 17 bits y debe rellenarse con ceros al principio para abarcar los 32 bits que usa GCC para representar un número entero. En la memoria, quedaría algo como la siguiente imagen:

![76132 en memoria](/assets/2015-06-18-que-son-las-variables-img2.jpg)

En el ejemplo, suponemos que el videojuego se está ejecutando y el número 76.132 está almacenado en la dirección de memoria 0x0042F2 (y las tres ubicaciones adyacentes). Pero, como se dijo antes, en la siguiente ejecución podría quedar almacenado en otra dirección totalmente diferente. Además, es imposible que el programador pueda prever cuál será la dirección de memoria que le corresponderá a este dato en cada ejecución del programa. Para evitar estos inconvenientes, lo que se hace es darle un nombre simbólico o **identificador**. Esto es lo que conocemos con la denominación de **variable**. Así, el programador puede decir que ese dato se va a identificar con el nombre "puntaje", independientemente de dónde quede almacenado en la memoria. Luego habrá mecanismos más complejos (que exceden al concepto de variable) que permiten asociar ese identificador con la dirección que le corresponde, para saber dónde está el dato al que el programador llamó "puntaje" e ir a buscarlo dentro de la memoria cada vez que el código del programa mencione a la variable "puntaje".

## Las variables en el código de un programa

Las variables se ven en el código. Un usuario nunca sabrá de su existencia, a menos que sea un entendido en el tema. El usuario sólo se limita a usar el programa, sin saber cómo están los datos distribuidos, qué tipos de variables se emplearon ni cuántas.

El programador usará variables, como ya se ha dicho, para almacenar datos que puedan adoptar diferentes valores a lo largo de la ejecución del programa, o bien que no estén definidos hasta que el programa se inicia. Por ejemplo, si el programa empieza solicitando al usuario que ingrese su edad, este dato seguramente no cambiará durante toda la ejecución (al menos hasta que ese usuario cierre el programa y un usuario diferente -con otra edad- lo vuelva a iniciar), pero es un dato que se desconoce hasta luego de que el programa se empezó a ejecutar, por lo que deberá guardarse en una variable y luego permitir al usuario que cambie su valor al introducir su edad actual.

Una variable también podría obtener su valor de alguna operación matemática o lógica, o bien por el valor de retorno de una [función](/conceptos/2015/06/23/funciones.html).

A la operación de almacenaje de un dato dentro de una variable se la llama "**asignación**", y en la mayoría de los lenguajes se suele utilizar el signo igual ("=") como operador. Por ejemplo, si a la variable "puntaje" le queremos asignar el valor inicial 0, podríamos escribir <code>puntaje = 0</code>.

Al hecho de crear variables dentro del código de un programa se lo denomina "declaración de variables". En algunos lenguajes se pueden declarar variables al momento de usarlas. Un ejemplo de esto es Python que, con el solo hecho de asignar un valor a una variable que no había sido usada hasta ese punto del código, crea esa nueva variable (es decir, le reserva una ubicación de memoria), deduciendo el tipo de dato de acuerdo al dato que se almacenó. Así, si escribimos <code>nombre = "Juana"</code> en Python, se creará una variable con identificador "nombre" con el dato "Juana", de tipo String. En otros lenguajes, como Java, C++ o Pascal, las variables deben ser declaradas y su tipo debe ser indicado por el programador: <code>String nombre = "Juana"</code>.
