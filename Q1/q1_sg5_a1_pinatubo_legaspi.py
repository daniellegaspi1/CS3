class Hero:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
        
    def take_damage(self,amount):
        self.hp -= amount
        print(f"{self.name} took {amount} damage.")
    
x = Hero("Arthur", 100)
y = Hero("Morgana", 100)

x.take_damage(10)

print(f"{x.name} is at {x.hp}  hp.")
print(f"{y.name}  is at {y.hp}  hp.")
