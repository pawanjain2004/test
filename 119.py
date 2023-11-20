class PlayerCharacter:
    membership = True
    # Class Object Attribute 
    def __init__(self, name, age):
        if(PlayerCharacter.membership):
          self.name = name  # attributes
          self.age = age

    def shout(self):
        print(f'my name if {self.name}')
        


player1 = PlayerCharacter('candy', 44)

player2 = PlayerCharacter('sandy', 84)

print(player1.shout())
print(player2.membership)
