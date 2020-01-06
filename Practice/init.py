class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)


#  initializing an object and passing it
jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()