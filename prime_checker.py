quit = False
list1 = []
while quit == False:
    num = int(input("\nPlease give me a number. I'll check if it's prime.\n(enter 0 to quit)\n"))
    if num == 0:
        break
    elif num == 1:
        print(f"{num} is not prime as it is not divisible by at least 2 numbers.")
    elif num == 2:
        print(f"{num} is a prime number, divisible by itself and 1.")
    else:
        for x in range(2, num - 1):
            if num % x == 0:
                list1.append(x)
        if len(list1) == 0:
            print(f"\n{num} is a prime number.")
        for y in list1:
            if num % y == 0:
                print(f"\n{num} is divisible by {y}.\n{num} divided by {y} equals {int(num / y)}")

    list1.clear()
