def main():
    name  = "Tanmoy"
    list = ["tanmoy","rahul","raj"]
    print(name == "tanmoy")
    print(name == "Tanmoy")
    print("T" in name)
    print("t" in name)
    print("Tan" in name)
    ## concatenations
    print("Concatenation example :: "+ (name+" ") *2)


    print(list == ["tanmoy","rahul","raj"])
    print(list == ["Tanmoy","rahul","raj"])
    print("Ram" in list)
    print("Raj" in list)
    print("Ram" not in list)
    ## concatenations -- For list have to convert it into str then concatenation will work
    print("Concatenation example list :: " + str(list) * 2)
    print(list[1])
    print(list[-2])


if __name__ == '__main__':
    main()
