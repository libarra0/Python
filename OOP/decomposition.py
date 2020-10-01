
class Automobile:

    def _init__(self, model, branch, color):
        self.model = model
        self.branch = branch
        self.color = color
        self._status = 'Resting'
        self._engine = Engine(cylinders = 4)

    def accelerate(self, type="Slow"):
        if type == "Fast":
            self._engine.inject_gasoline(10)
        else:
            self._engine.inject_gasoline(3)

        self._status = "Moving forward"

class Engine:

    def __init__(self, cylinders, type="Gas"):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0

    def inject_gasoline(self, quantity):
        pass