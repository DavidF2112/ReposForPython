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
        self.couple.items(persone)


if __name__ == '__main__':
    pesrone1 = Persone("David" , 16)
    group1 = Group()
    group1.add_persone(pesrone1)
    print("END PROGRAM")