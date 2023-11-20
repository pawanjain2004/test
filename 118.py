class PlayerCharacter:
    # self refers to the instance of the class being created.
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('candy', 44)

player2 = PlayerCharacter('sandy', 84)

print(player1.name)
print(player2.name)
