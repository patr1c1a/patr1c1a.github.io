---
layout: post
title: Fundamentos de programación orientada a objetos (POO)
date: 2025-04-27 09:00:00 -0300
categories: poo conceptos
tags: herencia encapsulamiento ocultamiento abstracción polimorfismo
published: true
---

Programar con objetos no suele parecernos simple al principio, pero siguiendo estas reglas básicas podemos escribir código limpio, reusable y fácil de modificar.

![Fundamentos de POO 1]({{ site.url }}/assets/2025-05-01-fundamentos-poo-img1.png)

![Fundamentos de POO 2]({{ site.url }}/assets/2025-05-01-fundamentos-poo-img2.png)

![Fundamentos de POO 3]({{ site.url }}/assets/2025-05-01-fundamentos-poo-img3.png)

![Fundamentos de POO 4]({{ site.url }}/assets/2025-05-01-fundamentos-poo-img4.png)



&nbsp;

{% include accesibilidad.html %}

Fundamentos de POO

Resumen:

- HERENCIA: Una subclase adquiere los atributos y métodos de la superclase.

- ENCAPSULAMIENTO: Agrupar lo que funciona como una unidad.

- OCULTAMIENTO: Solo se debe exponer lo necesario.

- ABSTRACCIÓN: Enfocarse en qué hace un componente (no en cómo lo hace).

- POLIMORFISMO: Mismo método/clase: diferente comportamiento según contexto.

En detalle:

Herencia:

Una clase padre ("clase base" o "superclase") sirve como "molde" de una clase hija ("subclase"). La clase padre es más general y la hija es más específica, "heredando" todos los atributos y métodos de su padre. También puede tener otros, propios. Puede decirse que [clase hija] "es un" [clase padre]. 

Ejemplo: Smartphone "es un" Dispositivo.

```java
public class Dispositivo {
    public void encender() {
        // lógica para encender
    }
}

public class Smartphone extends Dispositivo {
    public void llamar() {
        // lógica para llamar
    }
}
```

Encapsulamiento:

Diseñar cada clase como una unidad lógica coherente, que agrupa sus propios datos y responsabilidades sin hacer lo que no le corresponde, reduce la dependencia entre clases (logrando un bajo acoplamiento). 
Ejemplo: una clase que gestiona usuarios de un sistema puede ser responsable de administrarlos, pero no debería encargarse de enviarles emails de bienvenida o despedida; eso le corresponde a una clase específica.

Clase "GestorDeUsuarios" con un atributo privado llamado "listaDeUsuarios" y dos métodos públicos: agregar(usuario), eliminar(usuario). Clase Notificador con un método público enviarEmail(destino, asunto, cuerpo).

Ocultamiento:

Impide que otras clases accedan a atributos o métodos propios de una clase determinada (evitando modificaciones indebidas y escondiendo detalles de implementación). 

Ejemplo: un método público para guardar datos de una persona, que llama a un método privado (oculto) para verificar si el email es válido.

```java
public class Usuario {  
    public void guardarDatos(String email, long dni) {  
        if (esValido(email)) { 
            // implementación
        }
    }

    private boolean esValido(String email) {
        // método solo accesible a esta clase
    } 
}  
```

Abstracción:

Simplificar el uso de sistemas complejos, separando responsabilidades en capas, de modo que cada capa exponga solo lo necesario para quien la usa. 

Ejemplo: la clase ControladorClima puede encargarse de mostrar el clima, mientras que otra clase se comunica con un servicio externo del clima (y hasta podría cambiar la implementación, sin que esto afecte al controlador).

Una clase "ControladorClima" con un atributo privado llamado "servicio" de tipo "ServicioAPIClima" y un método público llamado "mostrarClima(ciudad: str)". Una clase "ServicioAPIClima" con un método público "obtenerClima(ciudad: str)".

Polimorfismo:

Permite que un objeto se comporte como instancia de su propia clase o de su clase padre. Un objeto puede: reemplazar métodos heredados (sobreescritura), tener múltiples versiones de un método (sobrecarga), ser tratado como su clase padre (subtipado).

Ejemplo: la clase Animal puede tener un método comer() y otro comer(comida) donde ambos tienen el mismo nombre pero distinta "firma". Además, la clase Gato puede ser subclase de Animal e implementar el método comer() de una forma específica. También, un objeto de tipo Gato puede ser usado donde se espera uno de tipo Animal.

```java
public class Animal {
    public void comer() {
        // implementación
    }
    public void comer(String comida) {
        // sobrecarga del método comer
    }
}

public class Gato extends Animal {
    @Override public void comer() {
        // sobreescritura del método comer
    }
}

Animal pelusa = new Gato();  // subtipado
pelusa.comer();
pelusa.comer("pescado");
```


</div></details>
<br />&nbsp;
<hr />
