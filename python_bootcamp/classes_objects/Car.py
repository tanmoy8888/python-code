class Car:
    def _init_(self, model, colour):
        self.model_name= model
        self.colour = colour
    def launch(self):
        print(f"{self.model_name} has {self.colour}")

    def main(self):
        car1 = Car("Maruti","Blue")
        car1.launch()
    if __name__ == '__main__':
        main()