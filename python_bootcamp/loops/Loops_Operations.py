
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

def list_comprehension():
    rectangles = [(2,3),(4,5),(6,7)]
    rectangles_area = [(x,y,x*y) for (x,y) in rectangles]
    print(rectangles)
    print(rectangles_area)


def main():
    while_loop()
    for_loop()
    range_operations()
    list_comprehension()

if __name__ == '__main__':
  main()