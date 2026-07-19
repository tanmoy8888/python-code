class Car:
    manufactured_in = "India"
    def __init__(self, model, colour):
        self.model_name= model
        self.colour = colour

    def launch(self):
        print(f"{self.model_name} has {self.colour}")

    @classmethod
    def show(self):
        print(f"{self.manufactured_in}")

def main():
    car1 = Car("Maruti", "Blue")
    car1.launch()
    car1.show()

if __name__ == "__main__":
    main()
