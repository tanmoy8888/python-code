class Car:
    manufactured_in = "India"
    display = "digital"

    def __init__(self, model, colour):
        self.model_name= model
        self.colour = colour

    def launch(self):
        print(f"{self.model_name} has {self.colour}")

    @classmethod
    def show(self):
        print(f"{self.manufactured_in}")

    @classmethod
    def display_option(cls):
        print(f"{cls.display}")

def main():
    car1 = Car("Maruti", "Blue")
    car1.launch()

    car1.show()
    car1.display_option()

if __name__ == "__main__":
    main()
