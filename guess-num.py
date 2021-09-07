import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 #count = count + 1
	num = input('please enter a number: ')
	num = int(num)
	if num == r:
		print('you are right')
		print ('this is the', count, 'times')
		break
	elif num > r:
		print('bigger than the answer')
	elif num < r:
		print('smaller than the answer')
	print ('this is the', count, 'times')
