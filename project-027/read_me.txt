Proyecto 26: 
En este ejercicio se aprendió acerca de los "decoradores". En Python, los decoradores son una forma poderosa y elegante de modificar el comportamiento de una función o método. Un decorador es esencialmente una función que toma otra función como argumento y extiende o altera su comportamiento sin modificarla directamente.

Un decorador se aplica a una función usando el símbolo @ seguido del nombre del decorador antes de la definición de la función.

Un decorador muy utilizado al trabajar en el paradigma orientado a objetos es el decorador @property que se utiliza para definir propiedades en una clase. Este decorador le permite a los métodos comportarse como atributos, lo que facilita la encapsulación y el control sobre cómo se acceden y modifican los datos.

Este ejercicio es el mismo que el proyecto anterior (proyect-026) solo que se agregó el decorador @property. Antes podiamos acceder y modificar a los atributos de nuestro objeto User1 mediante los getters y setters los cuales actúan como métodos. Ahora dejamos de lado los getters y utilizamos el decorador para que el método pase a comportarse como atributo. 


Project 26: 
In this exercise, we learned about "decorators." In Python, decorators are a powerful and elegant way to modify the behavior of a function or method. A decorator is essentially a function that takes another function as an argument and extends or alters its behavior without modifying it directly.

A decorator is applied to a function using the `@` symbol followed by the name of the decorator before the function definition.

A commonly used decorator when working in the object-oriented paradigm is the `@property` decorator, which is used to define properties in a class. This decorator allows methods to behave like attributes, facilitating encapsulation and control over how data is accessed and modified.

This exercise is the same as the previous project (project-026) except that the `@property` decorator has been added. Previously, we could access and modify the attributes of our `User1` object through getters and setters, which act as methods. Now, we use the decorator so that the method behaves like an attribute.