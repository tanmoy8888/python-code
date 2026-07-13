
def even_odd(a):
    if a % 2 == 0:
       print("Even")
    else:
       print("Odd")

def mandatory_optional(first ="Hello", second="World"):
    return first + " "+second

def main():
    even_odd(5)
    print(even_odd(5))
    print(mandatory_optional())

if __name__ == '__main__':
   main()