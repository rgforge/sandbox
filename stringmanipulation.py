#! /usr/bin/python3.7

#Manipulating output

#x = input('Please enter the string you would like. \n')
x = 'This is the string.'
print(x.center(40,'#'),'\n')
print(x.ljust(40,'-'),'\n')
print(x.rjust(40,'_'),'\n')

y = 5.12345678901234567890
print(y)
print('{:010.7f}'.format(y).center(40,'#'))
