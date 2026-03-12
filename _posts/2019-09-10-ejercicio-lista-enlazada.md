---
layout: post
title: Ejercicio resuelto - lista enlazada
date: 2019-09-10 21:00:00
categories: ejercicios c++ python
tags: listas nodos
published: true
---

Problema con listas enlazadas y 2 algoritmos diferentes para resolverlo.

💻 [Implementación de las soluciones en C++, para seguir el código paso a paso](https://pythontutor.com/visualize.html#code=%23include%20%3Ciostream%3E%0A%23include%20%3Cvector%3E%0Ausing%20namespace%20std%3B%0A%0Astruct%20Nodo%7B%0A%20%20%20%20int%20dato%3B%0A%20%20%20%20Nodo*%20siguiente%3B%0A%7D%3B%0A%0A//Inserta%20elemento%20al%20principio%20de%20la%20lista%0Avoid%20insertarNumero%28Nodo*%20%26inicio,%20int%20n%29%7B%0A%20%20%20%20Nodo*%20nuevo%3Dnew%20Nodo%3B%0A%20%20%20%20nuevo-%3Edato%3Dn%3B%0A%20%20%20%20nuevo-%3Esiguiente%3Dinicio%3B%0A%20%20%20%20inicio%3Dnuevo%3B%0A%7D%0A%0A//Imprime%20la%20lista%20pasada%20por%20par%C3%A1metro%0Avoid%20imprimirLista%28Nodo*%20inicio%29%7B%0A%20%20%20%20for%20%28%3B%20inicio!%3Dnullptr%3B%20inicio%3Dinicio-%3Esiguiente%29%7B%0A%20%20%20%20%20%20%20%20cout%20%3C%3C%20inicio-%3Edato%20%3C%3C%20%22%20-%20%22%3B%0A%20%20%20%20%7D%0A%7D%0A%0A//Retorna%20el%20nodo%20del%20medio%20%28el%20segundo,%20si%20hay%20dos%20nodos%20medios%29%0ANodo*%20nodoMedio_alternativa1%28Nodo*%20inicio%29%20%7B%0A%20%20%20%20vector%3CNodo*%3E%20A%20%3D%20%7Binicio%7D%3B%0A%20%20%20%20while%20%28A.back%28%29-%3Esiguiente%20!%3D%20nullptr%29%0A%20%20%20%20%20%20%20%20A.push_back%28A.back%28%29-%3Esiguiente%29%3B%0A%20%20%20%20return%20A%5BA.size%28%29%20/%202%5D%3B%0A%7D%0A%0A//Retorna%20el%20nodo%20del%20medio%20%28el%20segundo,%20si%20hay%20dos%20nodos%20medios%29%0ANodo*%20nodoMedio_alternativa2%28Nodo*%20inicio%29%20%7B%0A%20%20%20%20Nodo*%20lento%20%3D%20inicio%3B%0A%20%20%20%20Nodo*%20rapido%20%3D%20inicio%3B%0A%20%20%20%20while%20%28rapido!%3Dnullptr%20%26%26%20rapido-%3Esiguiente!%3Dnullptr%29%7B%0A%20%20%20%20%20%20%20%20lento%20%3D%20lento-%3Esiguiente%3B%0A%20%20%20%20%20%20%20%20rapido%20%3D%20rapido-%3Esiguiente-%3Esiguiente%3B%0A%20%20%20%20%7D%0A%20%20%20%20return%20lento%3B%0A%7D%0A%0A%0Aint%20main%28%29%7B%0A%20%20%20%20Nodo*%20lista%3Dnullptr%3B%0A%20%20%20%20insertarNumero%28lista,%206%29%3B%0A%20%20%20%20insertarNumero%28lista,%205%29%3B%0A%20%20%20%20insertarNumero%28lista,%204%29%3B%0A%20%20%20%20insertarNumero%28lista,%203%29%3B%0A%20%20%20%20insertarNumero%28lista,%202%29%3B%0A%20%20%20%20insertarNumero%28lista,%201%29%3B%0A%20%20%20%20%0A%20%20%20%20//Invocar%20nodoMedio_alternativa1%20%C3%B3%20nodoMedio_alternativa2%20para%20usar%20la%20funci%C3%B3n%20deseada%0A%20%20%20%20cout%20%3C%3C%20%22Elemento%20en%20el%20nodo%20medio%3A%20%22%20%3C%3C%20nodoMedio_alternativa1%28lista%29-%3Edato%20%3C%3C%20endl%3B%0A%20%20%20%20return%200%3B%0A%7D&cumulative=false&curInstr=63&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=cpp_g%2B%2B9.3.0&rawInputLstJSON=%5B%5D&textReferences=false){:target="_blank"}

Fuente: [leetcode](https://leetcode.com/problems/middle-of-the-linked-list/description/){:target="_blank"}

▶️ [Videos: listas enlazadas en C++](https://www.youtube.com/playlist?list=PLb_E6BNMg5j4PxrjKC7Nzjhy3ZV3xdiDB){:target="_blank"}

<br />![Enunciado]({{ site.url }}/assets/2019-09-10-ejercicio-lista-enlazada-01.png)
<br />
<br />![Código 1]({{ site.url }}/assets/2019-09-10-ejercicio-lista-enlazada-02.png)
<br />
<br />![Código 2]({{ site.url }}/assets/2019-09-10-ejercicio-lista-enlazada-03.png)
