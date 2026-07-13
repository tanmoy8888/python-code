
def even_odd(a):
    if a % 2 == 0:
       print("Even")
    else:
       print("Odd")

def mandatory_optional(first ="Hello", second="World"):
    return first + " "+second

def lambda_functions():
    l = [1,2,3,4,5]
    print(l)
    square_list = map(lambda x : x*x,l)
    print(list(square_list))


def main():
    even_odd(5)
    print(even_odd(5))
    print(mandatory_optional())
    print(mandatory_optional("Hii"))
    print(mandatory_optional(second="There"))
    lambda_functions()

if __name__ == '__main__':
   main()