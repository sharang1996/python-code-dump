for letters in 'Python':
	print 'letters are %c \n'%(letters)
	
fruits=['apple','banana','orange']
for fruit in fruits:
	print 'current fruit :',fruit

print '\n'

for index in range(len(fruits)):
	print 'current fruit :',fruits[index]
	
print '\n'

for num in range(10,20):
	for i in range(2,num):
		if(num%i==0):
			j=num/i
			print '%d * %d is %d \n' % (i,j,num)
			break
	else:
		print num,' is a prime number \n'
		
