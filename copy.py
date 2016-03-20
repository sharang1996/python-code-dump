from sys import argv
from os.path import exists

script,fromfile,tofile=argv

infile=open(fromfile)
text=infile.read()

print "Does the output file exist?? %r"%exists(tofile)
print "Ready ,hit CTRL-C to exit and RETURN to continue..."
raw_input()

outfile=open(tofile,'w')
outfile.write(text)

print "Done!!!"

infile.close()
outfile.close()
