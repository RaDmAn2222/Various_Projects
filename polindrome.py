string = input("Type something: ")
my_list = []

for i in string:
    my_list.append(i)

print(my_list)
my_list.reverse()
print(''.join(my_list))

if ''.join(my_list).lower() == string.lower():
    print("This is a polindrome")
else:
    print("This is not a polindrome")
