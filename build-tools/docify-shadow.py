#!/usr/bin/env python

# simple script to hack together python __doc__ support in swig-generated
# .py shadow class source files

import sys
import string
import re
import os



if len(sys.argv)<2:
  print 'usage: docify.py <swig-generated .py shadow class file>'
  sys.exit(1)

f=open(sys.argv[1],'r')
outfile=open('%s.tmp' % sys.argv[1],'w')

data=f.readlines()

for i in xrange(0,len(data)):
  match=re.search('^.*def __del__',data[i])
  if match:
    #print match.group(0)
    i=i+1
    break

if not match:
  raise 'source file doesn\'t look like swigged shadow class code'

# read ahead to next def statement
for i in xrange (i,len(data)):
  if re.search('^.*def', data[i]):
    break

pymeths=[]
for i in xrange (i,len(data)):
  if re.search('^.*def __repr__', data[i]):
    break
  pymeths.append(data[i])


methods={}
for line in pymeths:
   methmatch=re.search('def +([^ (]*) *\(\*args\)',line)
   fnmatch=re.search('\:.*[^_p](_?pcapc?\.[^(, ]+) *[(,]',line)
   methname=None
   fname=None
   if methmatch: methname=methmatch.group(1)
   if fnmatch: fname=fnmatch.group(1)
   if methname and fname:
     methods[methname]=fname
   else:
     # print 'warning: method(%s) fname(%s)\n\tline: %s' % ( methname, fname, line )
     pass

#print methods

for i in xrange(0,len(data)):
  outfile.write(data[i])
  match=re.search('^.*def __init__',data[i])
  if match:
    #print match.group(0)
    i=i+1
    break

# spit out the next 2 lines verbatim
outfile.write(data[i])
i=i+1
outfile.write(data[i])
i=i+1

outfile.write('        import sys\n')
outfile.write('        if sys.version[0]==\'2\':\n')

for method, fname in methods.items():
  outfile.write('          self.%s.__setattr__(\'__doc__\',%s.__doc__)\n' % (method, fname))


# spit out rest of file verbatim
for i in xrange (i,len(data)):
  outfile.write(data[i])

outfile.close()
f.close()

os.system('mv %s.tmp %s' % (sys.argv[1], sys.argv[1]))
