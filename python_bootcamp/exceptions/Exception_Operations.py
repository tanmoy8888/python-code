

def input_operations():
    try:
      n = int(input("Please enter a number \n"))
      print("You entered , "+str(n))
    except ValueError:
        print("Please enter numeric values only")


def main():
    input_operations()

if __name__ == '__main__':
   main()