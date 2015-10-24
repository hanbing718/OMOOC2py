# -*- coding: utf-8 -*-
import os
ls =os.linesep

#get filename

fname = raw_input('input a file name to save filenames:%s' % ls)
	

#

print"\nEnter lines *'.'by itself to quit).\n"

#loop until user terminates input

while True:
    	entry=raw_input('>')
	if entry=='EXIT':
       		break
    	elif entry=='READ':
			fobj=open(fname,'r')	
			for eachline in fobj:
				print eachline
    	elif entry=='WRITE':
		all=[]
		entrytxt=raw_input('>>')
       		all.append(entrytxt)
                
        else:	
		print 'ERROR'
fobj=open(fname,'w')
fobj.writelines(['%s%s' % (x,ls)for x in all])
fobj.close()
print 'done'
