print('Yonso Project Model School (YPMS)')
any1 = (input('Surname: '))
any2 = (input('Middle Name: '))
any3 = (input('Last Name: '))
sum = (any1+any2+any3)
print(any1,any2,any3)
num = int(input('Your Class: '))
if  num >= 1 and num <= 6:
    print('Valid')
else:
    print('Invalid')
payment = int(input('Fees: GH'))
if payment >= 650 and payment <= 850:
    print('Paid')
elif payment >=0 and payment <= 649:
    print('Not Accepted')
elif payment >= 851:
    print('Not Accepted')
person = float(input('Enter your age: '))
if  person >= 0 and person <= 12:
    print('CHILD')
elif person >= 13 and person <= 19:
    print('TEENAGE')
else:
    print('Any age above 19 is ADULT.')
