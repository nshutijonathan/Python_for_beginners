numbers = (input("enter the value of a number"))


def divisors(numbers):
    array = []
    for item in range(1, numbers):
        if(numbers % item == 0):
            print("divisors items", item)
            array.append(item)
    print(array)


    # print("all items",item)
divisors(numbers)
