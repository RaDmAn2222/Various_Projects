import random
guess = random.randint(1,99)
name = str(input(" Hi, What's your name? "))
print(guess)
answer = input("Choose between 'right', 'smaller', 'bigger': ")
a = 1
b = 99

while answer != "right":
    if answer == "smaller":
        b = guess
        guess = random.randint(a, b - 1)
        print(guess)
    elif answer == "bigger":
        a = guess
        guess = random.randint(a + 1 , b) 
        print(guess)
    answer = input("Choose between 'right', 'smaller', 'bigger': ")


print("You did it", name,"!!!")