class PlayerCharacter:
    membership = True
    # Class Object Attribute

    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def shout(self):
        print(f'my name if {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2




print(PlayerCharacter.adding_things(2, 3))
