
class Persona:
    
    def __init__(self, name):
        self.name = name

    def forward(self):
        print("I am walking")
    
class Cyclist(Persona):
    def __init__(self, name):
        super().__init__(name)

    def forward(self):
        print("I ride a bike")
    
def main():
    persona = Persona("David")
    persona.forward()

    cyclist = Cyclist("Leonardo")
    cyclist.forward()

if __name__ == "__main__":
    main()