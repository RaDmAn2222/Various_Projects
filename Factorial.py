def fact(num):
    if num == 1:
        return 1
    elif num == 0:
        return 1
    elif num < 0:
        print('Not defined')
    else:
        return num * fact(num - 1)


num = int(input("Enter a number: "))
result = fact(num)
print("Factorial is", result)
