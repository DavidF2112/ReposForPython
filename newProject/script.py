class Persone:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def __str__(self):
        return f"Hello Mr.{self.name} - {self.age}"
    

class Group:
    def __init__(self):
        self.couple = {}

    
    def add_persone(self,persone:Persone):
        self.couple[persone.name] = persone.age

    
    def print_dict(self):
        for name , age in self.couple.items():
            print(f"Name - {name}, Age - {age}")


if __name__ == '__main__':
    pesron1 = Persone("David" , 16)
    group1 = Group()
    group1.add_persone(pesron1)
    group1.print_dict()
    print("END PROGRAM")