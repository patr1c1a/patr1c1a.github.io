---
layout: post
title: Calculadora con Python usando Tkinter
date: 2019-08-02 21:00:00
categories: python tutoriales poo
tags: gui proyecto
published: true
---

Una calculadora simple es uno de los proyectos más comunes para comenzar a programar, tanto en consola como con interfaz gráfica.

En este proyecto usaremos Python 3 y el módulo para interfaces gráficas Tkinter.

También es posible acceder al video explicando el proyecto paso a paso:
{% include youtubePlayer.html id="V-_d5N4UJjw" %}

Esta calculadora tiene sólo la funcionalidad básica, quedando al lector la tarea de mejorarla y agregar funcionalidad. Algunas mejoras posibles:
* Borrar el contenido de la pantalla antes de continuar, después de haber mostrado un resultado.
* Incorporar un botón de borrado parcial (el actual sólo borra todo el contenido de la pantalla).
* No mostrar decimales al hacer una división que da como resultado un entero.

Pasemos a la implementación, para lo cual será necesario tener instalado Python 3 ([click aquí para ver un video sobre cómo descargar e instalar](https://www.youtube.com/watch?v=F9eM_VoKGJQ)). Tkinter es una de las opciones para crear interfaces gráficas con Python. La ventaja es que se instala automáticamente con la instalación de Python 3, al menos en Windows. En algunos sistemas operativos esto no es así. En Linux, es necesario instalarlo manualmente:
<pre><code>sudo apt-get install python3-tk</code></pre>

Ahora sí, comenzamos creando un archivo .py (vamos a usar uno solo) para escribir el código. Del módulo tkinter vamos a ir importando lo que necesitemos, para no importar el módulo completo con componentes que no se van a usar en el proyecto.

<pre><code>from tkinter import Tk

class Interfaz:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Calculadora")
	  return

ventana_principal=Tk()
calculadora=Interfaz(ventana_principal)
ventana_principal.mainloop()</code></pre>

Comencemos por la parte final de este fragmento de código:
<pre><code>ventana_principal=Tk()</code></pre>
La clase Tk es la encargada de crear la ventana principal o raíz (en inglés, “root”). Sólo puede haber una ventana que sea la principal, pero luego pueden crearse otras ventanas. En este ejemplo, sólo habrá una ventana, que será la que muestre la calculadora. Esta ventana ya tiene todas las características básicas necesarias: una barra de título, botones para minimizar, maximizar, cerrar, etc.
<pre><code>calculadora=Interfaz(ventana_principal)
ventana_principal.mainloop()</code></pre>
Luego de crear la interfaz gráfica, la ventana principal ingresa en un bucle infinito a la espera de eventos. Los eventos podrían ser cualquier cosa que suceda: que el usuario presione un botón, que ingrese un texto, etc. Este bucle finaliza cuando el usuario termina el programa, ya sea haciendo click en la cruz de la ventana o mediante una interrupción de teclado en la consola.

Finalmente, la clase Interfaz, que va a representar la interfaz gráfica de esta calculadora:
<pre><code>class Interfaz:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Calculadora")
        return</code></pre>
Aunque _return_ no es necesario, lo colocamos solamente por mejorar la legibilidad, ya que al continuar agregando código nos va a permitir identificar más fácilmente dónde termina una función.
El método \_\_init\_\_ es el constructor de esta clase y recibe como parámetro a la ventana principal. A esta ventana le asignaremos un título (“Calculadora”).

Si ejecutamos el programa, hasta el momento se ve así:

![ventana vacía]({{ site.url }}/assets/2019-08-02-calculadora-python-tkinter-img1.png)

Ahora es necesario incorporar un nuevo componente: una caja de texto, que será la “pantalla” de la calculadora, donde vamos a ver el resultado de las operaciones. Para esto utilizaremos un componente Text, que debe ser agregado en la importación del módulo tkinter:
<pre><code>from tkinter import Tk, Text</code></pre>
Y dentro del método \_\_init\_\_ de la clase Interfaz, agregaremos lo siguiente:
<pre><code>self.pantalla=Text(ventana,state="disabled",width=40,height=3,background="orchid",foreground="white",font=("Helvetica",15))</code></pre>
Esta instrucción instancia un objeto Text, pasándole la ventana como primer parámetro. Luego el estado (state) lo indicamos como deshabilitado para que el usuario no pueda hacer click y escribir manualmente (sólo podrá escribir a través del teclado de la calculadora). También se indican el ancho (width) y alto (height) de la pantalla, el color de fondo (background) y el color del texto (foreground) y, finalmente, la fuente (font), para lo cual se pasa como parámetro una tupla con el tipo y tamaño.
Tkinter tiene muchos colores disponibles. [Para verlos, click acá]({% post_url 2019-08-01-python-tkinter-colores %})

<pre><code>self.pantalla.grid(row=0,column=0,columnspan=4,padx=5,pady=5)</code></pre>
Lo que sigue es el posicionamiento de la pantalla. Ahora que comenzamos a colocar elementos en la ventana, necesitamos algo que se suele llamar “gestor de geometría” y que sirve para determinar cómo va a ser la disposición o el diseño de los elementos dentro de la ventana. En Tkinter hay diferentes tipos de gestores: grid, pack y place. Por ejemplo, place permite indicar la posición exacta de cada componente dentro de la ventana, ya sea en forma absoluta o en forma relativa a otros componentes. Pack es ideal para colocar elementos alineados en forma vertical u horizontal. Grid permite dividir a la ventana en una grilla con filas y columnas, e indicar la posición de un componente en determinada fila y columna. En este caso vamos a usar grid, porque el diseño de la calculadora se parece mucho a una grilla. Es por eso que al objeto Text que hemos llamado pantalla le indicamos que utilice el gestor “grid” y que se coloque en la fila 0, columna 0 (es decir, la primera “celda” de la grilla). También se indica que debe abarcar 4 columnas (columnspan) y que debe tener un margen interno de 5 a izquierda y derecha (padx), y 5 arriba y abajo (pady).

<pre><code>self.operacion=""</code></pre>
Esta variable contendrá la operación que la calculadora debe resolver. Al iniciar el programa, se inicializa como string vacío.

Hasta el momento tenemos algo como esto:
<pre><code>from tkinter import Tk, Text

class Interfaz:
    def __init__(self, ventana):
        #Inicializar la ventana con un título
        self.ventana=ventana
        self.ventana.title("Calculadora")

        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla=Text(ventana, state="disabled", width=40, height=3, background="orchid", foreground="white", font=("Helvetica",15))

        #Ubicar la pantalla en la ventana
        self.pantalla.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

        #Inicializar la operación mostrada en pantalla como string vacío
        self.operacion=""

        return


ventana_principal = Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()</code></pre>

![pantalla de la calculadora]({{ site.url }}/assets/2019-08-02-calculadora-python-tkinter-img2.png)

A continuación necesitaremos importar un nuevo componente del módulo tkinter: Button.
<pre><code>from tkinter import Tk, Text, Button</code></pre>

También crearemos, dentro de la clase Interfaz, un método para crear los botones que tendrá la calculadora:
<pre><code>def crearBoton(self,valor,escribir=True,ancho=9,alto=1):
    return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda: self.click(valor,escribir))</code></pre>

En este método se retorna un botón, llamando al constructor de la clase Button, al cual se le pasa la ventana donde estará ubicado (self.ventana), el valor que mostrará el botón (text), el ancho (width) y alto (height) y finalmente un comando (command), que es la acción que se debe ejecutar cuando se hace click sobre este botón, que será una llamada al método click, que crearemos más adelante. Es necesario usar una función lambda para poder pasar parámetros al método click (si no usamos lambda, el “command” sólo sería el valor de retorno de la función click, que en este caso es None, así que estaríamos diciéndole que no haga nada). Lambda nos permite crear funciones anónimas, pero es mejor no adentrarnos en ese tema en este momento.
Ahora en el \_\_init\_\_ creamos los 17 botones necesarios, mediante llamadas a este método:
<pre><code>
boton1=self.crearBoton(7)
boton2=self.crearBoton(8)
boton3=self.crearBoton(9)
boton4=self.crearBoton(u"\u232B",escribir=False)
boton5=self.crearBoton(4)
boton6=self.crearBoton(5)
boton7=self.crearBoton(6)
boton8=self.crearBoton(u"\u00F7")
boton9=self.crearBoton(1)
boton10=self.crearBoton(2)
boton11=self.crearBoton(3)
boton12=self.crearBoton("*")
boton13=self.crearBoton(".")
boton14=self.crearBoton(0)
boton15=self.crearBoton("+")
boton16=self.crearBoton("-")
boton17=self.crearBoton("=",escribir=False,ancho=20,alto=2)</code></pre>
Para el símbolo de división y el de borrado usamos los códigos unicode, para asegurarnos de que se muestren bien en pantalla. Vemos que se pasan sólo los argumentos necesarios, porque el método tiene varios parámetros opcionales con valores por defecto, pero el valor a mostrar es el único parámetro obligatorio. El parámetro “escribir” contiene un valor booleano que está en True por defecto y que permite saber si el botón debe escribir (mostrar) algo en pantalla o no. En el caso de los botones “=” y de borrado, este valor se pone en False porque son botones que realizan acciones específicas, que no deben mostrar sus caracteres en pantalla.

Finalmente, ubicamos los botones en la grilla que nos da el gestor grid:
<pre><code>botones=[boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,boton10,boton11,boton12,boton13,boton14,boton15,boton16,boton17]
contador=0
for fila in range(1,5):
for columna in range(4):
      	botones[contador].grid(row=fila,column=columna)
            contador+=1
botones[16].grid(row=5,column=0,columnspan=4)</code></pre>
Ponemos a los botones en una lista para poder iterar por ellos y luego empezamos a posicionarlos entre las filas 1 y 4 y entre las columnas 0 y 3. El botón “=” se reubica al finalizar, porque tiene una posición especial, debajo de todos los demás y con un tamaño mayor.

El código completo, hasta este punto, es el siguiente:
<pre><code>from tkinter import Tk, Text, Button

class Interfaz:
    def __init__(self, ventana):
        #inicializar la ventana con un título
        self.ventana=ventana
        self.ventana.title("Calculadora")

        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla=Text(ventana, state="disabled", width=40, height=3, background="orchid", foreground="white", font=("Helvetica",15))

        #Ubicar la pantalla en la ventana
        self.pantalla.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

        #Inicializar la operación mostrada en pantalla como string vacío
        self.operacion=""

        #Crear los botones de la calculadora
        boton1=self.crearBoton(7)
        boton2=self.crearBoton(8)
        boton3=self.crearBoton(9)
        boton4=self.crearBoton(u"\u232B",escribir=False)
        boton5=self.crearBoton(4)
        boton6=self.crearBoton(5)
        boton7=self.crearBoton(6)
        boton8=self.crearBoton(u"\u00F7")
        boton9=self.crearBoton(1)
        boton10=self.crearBoton(2)
        boton11=self.crearBoton(3)
        boton12=self.crearBoton("*")
        boton13=self.crearBoton(".")
        boton14=self.crearBoton(0)
        boton15=self.crearBoton("+")
        boton16=self.crearBoton("-")
        boton17=self.crearBoton("=",escribir=False,ancho=20,alto=2)

        #Ubicar los botones con el gestor grid
        botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17]
        contador=0
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila,column=columna)
                contador+=1
        #Ubicar el último botón al final
        botones[16].grid(row=5,column=0,columnspan=4)
        return


    #Método para crear un botón con el valor que debe mostrar
    def crearBoton(self,valor,escribir=True,ancho=9,alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda:self.click(valor,escribir))


ventana_principal = Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()</code></pre>

Al ejecutar, ya veremos la calculadora completa, pero aún le falta cierta funcionalidad:
![interfaz de la calculadora]({{ site.url }}/assets/2019-08-02-calculadora-python-tkinter-img3.png)


Antes de continuar, necesitamos importar algunas cosas más: END y re. El primero es un índice que señala el final del texto de un componente Text y el segundo permite evaluar expresiones regulares:
<pre><code>from tkinter import Tk, Text, Button, END, re</code></pre>

Ahora agregaremos el método que controla el evento disparado por los botones al hacer click sobre ellos:
<pre><code>def click(self,texto,escribir):
    if not escribir:
        if texto=="=" and self.operacion!="":
            self.operacion=re.sub(u"\u00F7", "/", self.operacion)
            resultado=str(eval(self.operacion))
	    self.operacion=""
            self.limpiarPantalla()
            self.mostrarEnPantalla(resultado)
        elif texto==u"\u232B":
            self.operacion=""
            self.limpiarPantalla()
    else:
        self.operacion+=str(texto)
        self.mostrarEnPantalla(texto)
    return</code></pre>
Como vimos anteriormente, el parámetro “escribir” en True indica que el valor del botón presionado debe mostrarse en pantalla. Para el caso de los botones “=” y de borrado, este parámetro viene con el valor False, ya que el botón “=” sirve para mostrar el resultado de la operación y el de borrado elimina todo el contenido de la pantalla. Entonces, si el contenido de escribir es True (bloque else) tendremos que agregar lo que el usuario ingresó a la operación que se está formando y luego mostrar en pantalla el texto del botón, lo cual delegaremos en un nuevo método que veremos en unos instantes, llamado mostrarEnPantalla. En cambio, si escribir es False, debemos ver si se presionó el botón “=” o el de borrado. En el caso del botón de borrado (el bloque elif), reiniciaremos la operación y limpiaremos la pantalla mediante otro método que en breve estaremos analizando. Si el botón presionado fue el de “=” debemos ver también si había una operación a resolver, por eso es que evaluamos si self.operacion es distinto del string vacío. Cuando hay una operación a resolver, esto es lo que sucede:

<pre><code>self.operacion=re.sub(u"\u00F7", "/", self.operacion)
resultado=str(eval(self.operacion))
self.operacion=""
self.limpiarPantalla()
self.mostrarEnPantalla(resultado)</code></pre>
En la primera línea debemos reemplazar el símbolo de división que mostramos en la calculadora por el operador de división que usa Python (“/”). Para esto utilizamos expresiones regulares, las cuales se incluyen en el módulo re (“regular expression”) de Python. Mediante el método sub (sustituir) cambiamos el carácter que representa a la división por el carácter / en la operación. De esta forma, si la operación a resolver es una división, podremos resolverla con Python.
A continuación usamos eval() que resuelve una operación matemática dada como string. Por ejemplo, eval(“1+2”) da como resultado 3. Como necesitamos que el resultado sea un string para mostrarlo en nuestra pantalla de la calculadora, lo convertimos mediante str().
Finalmente, reiniciamos la operación, para que quede otra vez vacía, a la espera de que el usuario ingrese una operación nueva, y luego limpiamos la pantalla para mostrar en su lugar el resultado.

El siguiente método es el que borra la “pantalla” de la calculadora:
<pre><code>def limpiarPantalla(self):
    self.pantalla.configure(state="normal")
    self.pantalla.delete("1.0", END)
    self.pantalla.configure(state="disabled")
    return</code></pre>
La forma de eliminar el contenido de un componente de clase Text (en este caso, el objeto self.pantalla) es con el método delete. Para que este método pueda modificar el contenido del Text su estado debe ser “normal”, por eso es que lo primero que se hace es cambiarlo (el estado estaba deshabilitado para impedir que el usuario pudiera escribir manualmente en la pantalla). Luego se efectúa el borrado, invocando al método delete y pasándole dos parámetros: desde dónde y hasta dónde borrar. El primer parámetro, “1.0”, indica la primera línea (número 1), primera columna (número 0), ya que ese es el formato que adopta la clase Text para indicar los índices. Y el segundo parámetro (END) indica el final del texto. De esta manera, borramos todo el contenido del objeto pantalla.
Finalmente, volvemos a deshabilitar la pantalla para que el usuario sólo pueda escribir operaciones mediante los botones de la calculadora.

Por último, el método para mostrar texto en la pantalla:
<pre><code>def mostrarEnPantalla(self, valor):
    self.pantalla.configure(state="normal")
    self.pantalla.insert(END, valor)
    self.pantalla.configure(state="disabled")
    return</code></pre>
De la misma forma en que usamos el método delete de la clase Text para borrar el texto, ahora usaremos el método insert para colocar texto. Y en este caso nuevamente necesitamos que el estado del objeto pantalla sea “normal”. Para insertar debemos indicar en qué parte vamos a colocar ese texto, y será al final del texto existente, lo cual se indica con el parámetro END. El siguiente parámetro es el valor a insertar. Y finalmente volvemos a deshabilitar la pantalla para que el usuario no pueda ingresar nada manualmente.

Finalmente, este es el código completo:
<pre><code>from tkinter import Tk,Text,Button,END,re

class Interfaz:
    def __init__(self, ventana):
        #Inicializar la ventana con un título
        self.ventana=ventana
        self.ventana.title("Calculadora")

        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla=Text(ventana, state="disabled", width=40, height=3, background="orchid", foreground="white", font=("Helvetica",15))

        #Ubicar la pantalla en la ventana
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        #Inicializar la operación mostrada en pantalla como string vacío
        self.operacion=""

        #Crear los botones de la calculadora
        boton1=self.crearBoton(7)
        boton2=self.crearBoton(8)
        boton3=self.crearBoton(9)
        boton4=self.crearBoton(u"\u232B",escribir=False)
        boton5=self.crearBoton(4)
        boton6=self.crearBoton(5)
        boton7=self.crearBoton(6)
        boton8=self.crearBoton(u"\u00F7")
        boton9=self.crearBoton(1)
        boton10=self.crearBoton(2)
        boton11=self.crearBoton(3)
        boton12=self.crearBoton("*")
        boton13=self.crearBoton(".")
        boton14=self.crearBoton(0)
        boton15=self.crearBoton("+")
        boton16=self.crearBoton("-")
        boton17=self.crearBoton("=",escribir=False,ancho=20,alto=2)

        #Ubicar los botones con el gestor grid
        botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17]
        contador=0
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila,column=columna)
                contador+=1
        #Ubicar el último botón al final
        botones[16].grid(row=5,column=0,columnspan=4)
        
        return


    #Crea un botón mostrando el valor pasado por parámetro
    def crearBoton(self, valor, escribir=True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda:self.click(valor,escribir))


    #Controla el evento disparado al hacer click en un botón
    def click(self, texto, escribir):
        #Si el parámetro 'escribir' es True, entonces el parámetro texto debe mostrarse en pantalla. Si es False, no.
        if not escribir:
            #Sólo calcular si hay una operación a ser evaluada y si el usuario presionó '='
            if texto=="=" and self.operacion!="":
                #Reemplazar el valor unicode de la división por el operador división de Python '/'
                self.operacion=re.sub(u"\u00F7", "/", self.operacion)
                resultado=str(eval(self.operacion))
                self.operacion=""
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)
            #Si se presionó el botón de borrado, limpiar la pantalla
            elif texto==u"\u232B":
                self.operacion=""
                self.limpiarPantalla()
        #Mostrar texto
        else:
            self.operacion+=str(texto)
            self.mostrarEnPantalla(texto)
        return
    

    #Borra el contenido de la pantalla de la calculadora
    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")
        return
    

    #Muestra en la pantalla de la calculadora el contenido de las operaciones y los resultados
    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")
        return


ventana_principal=Tk()
calculadora=Interfaz(ventana_principal)
ventana_principal.mainloop()
</code></pre>


