#!/home/cloudera/anaconda3/bin/python3.7
import sys

for line in sys.stdin:
	listReservation = line.strip().split(';')
	monthAndYear = listReservation[0]
	inboundOrOutbound = listReservation[1]
	city = listReservation[2]
	stops = listReservation[10]
	seats = listReservation[12]
	month = monthAndYear[0:2]
	
	if(( inboundOrOutbound == "O" ) and ( stops == "0" ) and (city == "Sydney")):
		print ("%s\t%s" % (month, seats))
	

	
	