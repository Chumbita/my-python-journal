Proyecto 24: 
La herencia múltiple en Python permite que una clase herede atributos y métodos de más de una clase base. Esto significa que una clase derivada puede tener más de una superclase. Una vez que se definieron las superclases, se define la clase derivada en donde se debe listar entre paréntesis los nombres de las clases de las cuales hereda. 
En el constructor de la clase derivada, se debe llamar a los constructores de las superclases. Esto se puede hacer utilizando el nombre de las propias clases en lugar de super(). Por ejemplo:

def __init__.(self, ...):
  SuperClase1.__init__(self, ...)
  SuperClase2.__init__(self, ...)

Para los métodos de la clase derivada que son heredados de las superclases y cuya implementación no se modificará, se recomienda referenciar a ellos usando super() para mantener la claridad y coherencia del código. Esto facilita la llamada a métodos en la jerarquía de herencia, especialmente cuando se utiliza herencia múltiple. Por ejemplo:

def metodo_heredado(self, ...):
    super().metodo_heredado(...)

En la herencia múltiple, pueden surgir dificultades cuando dos superclases tienen una propiedad o método con el mismo nombre. La pregunta es, al llamar a ese método en una instancia de la clase derivada, ¿cuál de los métodos de las dos superclases se ejecutará? Para solucionar este problema, Python utiliza el Orden de Resolución de Métodos (MRO, por sus siglas en inglés), que determina el orden de búsqueda de métodos y atributos en una jerarquía de clases con herencia múltiple. Puedes ver el MRO de una clase usando el atributo __mro__ o la función mro().

Project 24: 
Multiple inheritance in Python allows a class to inherit attributes and methods from more than one base class. This means a derived class can have more than one superclass. Once the superclasses are defined, the derived class is defined by listing the names of the superclasses in parentheses.

In the constructor of the derived class, you should call the constructors of the superclasses directly, rather than using super(). For example:

def __init__(self, ...):
    SuperClass1.__init__(self, ...)
    SuperClass2.__init__(self, ...)

For methods in the derived class that are inherited from the superclasses and whose implementation will not be modified, it is recommended to reference them using super() to maintain code clarity and consistency. This facilitates method calls in the inheritance hierarchy, especially with multiple inheritance. For example:

def inherited_method(self, ...):
    super().inherited_method(...)

In multiple inheritance, difficulties can arise when two superclasses have a property or method with the same name. The question is, when calling that method in an instance of the derived class, which of the two superclass methods will be executed? To address this problem, Python uses the Method Resolution Order (MRO), which determines the order of method and attribute lookup in a class hierarchy with multiple inheritance. You can view the MRO of a class using the __mro__ attribute or the mro() function

