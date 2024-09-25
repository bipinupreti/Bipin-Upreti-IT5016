class Person:
    def __init__(self):
        self.A="James"
        self._B="James Bond"
    def PrintName(self):
        print(self.A)
        print(self._B)
p=Person()
p.A
p._B
p.PrintName()