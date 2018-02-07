---
layout: post
title: Paso a paso - programa de escritorio en Visual Basic, parte 2
date: 2012-02-06 19:00:00
categories: tutoriales
published: true
---

Este artículo explica cómo conectar una base de datos al programa realizado en la [parte 1](/tutoriales/2012/02/06/tutorial-vb-parte1.html).

El proyecto del programa (para ser importado en Visual Studio y Access) que se va a explicar en este artículo puede descargarse [desde acá]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte2-proyecto.zip).

&nbsp;

## **Conexión con bases de datos**

Para aquellos que desconozcan la importancia y utilidad de trabajar con bases de datos, he aquí una pequeña introducción al tema.

Las bases de datos nos sirven para guardar la información. Algo indispensable para casi cualquier programa, especialmente para aquellos que permiten gestionar y organizar datos, y cuando es necesario realizar las operaciones básicas de altas, bajas y modificaciones (comúnmente llamadas "ABM" o "CRUD" en inglés).

Pensemos en un programa simple que nos ayude a conservar un registro de nuestros ingresos y gastos de dinero, con una ventana que muestre los ingresos ordenados por fecha, otra con los gastos, y otras dos ventanas que permitan dar de alta un nuevo ingreso o un nuevo gasto, para agregarlo al registro. ¿Dónde quedarían almacenados estos datos? ¿Qué instrucciones contendría el botón "Guardar" de cada ventana? ¿Dónde se le indicará que almacene esta información? Claramente, sería inútil guardarla en memoria RAM, ya que se perdería al cerrar la aplicación. Podría guardarse en archivos de registros, pero sería bastante engorroso realizar operaciones sobre ellos (ordenamiento, búsqueda, recuperación de datos, etc.). Lo que viene a solucionar este problema son las bases de datos modernas: sistemas que permiten organizar, almacenar y recuperar grandes cantidades de información fácilmente.

La organización de los datos en las bases de datos se realiza por medio de "tablas". Cada tabla representa una entidad del problema: por ejemplo, las tablas de "Ingresos" y "Gastos". Estas tablas tendrán columnas y filas; las primeras correspondiendo a los diferentes campos en que se divide la información y las segundas conteniendo la información concreta. Por ejemplo, para los gastos podría interesarnos guardar la fecha, el concepto, la cantidad, el modo de pagoâ€¦ Y quedaría algo como esto:

|id|fecha|concepto|modalidad|cantidad|
|---|---|---|---|---|
|1|13/02/2011|Alquiler|Cheque a la orden|1100|
|2|05/03/2011|Combustible|Efectivo|80|
|3|23/03/2011|Seguro médico|Efectivo|230|

Se deben notar dos cosas: la primera es que los nombres de columna se han colocado con palabras simples, sin espacios ni símbolos, y todos en minúscula, para evitar incompatibilidades. La segunda es que se ha agregado un campo "id" como primera columna. Esto permite la identificación unívoca de cada una de las filas, para facilitar las operaciones a realizar sobre los datos (se sabe que la fila con "id" 1 tiene determinados datos y no hay forma de confundirla con otra, lo mismo para la fila 2, la 3, etc.).

Otro detalle es que cada uno de estos campos tiene un "dominio", es decir, los datos que almacene serán todos de un mismo tipo. Por ejemplo, el campo "id" será de tipo autonumérico (para que el sistema le asigne automáticamente un número), la fecha será de tipo Fecha/Hora, el concepto y el modo de pago de tipo Texto, y la cantidad de tipo Número->Doble.

Las bases de datos son administradas utilizando sistemas llamados DBMS ("database management systems"), que son los que permiten operar sobre los datos. Hay DBMS de clases muy variadas y para usos muy diversos. Los hay pagos y libres, también de uso profesional o cotidiano. Estos sistemas requieren la utilización de un lenguaje para realizar consultas a las bases de datos. Una consulta es la "orden" que indica qué operación el usuario quiere realizar (recuperar información, insertar datos, borrar datos, etc.). Algunos DBMS conocidos: Microsoft Access, PostgreSQL, SQLServer, MySQL, FileMaker, Oracle, etc.

En este tutorial se utilizará Microsoft Access 2002, por su facilidad de manejo para quien da sus primeros pasos con las bases de datos. Es un DBMS de uso cotidiano y útil para bases de datos pequeñas (menores a 2GB), pero muy limitado para programas de uso profesional. De todas formas, es una excelente opción para comenzar, ya que es totalmente soportado por Visual Studio, que permite utilizarlo en conjunto con sus herramientas en una forma muy gráfica y simple.

La idea de trabajar con bases de datos es que el usuario no deba operar directamente sobre ellas, sino que luego creemos una aplicación (un programa en VB.Net, en este caso) que proveerá al usuario de una interfaz gráfica "amigable" y adaptada a sus necesidades concretas.

## Creando la base de datos

Dentro de Microsoft Access comenzaremos por crear una base de datos en blanco. Es importante guardarla en una ubicación que luego deberemos recordar, para indicarle a nuestra aplicación dónde está la base de datos con la que debe trabajar. Supongamos para este caso que la ubicación de la base de datos es c:/proyecto/gestion.mdb (mdb es la extensión de los archivos de bases de datos de Access).

Una vez creada la base de datos, vamos a crear dos tablas en vista diseño. En la primera pondremos los siguientes campos: **id** (autonumérico), **fecha** (fecha/Hora), **concepto** (Texto), **modalidad** (Texto), **cantidad** (Número), **cuota_actual** (Número), **cuotas_total** (Número). Al elegir cada tipo de dato, abajo aparecerá un recuadro con más detalles. Dentro de la opción "Tamaño del campo" vamos a especificar "255" para los campos de tipo Texto, "Doble" para el campo "cantidad" (para que permita decimales) y "Fecha general" para el campo "fecha" (por compatibilidad con Visual Studio). Para el campo "id" se debe indicar que no se permitan valores repetidos, por lo que, en la opción "Indexado" deberemos elegir "Sí (Sin duplicados)". Los campos "cuota\_actual" y "cuotas\_total" mantendrán el tipo de dato "Entero Largo", ya que ellos sólo van a almacenar números enteros (si se realiza un pago en cuotas, "cuota\_actual" indicaría el número de cuota pagado y "cuotas\_total" indicaría el total de cuotas a pagar). Por último, vamos a seleccionar el campo "id" y luego, en el menú "Edición", la opción "Clave principal" (para indicar que este será el campo utilizado para identificar unívocamente a cada registro de la tabla). Una vez hecho todo esto, guardaremos esta tabla con el nombre "gastos".

Para crear una nueva tabla -esta vez para los ingresos- repetiremos el proceso, con los campos **id** (autonumérico), **fecha** (fecha/Hora), **concepto** (Texto), **modalidad** (Texto) y **cantidad** (Número). Y, nuevamente, para los campos de tipo Texto pondremos el tamaño máximo en 255, para la fecha el formato "Fecha general" y para la cantidad el tipo "Doble". Esta será la tabla "Ingresos".

Ya tenemos la base de datos creada y ahora sólo resta programar la interfaz visual para trabajar con ella.


## La interfaz con el usuario

En la creación de la interfaz se utilizarán los conocimientos básicos para trabajar con formularios y objetos de VB.NET, vistos en la [primera parte](/tutoriales/2012/02/06/tutorial-vb-parte1.html), por lo que no se volverán a explicar en forma detallada.

Empezamos por crear un nuevo proyecto de Visual Basic, al que llamaremos GestionDeGastos.

En el formulario principal, al que llamaremos Main y frmMain para su nombre de objeto, vamos a poner algunos labels y tres botones para acceder a las diferentes opciones que queremos que tenga este programa: "Ingresos", "Gastos" y "Saldo" (el diseño de los formularios y sus componentes queda librado a la imaginación de cada programador, aunque en el mundo profesional esta tarea se deja a los diseñadores gráficos). A los botones vamos a llamarlos btnIngresos, btnGastos y btnSaldo respectivamente. El botón btnIngresos va a abrir un formulario Ingresos (frmIngresos), btnGastos abrirá un formulario llamado Gastos (frmGastos) y btnSaldo abrirá el formulario Saldo (frmSaldo). El botón Salir cerrará la aplicación llamando al método <code>Application.Exit()</code>.

![pantalla inicial]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte2-img1.jpg)

En el formulario Ingresos colocaremos un DataGridView, que será la grilla donde se van a ver los datos de la tabla "ingresos" de la base de datos. Al objeto DataGridView le pondré el nombre dgvIngresos. Clickeando sobre la flecha en la parte superior derecha del DataGridView se verán una serie de opciones y un menú desplegable que indica "Elegir origen de datos". Clickeando en este menú seleccionamos "Agregar origen de datos al proyecto".

De las opciones elegiremos la primera ("Base de datos") y en la siguiente ventana, "Conjunto de datos". Clickeando en "Nueva conexión" aparecerá un recuadro que mostrará un botón Examinar en la sección "Nombre del archivo de la base de datos". Presionando este botón vamos a elegir la ruta a nuestra base de datos. En este caso, **C:\proyecto\gestion.mdb**. Podemos usar el botón "Probar conexión" para saber que se está conectando correctamente a la base de datos.

![crear conexión a la base de datos]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte2-img2.jpg)

Una vez hecho esto, Aceptar y presionar "Siguiente" en la ventana que estaba por debajo. Si la base de datos no está en la misma carpeta del proyecto de VB.NET, aparecerá un cartel preguntando si se desea copiarla a la carpeta del proyecto. Esto queda a decisión del programador, pero es buena idea tener todos los archivos en un mismo sitio cuando deseamos transportar el proyecto de un lugar a otro. Presionar "Siguiente" en el paso que aparece a continuación para que aparezca la vista con el contenido de la base de datos.

![seleccionar origen de datos]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte2-img3.jpg)

En esta ventana deberemos seleccionar la tabla desde la cual queremos traer los datos. Se generará un objeto _DataSet_, que representa a los datos de la base de datos, pero en memoria. Los DataSet contienen objetos DataTable, que son los que mantienen la información de las tablas que seleccionamos y permiten realizar operaciones sobre ella. En este caso, llamaremos ingresosDataSet al DataSet que se está creando con la tabla "ingresos". Al presionar el botón Finalizar se deberían ver las columnas de la tabla en el _DataGridView_.

![DataGridView]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte2-img4.jpg)

Además del DataGridView, al formulario vamos a ponerle botones para Agregar (btnAgregar), Eliminar (btnEliminar) y Modificar (btnModificar) datos: las famosas operaciones "ABM". También vamos a poner abajo algunos TextBox y dos DateTimePicker, que permitan filtrar los datos de la tabla.
  
![agregando componentes]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte2-img5.jpg)

Ahora vamos a editar las columnas del _DataGridView_, para que no muestre los nombres que tienen en la tabla de la base de datos, sino algo más adecuado. Para esto, hacemos click derecho sobre el DataGridView y elegimos la opción "Editar Columnas". En la ventana que aparece, se podrá elegir ocultar algunas columnas y cambiar el texto de cada una. Por ejemplo, seleccionando la columna **id**, se puede settear su propiedad _Visible_ en _False_. Es importante ponerla como invisible pero no eliminarla (lo que se haría usando el botón "Quitar"), ya que es imprescindible que esta columna permanezca (aunque oculta) en el _DataGridView_ para que, al seleccionar una fila de la tabla, se la pueda identificar utilizando el número de id de esa fila. También vamos a cambiar el título utilizando la propiedad _HeaderText_.

![editar columnas]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte2-img6.jpg)

El formato de los datos de las columnas se puede escoger seleccionando cada una y editando la propiedad DefaultCellStyle. En la columna Fecha vamos a seleccionar el Comportamiento "Format" y elegir el Tipo de Formato "Date Time" y el Tipo "dd/mm/aa hh:mm:ss p.m.", para que coincida con el formato de fecha elegido en la base de datos.
  
![formato de fecha]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte2-img7.jpg)

De la misma forma, vamos a editar el formato de la columna "cantidad", poniéndole un _HeaderText_ como "Monto en $" y eligiendo el Tipo de Formato "Moneda".

Algo que también es importante es configurar la propiedad _MultiSelect_ en _False_, para que el usuario no pueda seleccionar más de una fila por vez, y _SelectionMode_ del _DataGridView_ a _FullRowSelect_. Esto hará que no puedan seleccionarse celdas individuales, sino filas completas.

![modo de selección]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte2-img9.jpg)

Ahora vamos a configurar las acciones de los botones. La primera que haremos es la de eliminar, que es la más sencilla.

Al hacer doble click sobre el botón _Eliminar_, aparecerá el código del formulario. Pero antes de programar cualquier operación sobre la base de datos será necesario importar las clases que manejan los objetos ADO.NET necesarios para trabajar con esta base de datos. Para esto, vamos a agregar la siguiente línea al principio de todo (por encima de la línea _Public Class frmIngresos_): <code>Imports System.Data.OleDb</code>.

En el botón _Eliminar_, vamos a hacer una llamada a un procedimiento que será el encargado de eliminar la fila seleccionada, y una línea que volverá a rellenar el _DataGridView_ para actualizarlo con la modificación efectuada:

<pre><code>If MessageBox.Show("¿Desea eliminar el registro seleccionado?", "Eliminar", MessageBoxButtons.OKCancel, MessageBoxIcon.Question) = Windows.Forms.DialogResult.OK Then
    elimina(dgvIngresos.CurrentRow.Cells(0).Value)
End If
IngresosTableAdapter.Fill(Me.IngresosDataSet.ingresos)</code></pre>

La línea que llama al procedimiento "elimina" le envía como argumento el número de _id_ de la fila que se encuentra seleccionada: al _dgvIngresos: se le "pide" la fila actualmente seleccionada con la propiedad _CurrentRow_. De esa fila se obtiene la colección _Cells_, que contiene las celdas de la fila, y se indica que se seleccione la primera celda (la correspondiente a la primera columna), que es la que lleva el índice 0, y luego con la propiedad Value se obtiene el valor contenido en ella.

La grilla con una fila seleccionada se verá en forma similar a esto:
  
![grilla con fila seleccionada]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte2-img8.jpg)

Como anteriormente pusimos a la columna **id** como invisible, no podemos verla. Pero esto no significa que no exista. Por ello es que resulta importante _no quitar_ esa columna _ni cambiarla de lugar_, ya que es nuestra forma de saber que la primera columna (la primera -es decir, la número 0- de la colección de celdas) siempre será la que contenga el número de id que identificará la fila.

Para escribir la última línea (que actualiza la grilla), dentro del menú Datos del IDE seleccionamos Mostrar orígenes de Datos y esto hará que a la izquierda aparezca la lista de los DataTable generados hasta el momento. Con un click derecho sobre la tabla "ingresos" se podrá ver la opción "Editar DataSet con el diseñador", que mostrará la tabla y, debajo de ella, el comando (que se transforma en SQL) usado para rellenarla. Inicialmente (a menos que agreguemos otro), el comando va a ser algo como "Fill,GetData()". Así, la línea que recarga la grilla estará compuesta por: el nombre del TableAdapter (_IngresosTableAdapter_), el nombre del comando ("Fill"), y como argumentos el formulario actual (_Me_), el DataSet (_IngresosDataSet_) y el nombre de la tabla (_ingresos_). El nombre del TableAdapter y el DataSet pueden verse en la parte inferior de la vista de Diseño del formulario.

El código del procedimiento "elimina" será algo similar al siguiente (las líneas antecedidas por el carácter ' son comentarios):

<pre><code>Private Sub elimina(ByVal pk As String)
    'se crea la conexión a la base de datos
    Dim laConexion As OleDbConnection
laConexion = New OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\proyecto\gestion.mdb" )
   'se crea el objeto de comando SQL
    Dim elComando As OleDbCommand
    elComando = New OleDbCommand("delete from ingresos where id = " + pk, laConexion)
    Try
        laConexion.Open()
        'se instancia un objeto para conectar a la tabla
        Dim objetoLector As OleDbDataReader
        objetoLector = elComando.ExecuteReader()
        MessageBox.Show("Registro eliminado exitosamente", "Completado", MessageBoxButtons.OK, MessageBoxIcon.Information)
        objetoLector.Close()
    Catch ex As OleDbException
        MessageBox.Show(ex.Message)
    Finally
        'se cierra la conexión
        laConexion.Close()
    End Try
End Sub</code></pre>

Sin ahondar demasiado en detalles del lenguaje SQL, en este procedimiento se puede observar la consulta SQL utilizada para eliminar información de una tabla: <code>delete from ingresos where id = ...</code>

"Delete from" es la operación a realizar (eliminar). Lo siguiente ("ingresos") es el nombre de la tabla sobre la cual se va a realizar la acción. La última parte indica una condición a cumplir, y es lo que voy a utilizar para indicarle cuál de las filas borrar.

Como se vio antes, el método _elimina()_ recibe como parámetro un número al que llama "pk" (por "primary key"). La línea que llama a este procedimiento le envía como argumento el número que contiene la columna "id" de la fila que se encuentra seleccionada, por lo que la variable "pk" va a contener el número de id de la fila a borrar. Como el número de id es único para cada una de las filas, sólo cabe la posibilidad de que se elimine la fila que el usuario seleccionó. Así, la porción de código <code>"where id ="</code> está diciendo que se elimine aquella fila en que el contenido de la columna id coincida con el número que representa la variable "pk". Como la consulta SQL se envía en forma de string, lo que estamos haciendo al indicar <code>"delete from ingresos where id = " + pk</code> es concatenar el número dado por _pk_ al final del string que contiene la consulta SQL.

Pongamos un ejemplo: en la imagen de más arriba se ve que se encuentra seleccionada la fila que tiene como fecha el 10/10/2010, el concepto "Honorarios judicial", la forma de pago "giro" y el monto $1500. Pero a todo esto sabemos que se encuentra asociado un número de id, oculto, que se genera automáticamente cada vez que se inserta un nuevo dato en la tabla. Supongamos que el número de id de esta fila que tenemos seleccionada es el 17. Entonces, esta porción del código: <code>dgvIngresos.CurrentRow.Cells(0).Value</code> devolverá el valor 17. Ese es el valor que se le está pasando al método _elimina()_, y el valor que adopta el parámetro _pk_. Así, cuando se construye el comando SQL concatenándole el valor de _pk_ al string que lo contiene, en realidad estamos diciéndole: <code>delete from ingresos where id = 17</code> (borrar de la tabla ingresos aquella fila donde id sea igual a 17).

A continuación, para permitir el ingreso de nuevos datos y la modificación de los actuales, necesitaremos crear dos nuevos formularios con características muy similares. En uno vamos a tener espacios en blanco para ingresar datos nuevos, y en el otro esos espacios se cargarán con los datos de la fila que el usuario seleccione para modificar:

![crear nuevos formularios]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte2-img10.jpg)

Como en el resto de los formularios, el evento _Click_ del botón _btnSalir_ va a tener el código <code>Me.Close()</code>.

El botón "Borrar" va a servir para limpiar los datos de todos los campos a la vez. Por lo que su evento Click disparará un código similar al siguiente:

<pre><code>dtpFecha.Value = Now
txtConcepto.Text = ""
txtModalidad.Text = ""
txtCantidad.Text = ""</code></pre>

A la propiedad Value del _DateTimePicker_ se le asigna _Now_, que obtiene la fecha del sistema (fecha actual). A la propiedad _Text_ de los _TextBox_ se le asigna el string vacío "".

El evento _Click_ del botón Aceptar de este formulario va a ejecutar la acción de insertar en la tabla "ingresos" de la base de datos los datos que el usuario haya cargado en los _TextBox_ y el _DateTimePicker_. Pero esto necesita algún tipo de validación de datos. Por ejemplo, que no se hayan dejado campos vacíos, o que no se ingresen letras o símbolos en los campos que requieren números. La validación es un gran tema aparte que recomiendo dejar para una vez el programa esté completo y funcionando, ya que puede consumir bastante tiempo. Pero una validación posible sería algo como lo siguiente:

<pre><code>If (Trim(txtConcepto.Text) <> "")  And (Trim(txtModalidad.Text) <> "")  And (Trim(txtCantidad.Text) <> "")  Then 
    agregadatos() 
Else 
    MessageBox.Show("Debe completar datos antes de agregar", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error) 
End If</code></pre>

Para cada uno de los campos se utilizó el método _Trim()_ que elimina los espacios al comienzo y al final de un string (para evitar que el usuario ingrese algo como " Honorarios "), y la condición fuerza a que ninguno de los campos esté vacío para poder llamar al método _agregadatos()_, que será el que va a ejecutar la operación sobre la base de datos. Este método tendrá el siguiente código:

<pre><code>Private Sub agregadatos() 
   'se crea la conexión a la base de datos
    Dim laConexion As OleDbConnection 
    laConexion = New OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\proyecto\gestion.mdb")
    'se guardan en variables los valores ingresados por el usuario en tiempo de ejecución
    Dim campo1, campo2, campo3, campo4 As String 
    campo1 = dtpFecha.Value 
    campo2 = txtConcepto.Text 
    campo3 = txtModalidad.Text() 
    campo4 = txtCantidad.Text 
   'se crea el objeto de comando SQL
    Dim elComandoAs OleDbCommand 
   'la inserción se realiza utilizando parámetros que se pasan luego asignándole el valor de las variables campo1, campo2, campo3 y campo4.</span> 
    elComando = New OleDbCommand("insert into ingresos (fecha,concepto,modalidad,cantidad) values (@fecha,@concepto,@modalidad,@cantidad)", laConexion) 
    elComando.Parameters.AddWithValue("@fecha", campo1) 
    elComando.Parameters.AddWithValue("@concepto", campo2) 
    elComando.Parameters.AddWithValue("@modalidad", campo3) 
    elComando.Parameters.AddWithValue("@cantidad", campo4) 
    Try 
        laConexion.Open() 
        'crear objeto datareader para conectar a la tabla</span> 
        Dim objetoLector As OleDbDataReader 
        objetoLector = elComando.ExecuteReader() 
        MessageBox.Show("Registro insertado exitosamente", "Completado", MessageBoxButtons.OK, MessageBoxIcon.Information) 
        objetoLector.Close() 
    Catch ex As OleDbException 
        MessageBox.Show(ex.Message) 
    Finally 
    'se cierra la conexión
        laConexion.Close() 
    End Try 
End Sub</code></pre>

La consulta SQL funciona de forma bastante similar a la del método que elimina visto anteriormente. Sólo que en esta oportunidad se utiliza la operación _insert_ y los datos se ingresan por medio de parámetros, que se identifican con una @ delante para luego pasarles un valor (el de las variables que contienen lo ingresado por el usuario en el formulario) usando el método _AddWithValue()_ de la colección de parámetros del objeto _OleDbCommand_.

El formulario que se abrirá al presionar el _btnModificar_ de _frmIngresos_ necesitará tener previsto algo más aparte de la operación SQL para modificar los datos, ya que será necesario que se carguen los datos de la fila que se encuentre seleccionada. Para esto, en el botón btnModificar del frmIngresos se instancia el formulario de modificación de datos (suponiendo que éste se llama IngresosModificar y que el nombre de instancia a utilizar será frmIngresosModificar) de la siguiente manera:

<pre><code>Dim frmIngresosModificar = New IngresosModificar(dgvIngresos.CurrentRow.Cells(0).Value)
frmIngresosModificar.Show</code></pre>

Esto instancia un objeto de tipo IngresosModificar, llamado frmIngresosModificar y lo abre. Pero, para que no de un error de "demasiados parámetros", el formulario frmIngresosModificar debe estar preparado para recibir un parámetro al ser instanciado. Para esto, en el código del formulario IngresosModificar vamos a declarar una variable de tipo string que reciba el valor de la fila seleccionada (lo toma como string, aunque sea un número), y en el constructor que inicializa el formulario le indicamos que reciba por valor (ByVal) un string, que será el valor que se asigne a la variable:

<pre><code>Public Class IngresosModificar
    'se declara una variable de tipo string
    Dim valorFilaSeleccionada As String
    'al constructor del formulario se le agrega un parámetro que va a recibir por valor, de tipo string</span>
    Public Sub New(ByVal fila As String)
        InitializeComponent()
        'luego de la inicialización de componentes que se hace automáticamente, se le asigna el valor recibido como parámetro a la variable declarada antes:</span>
        valorFilaSeleccionada = fila
    End Sub</code></pre>

El formulario _frmModificar_ tendrá preparada una interfaz prácticamente igual a la del formulario utilizado para insertar un nuevo registro, que permitirá recibir los datos que vienen de la base de datos. Esto hará que, al abrirse el formulario, se vean los datos de la fila que se seleccionó para modificar. Para esto, en el evento Load del formulario se debe traer de la base de datos el registro correspondiente a la fila seleccionada:

<pre><code>Private Sub IngresosModificar_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
    'se crea la conexión a la base de datos
    Dim laConexion As OleDbConnection
    laConexion = New OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\proyecto\gestion.mdb")
    'se crea el objeto de comando SQL
    Dim elComando As OleDbCommand
    elComando = New OleDbCommand("select * from ingresos where id = " + valorFilaSeleccionada, laConexion)
    Try
        laConexion.Open()
        <span style="color: #339966;">'se instancia un objeto para conectar a la tabla
        Dim objetoLector As OleDbDataReader
        objetoLector = elComando.ExecuteReader()
        'se itera sobre la base de datos para ir obteniendo todas las columnas del registro sobre variables temporales
        While (objetoLector.Read())
            Dim campo1 As Date
            Dim campo2, campo3 As String
            Dim campo4 As Double
            campo1 = objetoLector.GetDateTime(1)
            campo2 = objetoLector.GetString(2)
            campo3 = objetoLector.GetString(3)
            campo4 = objetoLector.GetDouble(4)
            'se asignan los datos contenidos en las variables a los controles de la interfaz visual
            dtpFecha.Value = campo1
            txtConcepto.Text = campo2
            txtModalidad.Text = campo3
            txtCantidad.Text = campo4
        End While
        objetoLector.Close()
    Catch ex As OleDbException
        MessageBox.Show(ex.Message)
    Finally
        'se cierra la conexión
        laConexion.Close()
    End Try
End Sub</code></pre>

Algo importante es que en la base de datos puede haber diferentes tipos de datos y, al hacer la lectura, éstos deben leerse según su tipo. Por esto es que instanciamos variables de tipo String, Double y Date, que son los tipos de datos contenidos en la tabla _ingresos_. Pero también debe tenerse en cuenta esto al utilizar el objeto _OleDbDataReader_ para extraer los valores de la base de datos, al llamar al método _get_ de la siguiente forma: <code>objetoLector.GetDateTime(1)</code>. También debe notarse que el método recibe un número como argumento. Ese es el número de columna de la cual debe extraer el dato, teniendo en cuenta que la numeración comienza desde el 0. Recordando que nuestra primera columna es la _id_ (que sería la número 0), en este caso comenzamos por la número 1, que es la columna _fecha_.

En cuanto al comando SQL, usamos la consulta _select_, que selecciona las filas y columnas que cumplan con los criterios indicados. Con el asterisco se le indica que seleccione todas las columnas (aunque también podría haberlas mencionado una a una) y con la cláusula _where_ se le indica que debe seleccionar aquellas filas cuyo campo _id_ coincida con el número que contiene la variable _valorFilaSeleccionada_ (que será una sola).

Hasta acá sólo hemos logrado cargar la información de la fila seleccionada en la grilla, pero aún no se modificó nada. Lo que resta es que, una vez el usuario ha modificado los datos que creyó necesarios, el registro sea nuevamente insertado dentro de la base de datos. No importa saber cuál de todos los valores modificó y cuál dejó sin modificar, porque vamos a volver a insertar todo el registro, sobreescribiendo al anterior. Para esto, el botón btnAceptar debe llamar al siguiente método:

<pre><code>Private Sub modifica()
    'se crea la conexión a la base de datos
    Dim laConexion As OleDbConnection
    laConexion = New OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\proyecto\gestion.mdb")
    'se guardan en variables los valores ingresados
    Dim campo1 As Date
    Dim campo2, campo3 As String
    Dim campo4 As Double
    campo1 = dtpFecha.Value
    campo2 = Trim(txtConcepto.Text)
    campo3 = Trim(txtModalidad.Text)
    campo4 = CDbl(Trim(txtCantidad.Text))
    'se crea el objeto de comando SQL
    Dim elComando As OleDbCommand
    elComando = New OleDbCommand("update ingresos set fecha = @fecha, concepto = @concepto, modalidad = @modalidad, cantidad = @cantidad where id = " + valorFilaSeleccionada, laConexion)
    elComando.Parameters.Add("@fecha", campo1)
    elComando.Parameters.Add("@concepto", campo2)
    elComando.Parameters.Add("@modalidad", campo3)
    elComando.Parameters.Add("@cantidad", campo4)
    Try
        laConexion.Open()
        'se instancia un objeto para conectar a la tabla
        Dim objetoLector As OleDbDataReader
        objetoLector = elComando.ExecuteReader()
        MessageBox.Show("Registro modificado", "Completado", MessageBoxButtons.OK, MessageBoxIcon.Information)
        objetoLector.Close()
    Catch ex As OleDbException
        MessageBox.Show(ex.Message)
    Finally
        'se cierra la conexión
        laConexion.Close()
        Me.Close()
    End Try
End Sub</code></pre>

Si alguno de los datos de la base de datos fueran de otro tipo diferente a string, esto debe preverse al asignar los valores a las variables. Por ejemplo, si en la interfaz tenemos un _TextBox_ para que el usuario ingrese un número (como sucede con el _txtCantidad_), y sabemos que eso va a ir insertado en una columna de la base de datos que contiene valores de tipo Double, vamos a tener que convertir el dato que contiene el valor _txtCantidad.Text_, ya que la propiedad _Text_ de los _TextBox_ devuelve siempre un _string_.

La conversión de valores de un tipo a otro se efectúa con un método de "casting". Es importante haber validado los datos antes (por ejemplo, no intentar convertir a número algo que puede contener letras). En este caso, no convertimos al tipo _Date_ el valor retornado por la propiedad _Value_ del _DateTimePicker_ porque ésta devuelve siempre un dato de tipo _Date_. En cambio, sí fue necesario convertir a tipo _Double_ lo ingresado en el _txtCantidad_, ya que el contenido de un _TextBox_ obtenido con la propiedad _Text_ es siempre un string. Para esto se usó el método _CDbl()_, que convierte el argumento a _Double_. Otros métodos de casting son: **CInt()** -convierte a Integer-, **CDate()** -convierte a Date-, **CStr()** -convierte a String).

Con esto ya queda solucionada la inserción, modificación y eliminación de datos en la base de datos. Pero resta una de las funcionalidades que contiene el formulario Ingresos, que es la búsqueda de información para filtrar los registros mostrados en el _DataGridView_.

El botón "Borrar" va a hacer lo mismo que en los casos anteriores: volver todos los campos a cero para borrar lo que haya escrito el usuario. En este caso, como necesitamos reutilizar el código, vamos a poner las instrucciones en un nuevo procedimiento, que vamos a llamar dentro del evento _Click_ del botón.

<pre><code>Private Sub limpiarCampos()
    dtpDesde.Value = Now
    dtpHasta.Value = Now
    txtConcepto.Text = ""
    txtModalidad.Text = ""
End Sub</code></pre>

El botón "Ver todo" elimina los filtros de búsqueda aplicados por el usuario y vuelve a mostrar todo el contenido de la tabla, además de limpiar los campos. Así que su código será el mismo que el que usa el botón "Eliminar" para refrescar los datos de la grilla, además de llamar al procedimiento que limpia los campos para volverlos a su estado inicial:

<pre><code>IngresosTableAdapter.Fill(Me.IngresosDataSet.ingresos)
limpiarCampos()</code></pre>

El botón "Buscar" va a tener que filtrar los resultados mostrados en la grilla de acuerdo a los criterios definidos por el usuario: fecha (desde - hasta), concepto y forma de pago. Para esto se necesitará crear una consulta SQL que cumpla con estos criterios, y para crearla vamos a ver nuevamente la vista de diseño de la tabla ingresos (**Datos > Mostrar orígenes de datos > click derecho sobre el dataset de la tabla**). Donde veamos la representación gráfica de la tabla, habrá una sección sombreada en gris que dirá _ingresosTableAdapter_. Haciendo click derecho sobre ella, seleccionamos "Agregar consulta". En las dos ventanas a continuación damos "Siguiente" hasta que aparece la ventana que muestra el recuadro con la consulta SQL. Se mostrará una consulta genérica como <code>SELECT id, fecha, concepto, modalidad, cantidad FROM ingresos</code>, que es la consulta que rellena la grilla al cargarse el formulario. Para efectuar el filtro, reemplazaremos esa consulta por la siguiente: <code>SELECT id, fecha, concepto, modalidad, cantidad FROM ingresos WHERE (fecha between ? and ?) and (concepto like '%'+?+'%') and (modalidad like '%'+?+'%') order by fecha</code>

La cláusula _WHERE_ está indicando que los valores de las columnas coincidan con lo ingresado por el usuario, y los signos de pregunta ("?" ) representan parámetros, que le pasaremos desde el evento _Click_ del botón Buscar. La última cláusula, "order by fecha" indica que ordene los resultados por fecha (orden ascendente, por defecto).

Al presionar "Siguiente" vamos a desactivar la opción "Devolver un DataTable" y como nombre de método, en la opción "Rellenar un DataTable", vamos a ingresar la palabra "BuscarIngresos". Una vez creada la consulta, volvemos al código del formulario _Ingresos_ y al del evento _Click_ del _btnBuscar_. El código que va a ejecutar este botón es el siguiente:

<pre><code>Try
    IngresosTableAdapter.BuscarIngresos(Me.IngresosDataSet.ingresos, dtpDesde.Value,
    dtpHasta.Value, txtConcepto.Text, txtModalidad.Text)
Catch ex As System.Exception
    System.Windows.Forms.MessageBox.Show(ex.Message)
End Try</code></pre>

Esto llama al método _BuscarIngresos_ que acabamos de crear en el _TableAdapter_, y le pasa como argumentos la tabla sobre la cual efectuar la operación y luego la información que se ingresó en los campos de filtrado del formulario. Se debe tener en cuenta que los criterios de búsqueda deben coincidir con el tipo de datos que estén en la tabla (por ejemplo, si hubiera agregado un _TextBox_ para filtrar por "cantidad", el argumento debería ser convertido a _Double_ antes de enviarse a la consulta, ya que el _TextBox_ devolvería el valor en forma de string).
  
![filtrado de ingresos]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte2-img11.jpg)

Para el formulario de _Gastos_ el proceso es muy similar, por lo que no se reiterará. El que sí es diferente es el formulario de _Saldo_, que mostrará un balance entre ingresos y gastos según el filtro de fechas que se le indique. El diseño podría ser algo similar al siguiente:
  
![filtrado de saldos]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte2-img12.jpg)

En este caso, colocamos dos _DateTimePicker_ para permitir al usuario elegir un rango de fechas para obtener el saldo de ese período. Además, hay tres _Labels_ cuyo contenido va a variar. Los llamaremos _lblSaldoIngresos_, _lblSaldoGastos_ y _lblSaldoTotal_, y el texto que muestran, inicialmente, son tres guiones: "---". Este contenido va a cambiar al momento en que el usuario presione el botón "Ver Saldo", al que llamaremos _btnVerSaldo_, para mostrar el cálculo que corresponde al saldo (positivo o negativo) de dinero.

Para obtener el saldo, debemos sumar todos los valores de la columna "cantidad" de la tabla _ingresos_ que coincidan con el rango de fechas dado, y luego hacer lo mismo para la tabla _gastos_; finalmente se restan ambos valores y el resultado se muestra en el _lblSaldoTotal_.

A la suma de los valores de la columna "cantidad" vamos a hacerla en dos pasos, para evitar confusiones. Por lo que el botón _btnVerSaldo_ va a contener un código como el siguiente:

<pre><code>If dtpDesde.Value <= dtpHasta.Value Then
    Dim totalIngresos As Double = 0
    Dim totalGastos As Double = 0
    obtenerIngresosTotal(totalIngresos)
    lblSaldoIngresos.Text = totalIngresos
    obtenerGastosTotal(totalGastos)
    lblSaldoGastos.Text = totalGastos
    lblSaldoTotal.Text = totalIngresos - totalGastos
    If totalIngresos - totalGastos < 0 Then
        lblSaldoTotal.ForeColor = Color.Red 
    End If
Else
    MessageBox.Show("La fecha inicial no puede ser mayor a la fecha final", "Rango de fecha incorrecto", MessageBoxButtons.OK, MessageBoxIcon.Information)
End If</code></pre>

Y el código de los métodos _obtenerIngresosTotal()_ y _obtenerGastosTotal()_ será como el siguiente (cambiando únicamente en el nombre de la tabla en la consulta SQL):

<pre><code>Private Sub obtenerIngresosTotal(ByRef total As Double)
    'se crea la conexión a la base de datos
    Dim laConexion As OleDbConnection
    laConexion = New OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source= C:\proyecto\gestion.mdb")
    'se crea el objeto de comando SQL
    Dim elComando As OleDbCommand
    elComando = New OleDbCommand("select * from ingresos where fecha between @fecha1 and @fecha2", laConexion)
    elComando.Parameters.AddWithValue("@fecha1", dtpDesde.Value)
    elComando.Parameters.AddWithValue("@fecha2", dtpHasta.Value)
    Try
        laConexion.Open()
        'se instancia un objeto para conectar a la tabla
        Dim objetoLector As OleDbDataReader
        objetoLector = elComando.ExecuteReader()
        'se itera sobre la base de datos para ir obteniendo los valores de la columna requerida y sumándolos a una variable
        While (objetoLector.Read())
            total = total + objetoLector.GetDouble(4)
        End While
        objetoLector.Close()
    Catch ex As OleDbException
        MessageBox.Show(ex.Message)
    Finally
        'se cierra la conexión
        laConexion.Close()
    End Try
End Sub</code></pre>

Nótese que el texto del saldo se muestra en color rojo si el saldo es negativo:

![vista del saldo en el formulario]({{ site.url }}/assets/2012-02-06-tutorial-vb-parte2-img13.jpg)
