
class WashingMachine:
    def __init__(self):
        pass

    def to_wash(self, temperature = "Hot"):
        self._fill_the_water_tank(temperature)
        self._add_soap()
        self._to_wash()
        self._centrifuge()

    def _fill_the_water_tank(self, temperature):
        print(f'Filling the tank with {temperature} water')

    def _add_soap(self):
        print("Adding the soap")

    def _to_wash(self):
        print("Washing clothes")

    def _centrifuge(self):
        print("Centrifuge the clothes")

def run():
    washing_machine = WashingMachine()
    washing_machine.to_wash()

if __name__ == "__main__":
    run()