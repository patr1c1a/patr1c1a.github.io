---
layout: post
title: Paso a paso - programa de escritorio en Visual Basic, parte 1
date: 2012-02-06 19:00:00
categories: tutoriales
tags: objetos .net visual_basic visual_studio eventos proyectos
published: true
---

## Visual Studio: descargar versión gratuita y otras alternativas

En la década del '90 Visual Basic 6.0 y su entorno de programación eran la herramienta visual preferida de los programadores principiantes. Hoy día el IDE (entorno integrado de desarrollo) ha evolucionado en Visual Studio, un excelente IDE que no sólo permite programar en una versión muy actualizada del lenguaje Visual Basic, sino también en C# (muy similar a Java), Visual C++ y otros lenguajes, incluidas aplicaciones web con ASP.NET y aplicaciones móviles. Aunque este entorno y los programas hechos con el framework .NET sólo corran en Windows (existen algunos intentos multiplataforma pero nada completo), el [índice tiobe](http://www.tiobe.com/tiobe_index?page=index) que muestra los lenguajes de programación más populares suele tener siempre a Visual Basic y C# entre los primeros puestos.

Este IDE permite armar la interfaz visual de nuestros programas de una forma intuitiva y sencilla. Posee barras de herramientas que facilitan esta tarea con sólo arrastrar y soltar controles en la posición en que se desee ubicarlos. Además, tiene un muy buen soporte de accesibilidad.

Afortunadamente, existe una versión gratuita de Visual Studio, la cual puede descargarse [desde acá en español](https://www.visualstudio.com/es-us/products/visual-studio-community-vs.aspx) o [desde acá en inglés](https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx) y posee la mayor parte de la funcionalidad básica necesaria para el desarrollo de software sencillo de escritorio o web. También los alumnos universitarios pueden crear una cuenta en [dreamspark.com](http://dreamspark.com) (y verificar su calidad de estudiantes) para descargar software de Microsoft gratuitamente.

Además, existen algunas alternativas gratuitas, como [MonoDevelop](http://www.monodevelop.com), [SharpDevelop](http://www.icsharpcode.net/OpenSource/SD/), y [WebMatrix](https://www.microsoft.com/web/webmatrix) (sólo para aplicaciones web)</a>.

Para los ejemplos de este artículo se utilizará el IDE Microsoft Visual Studio 2010 y el lenguaje Visual Basic.



## El framework .NET

Como cualquier framework, .NET contiene código con funcionalidad que permite enfocarse en los detalles del desarrollo, reutilizando lo que ya está hecho.

Para no irnos en tecnicismos, diremos que este framework contiene bibliotecas de código que permiten aplicar la funcionalidad a diferentes lenguajes y, además, los programas escritos con él corren sobre un máquina virtual en Windows llamada "Common Language Runtime" (o CLR) que provee ciertos servicios.

A veces, al instalar software en una máquina, éste advierte que es necesaria determinada versión de .NET, y esto es porque el software que se está instalando incluye código de este framework y es necesario que ese código se encuentre en la máquina.

Este framework corre por debajo de los programas codificados en diversos lenguajes. Es por esto que no existen demasiadas diferencias entre la potencia de Visual Basic y la de C# (a pesar de tener una sintaxis completamente diferente).


## Breve glosario

Visual Studio tiene sus propias denominaciones para algunos componentes y hay otros que son usuales en diferentes entornos de desarrollo. También se incluyen algunos breves conceptos de programación orientada a objetos, ya que es el paradigma utilizado en el programa explicado este artículo.
  
* _Proyecto_: nombre global que se le da a la aplicación en progreso, con todos sus componentes.
  
* _Solución_: cada uno de los "programas" (estrictamente hablando) que componen el proyecto.
  
* _Formulario_: es lo que en Windows llamaríamos "ventana".
 
* _Control_: cualquier objeto que puede ser agregado a un formulario y permite darle funcionalidad.
  
* _Objeto_: este es un concepto de programación orientada a objetos (POO). En resumidas cuentas, un objeto es una copia obtenida de un "molde" o "plantilla" con determinadas características. Algunos objetos vienen ya predefinidos en el framwork pero también pueden ser definidos por el programador. Por ejemplo, si creamos un formulario con determinadas características (texto, tamaño, colores, botones, etc.), hemos creado un "molde", y cada vez que ese formulario es llamado y mostrado en pantalla, lo que se muestra es un objeto obtenido a partir de ese molde.
  
* _Método_: otro concepto propio de la POO. Los métodos permiten enviar "mensajes" u "órdenes" a los objetos. Generalmente, la llamada a un método va antecedida del objeto al que pertenece, separado por un punto.
  
* _Propiedades_: características de cada objeto. Las propiedades tienen valores asignados. Cada objeto que proviene de un mismo "molde" tendrá las mismas propiedades, pero ellas pueden tener diferentes valores asignados. Por ejemplo, una propiedad podría ser el ancho de un formulario, y así, todos los formularios que son creados a partir del mismo molde tendrán una propiedad "ancho", pero uno podría tener un valor de 480 y otro de 700.
  
* _Evento_: una acción que se produce durante la ejecución del programa. Por ejemplo, el hecho de que el usuario presione un botón con el mouse. Los eventos son importantes porque pueden definirse comportamientos en respuesta a ellos (ej.: el usuario hace click sobre un botón y esto hace que se abra un nuevo formulario).
  
* _Label (control)_: una etiqueta de texto de una sola línea que no permite ingreso de caracteres por medio del teclado.
  
* _TextBox (control)_: una pequeña cajita de texto que permite mostrar o introducir caracteres por medio del teclado.
  
* _ComboBox (control)_: caja desplegable que muestra un elemento por vez.
  
* _Botón (control)_: elemento que permite la interacción con un componente del programa. Por ejemplo, un botón podría realizar la acción de ingresar datos al sistema.
  
* _MessageBox (control)_: es un "cartel" como los típicos que Windows utiliza para notificar al usuario de algo, informar de un error o pedirle una decisión sobre si desea o no realizar una acción determinada.
  
* _Origen de datos (control)_: como la expresión lo dice, es algo de donde provienen datos. Usualmente, se refiere a una base de datos, desde la cual se obtendrá información que se manipulará en el programa.


## Desarrollo de un programa con altas, bajas y modificaciones ("ABM"en español o "CRUD" en inglés)

El resultado de todo lo que se describirá en este artículo será un programa de ejemplo, cuyo objetivo es gestionar gastos, pero en realidad se agregan detalles. Como se dijo anteriormente, los ejemplos presentados se realizaron utilizando Microsoft Visual Studio 2010, y para la base de datos se utilizó Microsoft Access, ya que tiene un soporte nativo con el IDE. Pero se debe tener en cuenta que Access no es apropiado para cualquier solución, ya que tiene algunas limitaciones (por ejemplo, la base de datos puede alcanzar 2GB de tamaño como máximo).

> Este artículo (y la [parte 2](/tutoriales/2012/02/06/tutorial-vb-parte2.html)) dan por supuesto que el lector domina conceptos y herramientas básicas [de programación](/conceptos/2015/06/17/empezando-a-programar.html) como las [variables](/conceptos/2015/06/18/que-son-las-variables.html), [tipos de datos](/conceptos/2015/06/18/tipos-de-datos.html), [estructuras de control](/conceptos/2015/06/23/estructuras-de-control.html), [funciones](/conceptos/2015/06/23/funciones.html), [abstracción](/conceptos/2015/06/20/abstraccion-y-modularizacion.html) y [programación orientada a objetos](/poo/2016/01/07/programacion-orientada-a-objetos.html).

Teniendo claros estos temas, podemos adentrarnos en este "**mini-tutorial**" que no es sino una descripción práctica, paso a paso, de cómo se construye un programa básico con "ABM" utilizando las herramientas que provee Visual Studio y el framework .NET.



## Manos a la obra

Una vez abierto Visual Studio, crearemos un nuevo proyecto haciendo click en el menú **Archivo > Nuevo > Proyecto** (o por medio del atajo de teclado Ctrl+Shift+N).

![crear proyecto]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img1.png)

Aparecerá el menú completo de plantillas que soporta Visual Studio. De este menú vamos a elegir Visual Basic y, de entre sus opciones, "Aplicación de Windows Forms". Le daremos un nombre al proyecto y seleccionaremos en qué carpeta guardarlo.

![crear proyecto]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img2.png)

Lo primero que veremos será el formulario inicial, en blanco, al que el sistema le habrá dado el nombre predefinido "Form1". A la izquierda, la caja de herramientas con los controles que podemos agregar al formulario. A la derecha, en la parte superior se sitúa el "explorador de soluciones", que muestra los componentes de la aplicación; en la parte inferior, la ventana de propiedades con los valores asignados a las propiedades del objeto seleccionado. Si alguna de estas cajas no estuviera visible, pueden ser abiertas desde el menú "Ver".

![proyecto en blanco]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img3.png)

Seleccionando el formulario (es decir, haciéndole un click) se pueden ver sus propiedades y establecerles valores. Ahora será necesario ponerle un título, que será el texto que se mostrará en la barra de título de la ventana. Para esto, seleccionamos la propiedad "Text" y le damos el título que queremos que muestre:

![propiedad text]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img4.png)

Algo importante es no confundir el texto que muestra un objeto con su nombre: todos los objetos tienen un nombre, que es el nombre de la instancia (es decir, de la "copia" que se sacó del "molde"). Esto puede verse en la propiedad "(Name)". El nombre del objeto es un identificador como cualquier variable, así que es recomendable no incluir caracteres extraños en él. Se utiliza para hacer referencia al objeto cuando se necesita acceder a uno de sus métodos, eventos o propiedades. Aquí ya comenzamos a incorporar conceptos de programación orientada a objetos. Para quien no esté familiarizado con ellos [puede leer este artículo](/poo/2016/01/07/programacion-orientada-a-objetos.html).

![propiedad name]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img5.png)

Para comenzar a agregar contenidos a nuestro formulario, vamos a colocar algo de texto y un botón que abre un nuevo formulario. En primer lugar, utilizaremos un Label para poner un título a este formulario y otro Label debajo, que contendrá un texto explicativo.

Seleccionando el Label que contiene el título, nos situamos sobre la propiedad "Text" para escribir el texto. Luego sobre "Font", y hacemos click sobre el botón con tres puntos para elegir el tipo y tamaño de fuente. Con la propiedad "ForeColor" definiremos el color de la fuente.

![insertando un label]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img6.png)

Una herramienta útil es la de "Formato", que se encuentra en el menú superior. Con ella podemos alinear un objeto dentro de otro o dentro del formulario, alinear los lados de varios objetos, igualar la separación horizontal o vertical entre varios objetos, etc.

A continuación, agregamos un Button (botón), al que luego daremos funcionalidad. Los botones también tienen una propiedad "Text" para establecer el texto que mostrarán. Incluso puede cambiarse su color y agregarles una imagen a modo de ícono, utilizando las propiedades "BackColor" e "Image" respectivamente. Agregamos un nuevo Button que permitirá cerrar el programa y le insertamos una imagen. Utilizando las propiedades "ImageAlign" y "TextAlign" indicamos dónde quiero que se ubique el texto y dónde la imagen. La propiedad "Image" trae a la vista un cuadro en el que podremos escoger la imagen haciendo click en el botón "Importar":

![botón salir]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img7.png)

![importar recurso]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img8.png)

Para terminar de "decorar" este formulario, vamos a agregar una imagen usando un PictureBox. Clickeando sobre el link "Elegir imagen" se abrirá nuevamente el cuadro para agregar imágenes a la aplicación.

![agregar picture box]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img9.png)

Una vez agregada la imagen, es posible optar por distintos modos de visualización: _Normal_ (deja la imagen en su tamaño original), _StretchImage_ (ajusta la imagen a las medidas del PictureBox, modificando la relación ancho/alto), _Autosize_ (adapta el PictureBox a las medidas de la imagen), _CenterImage_ (deja la imagen en su tamaño original y la centra en el PictureBox), _Zoom_ (ajusta la imagen a las medidas del PictureBox, sin modificar la relación ancho/alto).

Ahora daremos funcionalidad a los botones. Para hacerlo, es necesario ingresar código en los eventos que éstos pueden desencadenar. Los eventos pueden verse en la ventana de Propiedades al hacer click sobre el botón que se encuentra arriba del listado de propiedades (el que tiene forma de rayo).

El evento más comúnmente usado en los botones es la acción de hacer Click sobre ellos. La forma más fácil de acceder al código de este evento es dando doble click sobre el botón. Pero también puede accederse haciendo doble click sobre el evento "Click" en la lista de eventos:

![eventos de un botón]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img10.png)

Esto nos llevará a una nueva visualización: el código del formulario. Y automáticamente creará una función vacía para responder al evento que seleccionamos.

También en esta vista pueden elegirse otros eventos a ser disparados por el botón. La caja superior que muestra el evento "Click" es un menú desplegable que permite ver todos los eventos asociables a ese mismo objeto.

![código del evento]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img11.png)

La función creada es de tipo "Private", lo cual indica que sólo puede accederse desde dentro del formulario. "Sub" es la palabra que identifica a los subprocesos y btnSalir_Click es el nombre de la función. Luego, entre paréntesis, se encuentra la lista de parámetros: "ByVal" indica que son parámetros por valor (por oposición a parámetros por referencia, o "ByRef"), luego el nombre del parámetro y por último el tipo, antepuesto por la palabra "As" que se utiliza para definir el tipo de los datos. A continuación de la lista de parámetros se encuentra la palabra "Handles" (indicadora de evento) seguida del nombre del evento al que va a responder esta función (en este caso, el evento "Click" del objeto btnSalir).

Como cuerpo de la función vamos a colocar un método que cierra la aplicación: Application.Exit()

Así, la función completa queda de esta forma:
  
<pre><code>Private Sub btnSalir_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnSalir.Click
    Application.Exit()
End Sub</code></pre> 
  
Aquí notarán una interesante característica de este IDE: el IntelliSense. Esta herramienta completa automáticamente los nombres de objetos, métodos, propiedades, etc. a medida que escribimos. Por ejemplo, si escribimos"Appl" tendremos una lista desplegable con sugerencias que comiencen con esas letras. También autocorrige las mayúsculas y minúsculas y agrega algunas cositas, como el "End Sub" que finaliza las funciones. Es muy útil al buscar propiedades, eventos y métodos, ya que al escribir el nombre de un objeto seguido de un punto se mostrará una lista desplegable con todas las opciones posibles.

En la parte superior de la caja que muestra el código pueden verse los distintos formularios y vistas abiertos. Clickeando sobre "Form1.vb[Diseño]" volveremos a la vista de diseño.

Para terminar con este formulario, agregaremos funcionalidad al otro botón. Pero debido a que la función de éste es mostrar un formulario diferente, primero deberemos agregar ese formulario al proyecto. Para esto voy a clickear en el menú Proyecto -> Agregar Windows Forms... y voy a darle un nombre a este formulario (por defecto el sistema lo llama Form2, pero en una aplicación con muchos formularios esto puede tornarse muy confuso). Este nombre no es el del objeto, sino el del archivo del diseñador, y el que se mostrará en el explorador de soluciones. Al igual que con el otro formulario, podremos cambiar las propiedades a gusto, y asignarle un nombre al objeto. En este caso, lo llamaré frmDatos.

Ahora, volviendo a la vista de diseño del primer formulario, doy doble click sobre el botón que llamé "btnDatos" para que aparezca el evento Click de este botón, y dentro de él escribo el método que muestra el nuevo formulario, frmDatos:

<pre><code>Private Sub btnDatos_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnDatos.Click
    frmDatos.Show()
End Sub</code></pre>

A esta altura podemos ejecutar nuestro programa para corroborar que todo esté funcionando correctamente. Para esto haremos click sobre el botón verde en forma de flecha que se encuentra en la barra de herramientas. Esta funcionalidad también puede encontrarse en el menú Depurar -> Iniciar depuración, o bien presionando F5. De esta forma se puede ver cómo el programa se mostraría si se ejecutara desde el archivo ejecutable que en su momento voy a generar.

![ejecución]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img12.png)

Hasta el momento, el botón "Salir" debería cerrar el programa y el botón "Datos" debería traer a la vista el nuevo formulario, vacío.

Pero este nuevo formulario no sirve de mucho si no tiene contenido. Así que vamos a agregar algunas cosas: algunos Label, para indicar los datos que el usuario debería ingresar, un TextBox para que ingrese su nombre, uno para la edad, dos ComboBoxRadioButton para que elija su género y dos CheckBox para que elija su ocupación. La diferencia entre RadioButton y CheckBox es que el primero sólo permite seleccionar una de entre todas las opciones y el segundo permite marcar más de una. También agregaremos dos botones: uno para cerrar el formulario y otro para procesar la información.

Algo más que agregamos y que no puede verse es un Label que colocamos al lado del que dice "Capacidad", al cual le borramos el valor de su propiedad Text (por lo cual quedó vacío, por el momento).

Así se vería el formulario, luego de agregar todo esto:

![vista del formulario]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img13.png)

Es importante dar nombres a los objetos para luego poder definir su funcionalidad. En este caso, llamamos txtNombre al TextBox, cboEdad al ComboBox, radioM y radioF a los RadioButton, chkEstudio y chkTrabajo a los CheckBox, lblResultado al Label que no muestra nada, btnAceptar al botón inferior y btnCerrar al otro.

Empezando por lo más fácil, vamos a definir el Click del btnCerrar. En este caso el método a llamar (Close) se ejecutará sobre el propio formulario. Para esto se utiliza la pseudovariable "Me": <code>Me.Close()</code>

<pre><code>Private Sub btnCerrar_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnCerrar.Click
    Me.Close()
End Sub</code></pre>

El ComboBox para seleccionar la edad debería cargarse con números al abrirse el formulario (digamos... ¿números del 1 al 120?), de manera que el usuario pueda elegir su edad de la lista. Esto puede lograrse fácilmente con alguna estructura iterativa que vaya agregando cada número al ComboBox. Para esto usaremos un FOR-NEXT (_next_ es la palabra reservada que cierra un bucle _for_). Y para que esta acción se realice tan pronto como se abra el formulario, la vamos a colocar en el evento "Load" de nuestro formulario Datos. Para acceder a él rápidamente, se puede hacer doble click sobre la barra de título del formulario, aunque también puede accederse mediante la lista de eventos, como se mencionara anteriormente.

Dentro de este evento, el _for_ es muy similar a cualquier otro lenguaje: definimos una variable de tipo entero, "i"; para definir variables locales al procedimiento se utiliza el modificador "Dim" (otros modificadores: Private, Friend, Public): <code>Dim i As Integer</code>.

<pre><code>Private Sub frmDatos_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load 
    Dim i As Integer 
    For i = 1 To 120 
    cboEdad.Items.Add(i) 
    Next 
End Sub</code></pre>

En el _for_ indicamos que la variable **i** va a iterar entre los valores 1 y 120, y que por cada iteración va a agregar ese valor al ComboBox. Para esto accedemos a la propiedad Items del cboEdad y luego al método Add de esa propiedad, pasándole como parámetro la **i**.

A continuación, agregaremos funcionalidad al evento Click del botón "Aceptar": le vamos a decir que muestre un MessageBox que, basándose en la edad de la persona (mayor o menor de 21 años) le indique si puede continuar o no. Además, en el Label "invisible" que se encuentra al lado del que dice "Capacidad" (lblResultado) aparecerá la palabra "capaz" si tiene 21 años o más, o "incapaz" si tiene menos. El código es el siguiente:

<pre><code>Private Sub btnAceptar_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnAceptar.Click 
    Dim edad As Integer
    edad = CInt(cboEdad.SelectedItem)
    If edad > 21 Then
        lblResultado.Text = "capaz"
        MessageBox.Show("Mayor de edad. Puede continuar completando los datos para obtener su crédito por US$ 1 millón", "Verificación", MessageBoxButtons.OK, MessageBoxIcon.Information)
    Else
        lblResultado.Text = "incapaz" 
        MessageBox.Show("Menor de edad. Lamentablemente no puede obtener un crédito por US$ 1 millón", "No pasa la verificación", MessageBoxButtons.OK, MessageBoxIcon.Hand)
    End If
End Sub</code></pre>

Analicémoslo:

<code>Dim edad As Integer</code> declara una variable de tipo entero. La utilizaremos para almacenar la edad que seleccionó el usuario, ya que el ComboBox devuelve datos de tipo Object (una clase global que engloba a todas las clases de objetos), y se hará necesario convertir ese Object a un dato de tipo Integer. Esto se logra con la siguiente línea: <code>edad = CInt(cboEdad.SelectedItem)</code>. Los métodos para convertir ("cast") datos de un tipo a otro, son los siguientes: CBool, CByte, CChar, CDate, CDec, CDbl, CInt, CLng, CObj, CShort, CSng, CStr.

Luego comparamos la edad ingresada por el usuario contra el número 21 con un <code>If edad > 21 Then</code>. Si la evaluación de esa condición da como resultado True, se ejecuta el bloque de código que sigue, a saber:

<pre><code>lblResultado.Text = "capaz" 
MessageBox.Show("Mayor de edad. Puede continuar completando los datos para obtener su crédito por US$ 1 millón", "Verificación", MessageBoxButtons.OK, MessageBoxIcon.Information)</code></pre>

Es decir, al _Label_ vacío (lblResultado) se le asigna el texto "capaz" en su propiedad _Text_. A continuación, se muestra un _MessageBox_, que recibe los siguientes parámetros, en este orden: _String_ con el texto que muestra el cuadro, _String_ con el título del cuadro, botones que aparecen en el cuadro (llamando a _MessageBoxButtons_ para elegir el/los botones), ícono que muestra el cuadro (llamando a _MessageBoxIcon_ para elegir el ícono).

Por el _else_ se accede al bloque de código a ejecutar en caso de que la condición devuelva False. Es bastante similar al anterior, sólo que este muestra el texto "**incapaz**" en la propiedad _Text_ del _lblResultado_ y el mensaje e ícono del _MessageBox_ son diferentes.

De la misma forma, podría crearse un tercer formulario y hacer que se muestre en caso de que la condición evaluada por el If sea True (es decir, que se le dio acceso al usuario). Suponiendo un formulario llamado frmAcceso, el código a mostrar dentro del _if_ sería <code>frmAcceso.Show()</code>.

La ejecución del programa mostrará algo parecido a esto:

![programa en ejecución]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img14.png)
  
Ahora, para generar el ejecutable que haga funcionar todo esto en un solo archivo, debemos elegir del menú superior la opción **Generar > Generar proyecto**. Luego, dentro de la carpeta del proyecto buscar la subcarpeta "bin" y dentro de ella la carpeta "Release". Habrá más de un archivo pero sólo uno de ellos será el .exe que contiene la aplicación. Ese será el que podemos trasladar a otra computadora (que cuente con las librerías necesarias) para que todo el mundo disfrute de la brillante pieza de software que acabamos de crear.

![listado de archivos en la carpeta Release]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte1-img15.png)

## Fin de la parte 1

Hay muchísimas cosas más que pueden hacerse. Esto es sólo una introducción para empezar a familiarizarse con esta potente herramienta de trabajo.

Una excelente fuente de consulta es el [foro oficial de MSDN](https://social.msdn.microsoft.com/Forums/es-ES/home), donde puede buscarse información sobre cómo hacer diferentes cosas con Visual Studio, o preguntar sobre el tema si es que nadie lo preguntó antes.

Por otra parte, siempre es muy útil consultar la documentación oficial de los lenguajes y frameworks que utilizamos. En este caso, dependerá de la versión del framework .NET que se utilice, pero [la documentación de VS2010 puede hallarse acá](https://msdn.microsoft.com/es-es/library/k1s94fta%28v=vs.100%29.aspx).

En la [parte 2](/tutoriales/2012/02/06/tutorial-vb-parte2.html) haremos un programa de gestión de gastos, con conexión a base de datos.
