import random
start = input('Please decide the initial value: ')
end = input('Please enter one last value: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
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
