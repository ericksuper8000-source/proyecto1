class A():
    def Mostrar(self):
        print (f'Hola A')

class E():
    def Mostrar(self):
        print(f'Hola E')

class B(E):
    def Mostrar(self):
        print(f'Hola B')

class C(A):
    def Mostrar(self):
        print(f'Hola C')

class D(B,C):
    def Mostrar(self):
        print(f'Hola D')

Objeto1 = D()

Objeto1.Mostrar()

