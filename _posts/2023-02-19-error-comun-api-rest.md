---
layout: post
title: Un error común al crear una API REST
date: 2023-02-19 20:00:00 -0300
categories: otros
tags: api rest backend flask python
published: true
---

Este es uno de esos errores que, al principio, pueden ser difíciles de detectar porque todo funciona como esperamos y no hay fallas en la lógica. Pero, si queremos que nuestra API siga el estilo arquitectónico REST, debemos respetar ciertos principios.

El ejemplo está escrito con el microframework Flask para Python, pero es válido para cualquier lenguaje, ya que el problema está en qué endpoints definimos.

Para refrescar algunos conceptos sobre APIs:

* [Conceptos básicos sobre APIs]({% post_url 2021-01-28-apis %})

* [APIs REST vs. SOAP]({% post_url 2021-12-30-api-rest-soap %})

* [Los 5 "verbos" HTTP más usados]({% post_url 2021-02-24-verbos-http %})

* [URI, URN, URL. ¿Qué son?]({% post_url 2022-08-16-uri-url-urn %})
 

![UN ERROR COMÚN AL CREAR UNA API REST]({{ site.url }}/assets/2023-02-19-error-comun-api-rest.png)


&nbsp;

{% include accesibilidad.html %}

UN ERROR COMÚN AL CREAR UNA API REST

Para que nuestra API sea RESTful debe cumplir con varios principios. Entre ellos, el de presentar a la información como una colección de "recursos", cada uno identificado por una dirección ("URI"). Para esto utilizamos endpoints que permiten acceder y operar con esos recursos mediante verbos HTTP (get, post, delete, put, patch…).

Ejemplo de dos versiones de una API en Flask. Una de ellas, aunque funcional, no es REST (@app.route indica la URL de acceso al endpoint):

Versión 1:

```python
from flask import Flask
 
app = Flask(__name__)

@app.route("/agregar/", methods=["POST"])
def agregar_producto():
    # Código para agregar producto

@app.route("/listar/", methods=["GET"])
def listar_productos():
    # Código para listar productos

@app.route("/eliminar/", methods=["DELETE"])
def eliminar_producto():
    # Código para eliminar producto

@app.route("/modificar/", methods=["PUT"])
def modificar_producto():
    # Código para modificar producto
 
if __name__ == '__main__':
    app.run()
```

Versión 2:

```python
from flask import Flask
 
app = Flask(__name__)

@app.route("/producto/", methods=["POST"])
def agregar_producto():
    # Código para agregar producto

@app.route("/producto/", methods=["GET"])
def listar_productos():
    # Código para listar productos

@app.route("/producto/", methods=["DELETE"])
def eliminar_producto():
    # Código para eliminar producto

@app.route("/producto/", methods=["PUT"])
def modificar_producto():
    # Código para modificar producto
 
if __name__ == '__main__':
    app.run()
```

La versión 1 no sigue el estilo REST, pues usa una URL diferente para cada operación (agregar, listar, eliminar, modificar). En la opción 2 existe un único endpoint que representa al recurso "producto" y las operaciones se distinguen mediante el verbo HTTP apropiado para cada una.

</div></details>



<hr />
