for num in range(0,100):
	print "enter 2 numbers"
	num1=raw_input("Enter first ")
	num2=raw_input("enter second ")
	ch=raw_input("1.Addition \n 2.subtraction \n 3.multiplication \n 4.division \n 5.exit \n")
	if ch=='1':
		print int(num1)+int(num2)
	elif ch=='2':
		print int(num1)-int(num2)
	elif ch=='3':
		print int(num1)*int(num2)
	elif ch=='4':
		print int(num1)/int(num2)
	else:
		break
