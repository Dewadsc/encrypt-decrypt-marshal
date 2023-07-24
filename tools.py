import os
import marshal

s = open("main.py").read()
g = compile(s, '', 'exec')
b = marshal.dumps(g)

w = open('f-marshal.py', 'w')
w.write('import marshal\n')
w.write('exec(marshal.loads('+repr(b)+'))')
w.close()