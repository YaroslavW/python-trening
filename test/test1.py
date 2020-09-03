what = input('What will we do? (+,- или *,/): ')

a = float(input('Input first num  :'))
b = float(input('Input second num  :'))

if what == '+':
    c = a + b
    print("Result = " + str(c))
elif what =='-':
    c = a - b
    print("Result = " + str(c))
elif what == '*':
    c = a * b
    print('Result = ' + str(c))
elif what == '/':
    c = a / b
    print('Result =' + str(c))
else:
    print("What is wrong...")

