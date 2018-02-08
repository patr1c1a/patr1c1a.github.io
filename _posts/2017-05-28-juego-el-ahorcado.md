---
layout: post
title: Juego en terminal - El Ahorcado
date: 2017-05-28 19:12:00
categories: c++
tags: paradigma_imperativo juegos proyectos
published: true
---

# Desafío

El desafío consiste en programar un juego en terminal de texto, utilizando C++. La idea es practicar lógica y algoritmia utilizando structs, vectores y conjuntos.

Primero necesitarás [descargar el archivo](/assets/2017-05-28-juego-el-ahorcado-proyecto.zip). Este archivo contiene tres cosas:
* el desafío, que es un archivo .cpp para completar. En él verás la estructura del programa ya planteada y algunas indicaciones para que escribas tu código. Este código es el que deberás usar en tu proyecto como punto de partida.
* el ejecutable para que veas cómo debería funcionar el programa cuando completes el desafío (contiene 2 archivos: un exe y un txt que el programa necesita para funcionar; sólo deberás descomprimirlos en una misma carpeta y ejecutar el exe).
* el código fuente completo del ejecutable (¡no vale "espiarlo" antes de intentar el desafío!).

[Descargá el archivo](/assets/2017-05-28-juego-el-ahorcado-proyecto.zip).


## El juego

El juego del ahorcado consiste en tomar una palabra al azar y darle al usuario la posibilidad de que adivine letras hasta completar la palabra. Tiene 6 intentos para arriesgar letras. Por cada letra incorrecta, se resta un intento. Cuando se queda sin intentos, pierde. Si adivina todas las letras, gana. También, en cualquier momento del juego, puede arriesgar la palabra completa y, si la acierta, el juego finaliza y el usuario gana; pero si la palabra es incorrecta el juego finaliza y el usuario pierde.


## Características del programa

Según el nivel elegido por el usuario se le brindará determinada ayuda:
* Nivel 1: palabras de hasta 7 letras (inclusive).
* Nivel 2: palabras de 8 a 11 letras (inclusive).
* Nivel 3: palabras de más de 11 letras.

Las palabras se encuentran en un archivo de texto que se leerá al inicio. El archivo de texto se encuentra en el mismo directorio que el archivo ejecutable del juego.

Una vez elegido el nivel y al comenzar el juego, se cargarán las palabras disponibles y se seleccionará una al azar. 

El usuario cuenta con 6 intentos para arriesgar letras, o puede arriesgar la palabra completa en cualquier momento.

Comienza mostrándose un "dibujo" de la horca vacía y tantos guiones como letras haya. 

Se le brindará al usuario la opción de arriesgar una letra o la palabra entera. Si arriesga una letra que ya había arriesgado anteriormente, ese intento no cuenta y se le vuelve a pedir una letra. Cuando el usuario ingresa su opción, si la letra existe en la palabra, se muestra en el lugar correspondiente y se contabiliza como letra ya utilizada. Si la letra no existe en la palabra, se modifica el dibujo de la horca para sumar una parte del ahorcado y se resta un intento, pero también se cuenta a la letra como ya utilizada. Si la letra no existe en la palabra y, además, al ahorcado le quedaba una sola parte por completar, se completa y el juego termina.

Siempre se muestra un dibujo del estado del juego al inicio, luego de cada intento y al finalizar.

No se distinguen mayúsculas o minúsculas (todas son convertidas a una forma estándar). No se aceptan vocales acentuadas o con diéresis.

El juego termina cuando:
* No quedan más intentos (pierde).
* El usuario acierta todas las letras, una a una (gana).
* El usuario arriesga una palabra (gana si acierta, pierde si no).


## Ejecución

Para ejecutar el juego se debe iniciar el programa ahorcado.exe, siempre teniendo el archivo palabras.txt en el mismo directorio que ahorcado.exe. El ejecutable fue generado bajo el estándar C++11, utilizando el IDE [Qt Creator](www.qt.io/download-open-source).


## Código

El código que se provee para completar tiene varias partes ya resueltas y otras son funciones que se deben implementar. Cada una tiene su documentación, la cual debe respetarse.

### Archivos de cabecera incluidos

<pre><code>#include &lt;iostream>
#include &lt;set>
#include &lt;vector>
#include &lt;fstream>
#include &lt;string>
#include &lt;ctime>
#include &lt;cstdlib>
#include &lt;climits></code></pre>


### Constantes y objetos utilizados

<pre><code>const int GANADOR=7;
const int PERDEDOR=0;
const string ARCHIVO_PALABRAS="palabras.txt";

struct Palabras{
    vector&lt;string> nivel1;
    vector&lt;string> nivel2;
    vector&lt;string> nivel3;
};

struct Jugada{
    unsigned int nivel;
    unsigned int intentos=6;
    string palabra;
    set&lt;char> letrasAdivinadas;
    bool ganador=false;
    string palabraArriesgada;
    char ultimaLetraArriesgada;
};</code></pre>


### Funciones incluidas

<pre><code>/*
FUNCIÓN: existeArchivo
PROPÓSITO: Determina si el archivo cuyo nombre se pasa por parámetro está vacío.
PARÁMETROS:
    string: nombre del archivo a evaluar.
RETORNO: true si el archivo existe, false en caso contrario.
*/
bool existeArchivo(string archivo){
    ifstream infile(archivo);
    return infile.good();
}


/*
FUNCIÓN: cargarPalabras
PROPÓSITO: Lee del archivo cada palabra almacenada y la guarda en un contenedor en memoria de acuerdo a su cantidad de letras.
Para el nivel 1 las palabras tienen hasta 7 letras inclusive.
Para el nivel 2 las palabras tienen entre 7 y 11 letras inclusive.
Para el nivel 3 las palabras tienen más de 11 letras.
RETORNO: objeto Palabras con vectores de palabras de acuerdo al nivel si el archivo de palabras existe
(si algún archivo no existe, el vector queda vacío).
*/
Palabras cargarPalabras(){
    vector&lt;string> palabrasNivel1, palabrasNivel2, palabrasNivel3;
    string palabra;
    if (existeArchivo(ARCHIVO_PALABRAS)) {
        ifstream archivo(ARCHIVO_PALABRAS);
        if (archivo.is_open()) {
            while (getline(archivo, palabra)) {
                if (palabra.length()&lt;=7)
                    palabrasNivel1.push_back(palabra);
                else
                    if ((palabra.length()>7) && (palabra.length()&lt;=11))
                        palabrasNivel2.push_back(palabra);
                    else
                        palabrasNivel3.push_back(palabra);
            }
            archivo.close();
        }
    }
    Palabras palabras;
    palabras.nivel1=palabrasNivel1;
    palabras.nivel2=palabrasNivel2;
    palabras.nivel3=palabrasNivel3;
    return palabras;
}


/*
FUNCIÓN: seleccionarPalabra
PROPÓSITO: Selecciona de manera aleatoria un elemento de un vector de strings y lo retorna.
PARÁMETROS:
    vector&lt;string> : vector con palabras.
RETORNO: Palabra seleccionada al azar.
*/
string seleccionarPalabra(vector&lt;string> palabras){
    srand(time(NULL));
    int indice = rand() % palabras.size();
    return palabras[indice];
}


/*
FUNCIÓN: mostrarDibujo
PROPÓSITO: Mostrar el dibujo en el estado actual.
PARÁMETROS:
    int : cantidad de intentos restantes
*/
void mostrarDibujo(int intentos){
    switch (intentos){
    case 6:
        cout &lt;&lt; "__________\n|         |\n|\n|\n|\n|\n|";
        break;
    case 5:
        cout &lt;&lt; "__________\n|         |\n|         0\n|\n|\n|\n|";
        break;
    case 4:
        cout &lt;&lt; "__________\n|         |\n|         0\n|         |\n|\n|\n|";
        break;
    case 3:
        cout &lt;&lt; "__________\n|         |\n|         0\n|        /|\n|\n|\n|";
        break;
    case 2:
        cout &lt;&lt; "__________\n|         |\n|         0\n|        /|\\\n|\n|\n|";
        break;
    case 1:
        cout &lt;&lt; "__________\n|         |\n|         0\n|        /|\\\n|        /\n|\n|";
        break;
    case PERDEDOR:
        cout &lt;&lt; " _________\n|         |\n|         0\n|        /|\\\n|        / \\\n|\n|\n";
        break;
    case GANADOR:
        cout &lt;&lt; "__________\n|         |\n|         \n|        \n|      0\n|     \\|/\n|     / \\\n";
        break;
    }
    cout &lt;&lt; endl;
}

int main(){
    Palabras palabras=cargarPalabras();
    int nivel;
    bool errorDeTipoIngresado;
    set&lt;int> opcionesValidas{0,1,2,3};

    std::cout &lt;&lt; R"(
                 8888888888 888
                 888        888                     __________
                 888        888                    |         |
                 8888888    888                    |         0
                 888        888                    |        /|\
                 888        888                    |        / \
                 888        888                    |
                 8888888888 888                    |



                          888                                             888
                          888                                             888
                          888                                             888
                  8888b.  88888b.   .d88b.  888d888 .d8888b  8888b.   .d88888  .d88b.
                     "88b 888 "88b d88""88b 888P"  d88P"        "88b d88" 888 d88""88b
                 .d888888 888  888 888  888 888    888      .d888888 888  888 888  888
                 888  888 888  888 Y88..88P 888    Y88b.    888  888 Y88b 888 Y88..88P
                 "Y888888 888  888  "Y88P"  888     "Y8888P" Y888888  "Y88888  "Y88P"
    )" &lt;&lt; '\n';

    do{
        cout &lt;&lt; "\n\tSeleccionar Nivel:" &lt;&lt; endl;
        cout &lt;&lt; "\t\t1: Facil" &lt;&lt; endl;
        cout &lt;&lt; "\t\t2: Medio" &lt;&lt; endl;
        cout &lt;&lt; "\t\t3: Dificil" &lt;&lt; endl;
        cout &lt;&lt; "\t0: Salir\n" &lt;&lt; endl;

        cout &lt;&lt; "--Opcion seleccionada: ";
        cin >> nivel;
        errorDeTipoIngresado = cin.fail();
        cin.clear();
        cin.ignore(INT_MAX, '\n');

        if (opcionesValidas.find(nivel) != opcionesValidas.end()){
            switch (nivel){
            case 0:
                break;
            case 1:
                if (palabras.nivel1.empty()){
                    cout &lt;&lt; "\tERROR: No hay palabras para ese nivel." &lt;&lt; endl;
                }
                else{
                    controlarJuego(nivel, palabras.nivel1);
                }
                break;
            case 2:
                if (palabras.nivel2.empty()){
                    cout &lt;&lt; "\tERROR: No hay palabras para ese nivel." &lt;&lt; endl;
                }
                else{
                    controlarJuego(nivel, palabras.nivel2);
                }
                break;
            case 3:
                if (palabras.nivel3.empty()){
                    cout &lt;&lt; "\tERROR: No hay palabras para ese nivel." &lt;&lt; endl;
                }
                else{
                    controlarJuego(nivel, palabras.nivel3);
                }
                break;
            }
        }
    } while (errorDeTipoIngresado || (opcionesValidas.find(nivel) == opcionesValidas.end()) || nivel!=0);

    return 0;
}</code></pre>


### Funciones a desarrollar

<pre>FUNCIÓN: mostrarJuego
PROPÓSITO: Mostrar el juego en el estado actual. Por cada letra adivinada, si la letra existe en la palabra se muestra en el lugar correspondiente, en caso contrario, se muestra un guión bajo " _ ".
PARÁMETROS:
    string : palabra en juego.
    set&lt;char> : letras ya adivinadas por el usuario.</pre>


<pre>FUNCIÓN: trim
PROPÓSITO: Eliminar espacios delante y detrás de una cadena de caracteres.
PARÁMETROS:
    string : cadena a modificar
RETORNO: cadena modificada (sin los espacios sobrantes).</pre>


<pre>FUNCIÓN: mayusculas
PROPÓSITO: Retornar un string con todas sus letras en mayúscula.
PARÁMETROS:
    string : cadena de caracteres a convertir a mayúscula.
RETORNO: string con la cadena convertida.</pre>


<pre>FUNCIÓN: todasLasLetrasAdivinadas
PROPÓSITO: Verificar si el usuario ya adivinó todas las letras de la palabra.
PARÁMETROS:
    set&lt;char> : letras ya arriesgadas.
    set&lt;char> : letras en la palabra.
RETORNO: true si todas las letras de la palabra fueron adivinadas, false en caso contrario.</pre>


<pre>FUNCIÓN: letraEnPalabra
PROPÓSITO: Verificar si la letra arriesgada por el usuario está en la palabra o no
PARÁMETROS:
    string : palabra a adivinar en la jugada actual.
    char : letra arriesgada por el usuario.
RETORNO: true si la letra estaba en la palabra, false en caso contrario.</pre>


<pre>FUNCIÓN: verificarEstado
PROPÓSITO: Verifica el estado del juego (si el jugador ganó o no).
Si aún quedan intentos (intentos!=PERDEDOR), se verifica si el jugador arriesgó una palabra y, de ser así, se verifica si coincide con la palabra en juego. En ese caso, el campo ganador se pone en true. Si no acertó la palabra, el campo intentos se pone en 0 (utilizando la constante PERDEDOR).
Si no arriesgó una palabra, se verifica si la letra arriesgada está en la palabra y, de no ser así, se decrementa el campo intentos.
Si la letra arriesgada está en la palabra, se verifica si ya acertó todas las letras de la palabra en juego. En caso de ser así, el campo ganador se pone en true.
PARÁMETROS:
    Jugada : datos de la jugada actual.
RETORNO: Jugada actual.</pre>


<pre>FUNCIÓN: arriesgarPalabra
PROPÓSITO: Ofrecer al usuario la posibilidad de "adivinar" la palabra, impidiendo incluir números en la palabra arriesgada.
RETORNO: palabra arriesgada por el usuario.</pre>


<pre>FUNCIÓN: arriesgarLetra
PROPÓSITO: Ofrecer al usuario la posibilidad de "adivinar" una letra.
Si la letra ya había sido usada previamente (esté o no en la palabra) se imprime un mensaje y se pide otra.
Se valida que el dato ingresado sea una letra y no otro tipo de carácter.
PARÁMETROS:
    const set&lt;char>* : puntero al conjunto de letras ya arriesgadas.
RETORNO: letra elegida por el usuario.</pre>


<pre>FUNCIÓN: arriesgar
PROPÓSITO: Ofrecer al usuario la posibilidad de "adivinar" una letra o la palabra entera, mostrándole un menú que le permita elegir (se valida el ingreso de un dato válido).
Si elige arriesgar una letra, se llama a la función correspondiente y la letra se guarda en el campo ultimaLetraArriesgada, además de agregarse al campo letrasAdivinadas.
Si elige arriesgar una palabra, se llama a la función correspondiente y la palabra se guarda en el campo palabraArriesgada.
PARÁMETROS:
    Jugada : datos de la jugada actual.
RETORNO: Jugada actual.</pre>


<pre>FUNCIÓN: controlarJuego
PROPÓSITO: Inicializa el juego de acuerdo al nivel seleccionado por el usuario, almacenando en el campo palabra una palabra al azar, en mayúsculas.
Luego controla el orden del desarrollo del juego (una jugada continúa mientras el jugador tenga intentos restantes y el campo "ganador" esté en falso).
Mientras la jugada continúa, se muestra la cantidad de intentos restantes, el dibujo de la horca en el estado actual, la palabra a adivinar (con guiones en las letras no adivinadas). Luego se da la opción de arriesgar una letra o la palabra entera. Si la cantidad de intentos se redujo (porque no acertó la letra), se muestra un mensaje que lo indique. Si la letra arriesgada era correcta, se muestra un mensaje que lo indique. Una vez finalizada la jugada, si el campo ganador está en true significa que acertó todas las letras o que arriesgó una palabra y acertó, y se muestra el dibujo correspondiente al estado GANADOR y un mensaje, y el juego termina. Si la jugada finalizó con el campo ganador en falso, se muestra el dibujo correspondiente al estado PERDEDOR y un mensaje, y el juego termina.
PARÁMETROS:
    int : nivel del juego.
    vector&lt;string> : palabras del nivel seleccionado</pre>


## Mejoras posibles

El desafío terminado logra un juego un poco sencillo, al que pueden agregársele varias mejoras. ¿Te animás a investigarlo e implementarlas por tu cuenta?

* Una vez utilizada una palabra en una jugada, evitar que vuelva a utilizarse hasta que el programa se cierre.
* Soporte de caracteres no ascii estándar (letra ‘ñ’ y vocales acentuadas o con diéresis)
* Guardar puntajes del jugador (por ejemplo, la cantidad de intentos restantes es el puntaje obtenido en una jugada) y acumularlos, o formar un “ranking” de puntajes.
* Tomar las palabras de alguna fuente confiable (por ejemplo, un diccionario online), en vez de un archivo de texto local.
