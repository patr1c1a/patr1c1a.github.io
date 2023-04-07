---
layout: post
title: Ejercicio resuelto - Java
date: 2023-04-07 08:00:00 -0300
categories: java ejercicios
tags: poo
published: true
---

Un ejercicio simple con Java en el que debemos construir una clase que presente dos métodos constructores distintos.

![Ejercicio resuelto - Java]({{ site.url }}/assets/2023-04-07-ejercicio-poo-java.png)


&nbsp;

{% include accesibilidad.html %}

Ejercicio resuelto - Java (programación orientada a objetos)

Escribir un programa que permita obtener el área y el perímetro de un triángulo, usando una clase "Triangulo". Si no se indican valores, por defecto, los lados del triángulo serán de 2, 3 y 4.

Resolución:

```java
class Triangulo {
    private int ladoA, ladoB, ladoC;
     
    public Triangulo() {
        ladoA=2; ladoB=3; ladoC=4;
    }
    public Triangulo(int a, int b, int c) {
        ladoA=a; ladoB=b; ladoC=c;
    }
    int area() {
        return ladoA*ladoB*ladoC;
    }
    int perimetro() {
        return ladoA+ladoB+ladoC;
    }

    void setLadoA(int a) { ladoA=a; }
    void setLadoB(int b) { ladoB=b; }
    void setLadoC(int c) { ladoC=c; }
    int getLadoA() { return ladoA; }
    int getLadoB() { return ladoB; }
    int getLadoC() { return ladoC; }
}

public class Prueba {
    public static void main(String[] args) {
        Triangulo t1=new Triangulo();
        Triangulo t2=new Triangulo(5,6,7);
        System.out.println(t1.area());
        System.out.println(t2.area());
        System.out.println(t1.perimetro());
        System.out.println(t2.perimetro());
        t1.setLadoA(6);
        System.out.println(t1.area());
        System.out.println(t1.perimetro());
    }
} 
```

</div></details>

<br />
💻 [Código ejecutable](https://jdoodle.com/a/66HL){:target="_blank"}

{% include codeEditor.html id="66HL?stdin=0&arg=0&rw=1" %} 
<br />

<hr />
