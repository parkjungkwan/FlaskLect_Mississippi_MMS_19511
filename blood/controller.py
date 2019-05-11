from blood.model import BloodModel

class BloodController:
    def __init__(self, weight, age):
        self._model = BloodModel()
        self._weight = weight
        self._age = age

    def calc(self):
        pass