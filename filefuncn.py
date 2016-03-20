from sys import argv
script,input_file=argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)
	
def print_a_line(line_num,f):
	print line_num,f.readline()
	
print "First we print the whole file"
print_all(open(input_file))

f=open(input_file)

print "now we rewind to the start of the file"
rewind(f)

print "now we print 3 lines"

linenum=1
print_a_line(linenum,f)
linenum+=1
print_a_line(linenum,f)
linenum+=1
print_a_line(linenum,f)
