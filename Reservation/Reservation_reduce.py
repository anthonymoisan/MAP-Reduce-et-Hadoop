#!/home/cloudera/anaconda3/bin/python3.7

import sys

dictRes={}

for line in sys.stdin:
	(month, seats) = line.strip().split("\t")
	try:
		seats = int(seats)
	except ValueError:
		#seats is not a number
		continue
	
	if month in dictRes:
		dictRes[month] += seats
	else:
		dictRes[month] = seats	
				
for month in sorted(dictRes):
	print ("Month : %s\t Number of passengers from Sydney : %s"% (month, dictRes[month]))
	
	