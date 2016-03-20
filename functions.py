def print3(*argc):
	arg1,arg2,arg3=argc
	print "arguement 1: %r \n arguement2: %r \n arguement3: %r \n"%(arg1,arg2,arg3)
	
def print2(arg1,arg2):
	print "arguement1:%r \n arguement2:%r \n"%(arg1,arg2)

print3("I","Am","Awesome")
print2(5,4)
