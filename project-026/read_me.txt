Proyecto 26
En este ejercicio se implementó el encapsulamiento y se hizo uso de getters y setters. El encapsulamiento es otro de los pilares del paradigma orientado a objetos y se refiere a la capacidad de restringir el acceso a determinados métodos y atributos de los objetos, estableciendo así qué puede utilizarse desde fuera de la clase. Existen tres tipos de encapsulamiento:

  - Público: los atributos y métodos pueden ser accedidos desde cualquier parte del programa.
  - Protegido: los atributos y métodos pueden ser accedidos solo por la misma clase y sus subclases.
  - Privado: los atributos y métodos pueden ser accedidos solo por la misma clase.

En Python, no existen modificadores de acceso como en otros lenguajes de programación. En su lugar, el acceso a una variable o función se determina por su nombre, siguiendo convenciones entre programadores. Estas son las convenciones utilizadas:

  - Público: los atributos o métodos sin guiones bajos en el nombre son públicos.
  - Protegido: los atributos o métodos precedidos por un guión bajo (_) son protegidos.
  - Privado: los atributos o métodos precedidos por dos guiones bajos (__) son privados.

Para los primeros dos casos (público y protegido), Python trata los atributos y métodos como públicos debido a que es una convención. Sin embargo, en el caso de los atributos o métodos privados, Python emplea name mangling para dificultar el acceso a ellos desde fuera de la clase.

Para acceder a los atributos privados, se utilizan los "getters" y "setters", también conocidos como funciones miembros, que permiten acceder y modificar las propiedades privadas.

Project 26
In this exercise, encapsulation was implemented, and getters and setters were used. Encapsulation is another pillar of the object-oriented paradigm and refers to the ability to restrict access to certain methods and attributes of objects, thereby defining what can be used from outside the class. There are three types of encapsulation:

  - Public: attributes and methods can be accessed from anywhere in the program.
  - Protected: attributes and methods can be accessed only by the same class and its subclasses.
  - Private: attributes and methods can be accessed only by the same class.

In Python, there are no access modifiers as in other programming languages. Instead, access to a variable or function is determined by its name, following conventions among programmers. These are the conventions used:

  - Public: attributes or methods without underscores in their names are public.
  - Protected: attributes or methods preceded by a single underscore (_) are protected.
  - Private: attributes or methods preceded by double underscores (__) are private.

For the first two cases (public and protected), Python treats attributes and methods as public because it is a convention. However, in the case of private attributes or methods, Python uses name mangling to make accessing them from outside the class more difficult.

To access private attributes, "getters" and "setters" are used, also known as member functions, which allow accessing and modifying private properties.