#! /usr/bin/env python

# Calculator


def adding():
	a = map(int,(input('Enter the numbers you would like to add seperated by spaces.   ')).split())
	a = (sum(a))
	print('The answer is %d' % a) 

def subtracting():
	x = int(input('Enter the first number to be subtracted from.   '))
	y = int(input('Enter the second number to be subtracted.   '))
	b = x - y
	print('The answer is %d' % b)

def multiplying():
	numbers = int(input('How many numbers do you want to multipy?   '))
	b = 1
	for x in range(numbers):
		a = int(input('What number do you want to work with?   '))
		b *= a
	print('The answer is %d.' % b)

def dividing():	
	try:
		x = int(input('What is the dividend?   '))
		y = int(input('What is the divisor?   '))
		z = x//y
		r = x%y
		print(f'The quotient is {z} and the remainder is {r}')
	except:
		print("You can't divide by ZERO.")
	else:
		pass

def sq_root():
	x = int(input('What number would you like the square root of?   '))
	if x < 0:
		print('Enter a valid number')
	else:
		print(f'The square root of {x} is {x**(.5)}')

def sq():
	x = int(input('What number do you want to square?   '))
	print(f'{x} squared is {x**2}')

def cubed():
	x = int(input('What number do you want to cube?   '))
	print(f'{x} cubed is {x**3}')

def sin():
	x = int(input('What is the length of the opposite side?   '))
	y = int(input('What is the length of the hypotenuse?   '))
	print(f'The sine is {round((x/y),2)}')

def cos():
	x = int(input('What is the length of the adjancent side?   '))
	y = int(input('What is the length of the hypotenuse?   '))
	print(f'The cosine is {round((x/y),2)}')

def tang():
	x = int(input('What is the length of the opposite side?   '))
	y = int(input('What is the length of the adjacent side?   '))
	print(f'The tangent is {round((x/y),2)}')

def fact():
	x = int(input('What number do you want to perform a factorial function on?   '))
	def factl(x):
		if x == 0:
			return 1
		else:
			return x * factl(x-1)
	print(f'The factorial of {x} is {factl(x)}.')

def inverse():
	#try:
		inv_question = (input('Press 1 for an additive inverse of the number. Press 2 for the multiplicative inverse or reciprocal.   '))
		if inv_question == '1':
			x = int(input('What is the number you would like the additive inverse of?   '))
			print(f'The additive inverse of {x} is {-x}.')
		elif inv_question == '2':
			x = int(input('What is the number you would like the multiplicative inverse or reciprocal of?   '))
			print(f'The multiplicative inverse of {x} is {round((1/x), 2)}.')
		else:
			print('You must enter 1 or 2.')
			inverse()
	#except:
	#	print('wrong')
	
def mod():
	x = int(input('What is the first number you want to find the divide?   '))
	y = int(input('What is the number you to divide by?   '))
	print(f'The remainder of {x} divided by {y} is {x%y}.')

def opening():
	x = int(input('''Choose what you would like to do:
	Enter 1 for addition
	Enter 2 for subtraction
	Enter 3 for muliplication
	Enter 4 for division
	Enter 5 for square root
	Enter 6 for square
	Enter 7 for cube
	Enter 8 for sine
	Enter 9 for cosine
	Enter 10 for tangent
	Enter 11 for factorial
	Enter 12 inverse
	Enter 13 for modulus
		'''))

	if x == 1:
		adding()
	elif x == 2:
		subtracting()
	elif x == 3:
		multiplying()
	elif x == 4:
		dividing()
	elif x == 5:
		sq_root()
	elif x == 6:
		sq()
	elif x == 7:
		cubed()
	elif x == 8:
		sin()
	elif x == 9:
		cos()
	elif x == 10:
		tang()
	elif x == 11:
		fact()
	elif x == 12:
		inverse()
	elif x == 13:
		mod()
	else:
		print('Please enter a valid choice.')
		opening()


opening()

while True:
	ans = input('Would you like another calculation? Y for yes.  Any key for no.   ')
	if ans.lower() == 'y':
		opening()
	else:
		print("Run program again when you are ready")
		break




