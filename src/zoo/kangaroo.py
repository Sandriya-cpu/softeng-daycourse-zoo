# kangaroo.py

from .animal import Animal


class panda(Animal):
    def __init__(self, name="gertrude"):
        super().__init__(name, species="panda")

    def sound(self):
        return "thumps"

    def action(self):
        return "hops around happily."
