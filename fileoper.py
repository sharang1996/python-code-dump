from sys import argv

script,filename=argv

txt=open(filename)

print "heres your file!!! %r:"%filename

print txt.read()

print "enter your filename again"
fname=raw_input("> ")

print open(fname).read()
