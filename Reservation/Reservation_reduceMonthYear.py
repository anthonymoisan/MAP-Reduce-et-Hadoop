#!/home/cloudera/anaconda3/bin/python3.7

import sys

dictRes={}

for line in sys.stdin:
	(monthAndYear, seats) = line.strip().split("\t")
	month = monthAndYear[0:2]
	year = monthAndYear[3:7]
	try:
		seats = int(seats)
	except ValueError:
		#seats is not a number
		continue
	
	if year in dictRes:
		if month in dictRes[year]:
			dictRes[year][month] += seats
		else:
			dictRes[year][month] = seats
	else:
		dictMonth = {}
		dictMonth[month] = seats
		dictRes[year] = dictMonth	
				
for year in sorted(dictRes):
	for month in sorted(dictRes[year]):
		print ("Year : %s - Month : %s \t Number of passengers from Sydney : %s"% (year, month, dictRes[year][month]))
	
	