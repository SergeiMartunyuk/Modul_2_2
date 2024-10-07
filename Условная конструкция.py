first = int(input('Enter a number: '))
second = int(input('Enter a number: '))
third = int(input('Enter a number: '))
if first == second == third:
    print(3)
elif first == second and first != third or first != second and first == third:
    print(2)
else:
    print(0)