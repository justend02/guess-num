import random

r = random.randint(1, 100)
while True:
	num = input('please enter a number: ')
	num = int(num)
	if num == r:
		print('you are right')
		break
	elif num > r:
		print('bigger than the answer')
	elif num < r:
		print('smaller than the answer')
