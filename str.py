#import string

f = open("test.dat","w")
x = 52
"""f.write(str(x))
f.close()"""
f.write("en junlio vendimos %d motos." % x)
f.close()