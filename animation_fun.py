import time
import os

def clear():
	# print('\n' * 100)
	os.system('clear')

x = 1

while(x < 50):
	global xxv
	global xv

	xxv = str('\n' * 10)
	xv = '                 '

	r = .1 # Rate of change, in seconds.

	clear()
	print(xxv+xv+'/')
	x += 1
	time.sleep(r)
	clear()
	print(xxv+xv+'-')
	x += 1
	time.sleep(r)
	clear()
	print(xxv+xv+'\\')
	x += 1
	time.sleep(r)
	clear()
	print(xxv+xv+'|')
	x += 1
	time.sleep(r)

clear()

print(xxv+xv+'THE END.'+(xxv))
