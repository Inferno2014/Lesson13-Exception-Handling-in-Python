try:
    num = int(input('Enter an integer: '))
    num1 = int(input('Enter second integer: '))
    result = num/num1
    result1 = num + num1
    print('Result is',result)
    print('Result is',result1)
except ZeroDivisionError:
    print('Division by zero(0) is not allowed!')
except ValueError:
    print('Please enter in numerical value!')
except NameError as ex:
    print('The exception is',ex)
finally:
    print('I will execute no matter what happens!')