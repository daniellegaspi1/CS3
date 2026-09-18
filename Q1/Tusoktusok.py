class Sauce:
    def __init__(self,name,taste):
        self.name = name
        self.taste = taste
        print(self.name,"is cooked")
    def __del__(self):
        print(self.name,"is ubos na")
    def __str__(self):
        return "This is " +self.name+ "and it tastes" +self.taste

class Tusoktusok:
    def __init__(self,name,sauce):
        self.name = name
        self.sauce = sauce
        print(self.name,"is cooked and dipped in",self.sauce.name)
    def eat(self):
        print("I am eating",self.name,"with",self.sauce.taste)
    def __del__(self):
        print(self.name,"was thrown in the trash can")

vinegar = Sauce("vinegar","sour")
fishball = Tusoktusok("fishball",vinegar)
fishball.eat()
del fishball
print(vinegar)
