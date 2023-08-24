string = input("Type something: ")

counter = dict()

for letter in string:
    counter[letter] = counter.get(letter, 0) + 1

for data in list(counter.keys()):
    print('There are %s %s characters' %(counter[data],data))
