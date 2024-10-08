"""
MRO - Method Resolution Order

POO - MRO - Method Resolution Order

Method Resolution Order (Resolução de Ordem de Métodos), é a ordem da execução dos métodos (quem será executado primeiro).

```python
class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f"Eu sou {self.__nome}"

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} está nadando"

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} do mar!"

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f"{self._Animal__nome} está andando."

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} da terra!"

class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

# Testando

tux = Pinguim("Tux")
print(tux.cumprimentar())
```

```
Eu sou Tux da terra!
```

Em Python, a gente pode conferir a ordem de execução dos métodos (MRO) de 3 formas:

- Via propriedade da classe __mro__
- Via método mro()
- Via help

```
>>>Pinguim.__mro__
(<class '__main__.Pinguim'>, <class '__main__.Terrestre'>, <class '__main__.Aquatico'>, <class '__main__.Animal'>, <class 'object'>)
```

```
>>>help(Pinguim)
Help on class Pinguim in module __main__:
class Pinguim(Terrestre, Aquatico)
 |  Pinguim(nome)
 |
 |  Method resolution order:
 |      Pinguim
 |      Terrestre
 |      Aquatico
 |      Animal
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, nome)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __annotations__ = {}
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from Terrestre:
 |
 |  andar(self)
 |
 |  cumprimentar(self)
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from Aquatico:
 |
 |  nadar(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Animal:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
```
"""