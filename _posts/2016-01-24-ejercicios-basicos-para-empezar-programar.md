---
layout: post
title: Ejercicios básicos para empezar a programar
date: 2016-01-24 19:00:00
categories: ejercicios
published: true
---

A continuación se listan algunos ejercicios muy básicos para comenzar a programar, utilizando sólo cálculos matemáticos, asignación de variables y entrada/salida de datos. Además se ofrecen tres resoluciones posibles (en Python, Java y C++).

_Nota_: las resoluciones propuestas pueden no ser las únicas factibles ni las más eficientes. Se incluyen sólo a modo de guía para la auto-corrección.
  

## Ejercicio 1
> Una persona utiliza una brújula para tomar ciertas mediciones dentro de una casa. Como los aparatos electrónicos modifican los campos magnéticos y afectan la medición, deben tomarse varias de ellas para estar seguros de tener un número lo más acertado posible. La persona que toma las mediciones se para mirando en dirección a la puerta, con la brújula en la mano, y anota los grados que indica la brújula. Luego se para en otra habitación del edificio, nuevamente en dirección a la puerta, y vuelve a anotar. Vuelve a hacer lo mismo en una habitación diferente, siempre mirando a la puerta, y anota una tercera medición. Escribir un programa que calcule el número más acertado para la medición.

### Resolución - ejercicio 1

* **Python**

<pre><code>valor1=int(input("Ingrese el primer valor"))
valor2=int(input("Ingrese el segundo valor"))
valor3=int(input("Ingrese el tercer valor"))
print((valor1+valor2+valor3)/3)</code></pre>

* **Java**

<pre><code>import java.util.Scanner;
public class prueba {
        public static void main(String[] args) {
            Scanner entrada = new Scanner(System.in);
            double valor1;
            double valor2;
            double valor3;
            System.out.print("Primer valor registrado: ");
            valor1 = entrada.nextDouble();
            System.out.print("Segundo valor registrado: ");
            valor2 = entrada.nextDouble();
            System.out.print("Tercer valor registrado: ");
            valor3 = entrada.nextDouble();
            System.out.println((valor1+valor2+valor3)/3);
            entrada.close();
        }
}</code></pre>

* **C++**

<pre><code>#include &lt;iostream&gt;
using namespace std;
int main()
{
        double valor1;
        double valor2;
        double valor3;
        cout &lt;&lt; "Primer valor registrado: ";
        cin &gt;&gt; valor1;
        cout &lt;&lt; endl &lt;&lt; "Segundo valor registrado: ";
        cin &gt;&gt; valor2;
        cout &lt;&lt; endl &lt;&lt; "Tercer valor registrado: ";
        cin &gt;&gt; valor3;
        cout &lt;&lt; (valor1+valor2+valor3)/3 &lt;&lt; endl;
        return 0;
}</code></pre>

---

## Ejercicio 2

> Calcular el precio total a pagar por una cena en un restaurante, permitiendo al usuario ingresar el valor de la comida, el recargo por cubiertos (a modo de porcentaje) y un porcentaje de propina. Mostrar en pantalla el precio total.

### Resolución - ejercicio 2

* **Python**

<pre><code>comida=float(input("Valor de la comida: $"))
porcentaje_cubierto=float(input("Porcentaje de recargo por cubiertos: "))
porcentaje_propina=float(input("Porcentaje de propina: "))
valor_cubierto=(porcentaje_cubierto*comida)/100
valor_propina=(porcentaje_propina*comida)/100
total=comida+valor_cubierto+valor_propina
print("Total a pagar: $", total)</code></pre>

* **Java**

<pre><code>import java.util.Scanner;
public class Restaurante {
        public static void main(String[] args) {
            Scanner entrada = new Scanner(System.in);
            double comida;
            double porcentaje_cubierto;
            double porcentaje_propina;
            System.out.print("Valor de la comida: $");
            comida = entrada.nextDouble();
            System.out.print("Porcentaje de recargo por cubiertos: ");
            porcentaje_cubierto = entrada.nextDouble();
            System.out.print("Porcentaje de propina: ");
            porcentaje_propina = entrada.nextDouble();
            double valor_cubierto=(porcentaje_cubierto*comida)/100;
            double valor_propina=(porcentaje_propina*comida)/100;
            double total=comida+valor_cubierto+valor_propina;
            System.out.println("Total a pagar: $" + total);
            entrada.close();
        }
}</code></pre>


* **C++**

<pre><code>#include &lt;iostream&gt;
using namespace std;
int main()
{
        double comida;
        double porcentaje_cubierto;
        double porcentaje_propina;
        cout &lt;&lt; "Valor de la comida: $";
        cin &gt;&gt; comida;
        cout &lt;&lt; endl &lt;&lt; "Porcentaje de recargo por cubiertos: ";
        cin &gt;&gt; porcentaje_cubierto;
        cout &lt;&lt; endl &lt;&lt; "Porcentaje de propina: ";
        cin &gt;&gt; porcentaje_propina;
        double valor_cubierto=(porcentaje_cubierto*comida)/100;
        double valor_propina=(porcentaje_propina*comida)/100;
        double total=comida+valor_cubierto+valor_propina;
        cout &lt;&lt; "Total a pagar: $" &lt;&lt; total &lt;&lt; endl;
        return 0;
}</code></pre>

---

## Ejercicio 3

> Un empresario que se dedica al espectáculo quiere tener una herramienta (un programa) que le ayude a sacar ciertos cálculos cada vez que trae una banda a tocar en algún estadio.
>
>Lo primero que necesita saber es cuánta gente va a poder asistir a cada recital. Para eso, cuando arregla con un club para usar su estadio, pregunta cuántos metros cuadrados tiene. Él sabe que, por metro cuadrado, entran 4 personas. También sabe que las tribunas ocupan un 20% de ese espacio, entonces pregunta cuántas personas caben en las tribunas.
>
> Cuando contrata a la banda que va a tocar, le pregunta qué porcentaje del espacio necesitan ellos para su escenario.
>
> Con estos datos, debe calcularse cuánta gente va a caber en el estadio para un recital determinado, para saber cuántas entradas tiene que mandar a imprimir. El empresario, cada vez que use el programa, va a ingresar la cantidad de metros cuadrados que tiene el estadio que contrató, la cantidad de gente que cabe en las tribunas y el porcentaje de espacio ocupado por el escenario.
>
> Luego, él quiere saber cuánto dinero ingresaría si vende todas las entradas disponibles, sabiendo que el 30% de las entradas vendidas son "entradas vip" y el resto son "entradas comunes". El empresario ingresa el precio de cada tipo de entrada cuando usa el programa.

### Resolución - ejercicio 3
          
_Cómo analizar la consigna:_
Imaginemos que el empresario es nuestro cliente y nos encarga que le programemos una herramienta para calcular algunas cosas cada vez que organice un recital. Es decir, partimos de la base de que el programa se va a usar en varios casos distintos (para varios recitales), y por eso tiene que tener la posibilidad de que el usuario le vaya ingresando distintos datos cada vez que lo quiera usar.

Leyendo el enunciado vemos que los resultados que el cliente necesita que arroje el programa (para los cuales vamos a necesitar ciertos cálculos o procesamiento, que después vemos) son: "cuánta gente va a caber en el estadio para un recital determinado" y "cuánto dinero ingresaría si vende todas las entradas disponibles". </em><em><em>Algunos datos son "fijos" o "constantes": el usuario (el empresario) ya sabe que eso no cambia. Éstos son:

* Que por metro cuadrado de espacio disponible caben 4 personas.
* Que las tribunas ocupan 20% del espacio del estadio.
* Que el 30% del total de entradas que venda van a ser a precio "VIP" y el resto (70%) van a ser a precio "común".

También hay datos que van a ir cambiando con cada ejecución del programa (dependiendo del estadio que consiga el empresario y la banda que contrate para tocar):
* La cantidad de metros cuadrados que mide el estadio.
* El porcentaje de espacio que ocupa el escenario.
* La cantidad de gente que cabe en las tribunas.

Los datos que no tenemos y necesitamos que el usuario ingrese se tienen que pedir con cada ejecución del programa, mediante un input y guardándolos en variables de los tipos adecuados.

Ahora ya podemos empezar a calcular la primera incógnita: "cuánta gente va a caber en el estadio para un recital determinado". La segunda todavía no se puede resolver porque, para saber cuánto ganaría si vende todas las entradas, primero hay que saber cuántas entradas en total pueden venderse (esto es, cuánta gente en total cabe para un recital).

Así que, para saber cuánta gente cabe, hay que ver que, del espacio disponible que tenemos (los metros cuadrados totales del estadio), hay partes que no se pueden usar: un 20% que es donde van las tribunas y otro porcentaje que es donde va el escenario (que no lo sabemos pero lo va a decir el usuario cuando use el programa). Entonces, al espacio total disponible le restamos esos dos porcentajes, para saber cuántos metros cuadrados nos van quedando disponibles. Luego multiplicamos esos metros cuadrados que nos quedan x 4, porque en cada metro cuadrado entran 4 personas. Pero también sabemos que en las tribunas entra una cantidad de gente que el usuario va a ingresar al usar el programa (se guarda en una variable), así que sumamos esa cantidad (la variable). Con eso sabemos ya cuánta gente cabe y, por ende, cuántas entradas pueden venderse.

Puede ser útil graficar los datos que tenemos o que vamos a obtener del usuario para hacerse una mejor idea mental de cómo calcular:

![diagrama]({{ site.url }}/assets/2016-01-24-ejercicios-basicos-para-empezar-programar-img1.png)

Ya podemos calcular la segunda incógnita: "cuánto dinero ingresaría si vende todas las entradas disponibles", porque ya sabemos cuántas entradas tenemos disponibles y los precios los va a ingresar el usuario con la ejecución del programa.

Sabemos que, de esa cantidad total de entradas que pueden venderse, un 30% se cobra a un precio y el 70% restante se cobra a otro precio. Así que calculamos el 30% y el 70% del total de entradas que pueden venderse. Como los precios son ingresados por el usuario, seguramente necesitemos guardarlos en variables también. Luego podemos multiplicar cada precio por la cantidad que le corresponde de entradas y sumamos ambos resultados para saber cuál es el total de dinero que va a ingresar si se logran vender todas las entradas.


* **Python**

<pre><code>dimensiones=float(input("Dimensiones del estadio (en m2): "))
PORCENTAJETRIBUNAS=20
personasentribunas=int(input("Cantidad de personas que caben en las tribunas: "))
porcentajeescenario=int(input("Porcentaje de espacio que ocupa el escenario: "))
m2tribunas=dimensiones*(PORCENTAJETRIBUNAS/100)
m2escenario=dimensiones*(porcentajeescenario/100)
m2disponibles=dimensiones-m2tribunas-m2escenario
personastotales=(m2disponibles*4)+personasentribunas
print("Caben ", personastotales, " personas.")
precioentradavip=float(input("Precio de entradas VIP: "))
precioentradacomun=float(input("Precio de entradas comunes: "))
print("Ingresos totales: ", personastotales*0.3*precioentradavip + personastotales*0.7*precioentradacomun)</code></pre>

* **Java**

<pre><code>import java.util.Scanner;

public class prueba {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        double dimensiones;
        final double PORCENTAJETRIBUNAS = 20.0;
        int personasentribunas;
        double porcentajeescenario;
        System.out.print("Dimensiones del estadio (en m2): ");
        dimensiones = entrada.nextDouble();
        System.out.print("Cantidad de personas que caben en las tribunas: ");
        personasentribunas = entrada.nextInt();
        System.out.print("Porcentaje de espacio que ocupa el escenario: ");
        porcentajeescenario = entrada.nextDouble();
        double m2tribunas;
        double m2escenario;
        double m2disponibles;
        m2tribunas=dimensiones*(PORCENTAJETRIBUNAS/100);
        m2escenario=dimensiones*(porcentajeescenario/100);
        m2disponibles=dimensiones-m2tribunas-m2escenario;
        double personastotales;
        personastotales=(m2disponibles*4)+personasentribunas;
        System.out.println("Caben " + personastotales + " personas.");
        double precioentradavip;
        double precioentradacomun;
        System.out.print("Precio de entradas VIP: ");
        precioentradavip = entrada.nextDouble();
        System.out.print("Precio de entradas comunes: ");
        precioentradacomun = entrada.nextDouble();
        System.out.print("Ingresos totales: $");
        System.out.println(personastotales*0.3*precioentradavip + personastotales*0.7*precioentradacomun);
        entrada.close();
    }
}</code></pre>

* **C++**

<pre><code>#include &lt;iostream&gt;
using namespace std;
int main()
{
    double dimensiones;
    const double PORCENTAJETRIBUNAS = 20.0;
    int personasentribunas;
    double porcentajeescenario;
    cout &lt;&lt; "Dimensiones del estadio (en m2): ";
    cin &gt;&gt; dimensiones;
    cout &lt;&lt; "Cantidad de personas que caben en las tribunas: ";
    cin &gt;&gt; personasentribunas;
    cout &lt;&lt; "Porcentaje de espacio que ocupa el escenario: ";
    cin &gt;&gt; porcentajeescenario;
    double m2tribunas;
    double m2escenario;
    double m2disponibles;
    m2tribunas=dimensiones*(PORCENTAJETRIBUNAS/100);
    m2escenario=dimensiones*(porcentajeescenario/100);
    m2disponibles=dimensiones-m2tribunas-m2escenario;
    double personastotales;
    personastotales=(m2disponibles*4)+personasentribunas;
    cout &lt;&lt; "Caben " &lt;&lt; personastotales &lt;&lt; " personas.";
    double precioentradavip;
    double precioentradacomun;
    cout &lt;&lt; "Precio de entradas VIP: ";
    cin &gt;&gt; precioentradavip;
    cout &lt;&lt; "Precio de entradas comunes: ";
    cin &gt;&gt; precioentradacomun;
    cout &lt;&lt; "Ingresos totales: $" &lt;&lt; personastotales*0.3*precioentradavip + personastotales*0.7*precioentradacomun;
    return 0;
}</code></pre>
      
