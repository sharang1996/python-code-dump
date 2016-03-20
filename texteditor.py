from sys import argv
script,filename=argv
print "we are going to erase %r."%filename
print "If u dont want to do that hit CRRL-C(^C)"
print "if u want that hit return"

raw_input("?")

print "opening file..."
target = open(filename,'r+')

backup = target.read()

print "Truncating the file..."
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
