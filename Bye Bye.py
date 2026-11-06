a = True
b = True
while a == True:
    n = int(input('Enter an integer: '))
    if n%2 != 0:
        print('The value',n,'has been taken successfully!')
    elif n%2 == 0:
        while b == True:
            print('bye')