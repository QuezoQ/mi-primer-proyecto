#this is a comment.
#Imprimir mensaje en pantalla
print("Hello, World!")
#condicional SI, un numero es mayor que otro, imprime un mensaje
if 5 > 2:
	print("Five is grater than two!")
#variables declaradas, numero y texto, python reconoce automaticamente el tipo de variable
x = 5 #integer variable
y = "Hello, Patricio" #string variable
#imprimir variables recien declaradas.
print(x) #output integer
print(y) #output string

#Siguiente parte de los comentarios.

#statements
print("Hello World")
print("Have a good day.")
print("Learning Python is fun!")

#try Double Quote
print("Hello World")
print('This will also work!')

#Print without new line
print("Hello World", end=" ")
print("I will print on the same line")

#Python Classes
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello {}!".format(self.name))

adam = Person('Adam')
adam.say_hello()
