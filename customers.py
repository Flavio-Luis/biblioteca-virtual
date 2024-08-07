class Person: # class Person com seus respectivos atributos
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Client(Person): # subclass que herda de Person e tem um atributo adicional
    def __init__(self, name, age, library_card):
        super().__init__(name, age)
        self.library_card = library_card