#! /usr/bin/python3

#D = diameter
#v = velocity
#rho = density
#mu = viscosity

'''

Check eval(input()) to verify that numbers are entered.
Try another def for print results.
Fix division by zero error
Exception handling

'''

def reynolds_number():

	D = eval(input('What is the numeric diameter? '))
	v = int(input('What is the numeric velocity? '))
	rho = int(input('What is the numeric density? '))
	mu = int(input('What is the numberic viscosity? '))
	reyn = (D*v*rho)/mu

#def reynolds_output():

	if reyn < 2100:
		print('The Reynolds number is %d.  And, it is laminar flow.' %reyn)
	elif reyn  >= 2100 and reyn <= 4000:
		print('The Reynolds number is %d.  And it is transient flow.' %reyn)
	elif reyn > 4000:
		print('The Reynolds number is %d.  And it is turbulent flow.' %reyn)
	else:
		print('There is no flow, or something went terribly wrong!!!')


question = 'Would you like to calculate Reynolds Number? Answer y or any key for no.     '
ans = input(question)
ans = ans.lower()

while ans == 'y':
	reynolds_number()
#	reynold_output()
	ans = (input(question))
	ans = ans.lower()

if ans != 'y':
	print('Run program again when you are ready.')
