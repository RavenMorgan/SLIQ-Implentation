# Sliq.py
# SENG 474
# Jeremy Ho & Helen Lin

import os, sys, string, time
from classlist import *
"""""
def main():
	#Main program
	
	# Read input file
	try:
		f = sys.stdin
	except IOError as e:
		sys.exit("{}".format(e))
	rawinput = []
	for line in f:
		if line.startswith("%") or not line.strip():
			continue
		rawinput.append(line[:-1].lower()) # ditch trailing newline
	
	# Remove non-data lines & format
	rawdata = rawinput[rawinput.index("@data")+1:]
	data = []
	for line in rawdata:
		data.append(line.split(','))
	
	# Process input
	start = time.time()
	CL = classlist(data)
	end = time.time()
	#print CL.leaves
	print( CL.displayTree())
	print ("SLIQ took " + str(end - start) + " seconds")\
"""
def main():
	data = [
		[ "Sunny", "17", "High", "False", "No" ],
		[ "Sunny", "20", "High", "True", "No" ],
		[ "Overcast", "23", "High", "False", "Yes" ],
		[ "Rainy", "32", "High", "False", "Yes" ],
		[ "Rainy", "43", "Normal", "False", "Yes" ],
		[ "Rainy", "68", "Normal", "True", "No" ],
		[ "Overcast", "17", "Normal", "True", "Yes" ],
		[ "Sunny", "20", "High", "False", "No" ],
		[ "Sunny", "23", "Normal", "False", "Yes" ],
		[ "Rainy", "32", "Normal", "False", "Yes" ],
		[ "Sunny", "43", "Normal", "True", "Yes" ],
		[ "Overcast", "68", "High", "True", "Yes" ],
		[ "Overcast", "17", "Normal", "False", "Yes" ],
		[ "Rainy", "20", "High", "True", "No" ]
	]
	data2 = [
		[ "23", "Family", "HIGH" ],
		[ "17", "Sports", "HIGH" ],
		[ "43", "Sports", "HIGH" ],
		[ "68", "Family", "LOW" ],
		[ "32", "Truck", "LOW" ],
		[ "20", "Family", "HIGH" ]
	]
	CL = classlist(data)
	#CL.init() 
	#print("soooooooooooooooooort",CL.sortList(data2 , 4))
	#print("--------",CL.addID(data))
	print("*********",CL.doSLIQ(data,5,2)) 
	print (CL.leaves)
	print (CL.displayTree())
if __name__ == '__main__':
	main()