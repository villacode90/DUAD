#3. Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo

#La herencia múltiple: Es La capacidad de una subclase de heredar de múltiples superclases.

#Esto conlleva un problema, y es que si varias superclases tienen los mismos atributos o métodos, la subclase sólo podrá heredar de una de ellas.

#En estos casos Python dará prioridad a las clases más a la izquierda en el momento de la declaración de la subclase:

class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este método lo heredo de A")

class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este método lo heredo de B")

class C(B,A):
    def c(self):
        print("Este método es de C")

#Instaciamos clase C, clase C hereda de la clase A y B, pero al realizara impresión de la clase que esté mas a la izquierda ya que hereda de dos clases, osea, imprimira el mensaje de la clase B.
c = C()

#Llamo el método A de la clase A heredada de la Clase C.
c.a()
#Llamo el método B de la clase B heredada de la Clase C.
c.b()
#Llamo el método C de la clase C.
c.c()