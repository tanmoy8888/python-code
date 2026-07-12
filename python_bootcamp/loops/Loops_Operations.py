
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

def main():
    while_loop()
    for_loop()

if __name__ == '__main__':
  main()