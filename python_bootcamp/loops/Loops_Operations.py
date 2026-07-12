
def while_loop():
    print("Printing while loops elements")
    a = 0
    while a < 5:
        print(a)
        a += 1

def for_loop():
    print("Printing for loops elements")
    names = ["Tanmoy","Rahul","Raj","Rohit"]
    for name in names:
        print(name)

def range_operations():
    print("Printing range elements")
    for i in range(0,10,2):
        print(i)

def main():
    while_loop()
    for_loop()
    range_operations()

if __name__ == '__main__':
  main()