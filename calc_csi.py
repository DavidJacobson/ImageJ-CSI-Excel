## ImageJ CSI Finder
## By David Jacobson
## CUNY - CCNY - Biomedical Engineering STEM ERE '17

from math import pi as pi


### Set this, round to x decimal place
ROUND_TO = 3 
###

# This is messy, but it enables you to directly copy paste from the 
# ImageJ dialog. It stripts out the \t (tabs) and breaks it into pieces
# Replace this as needed.
input = """
1	615.776	115.265
2	177.696	50.065
3	99.937	43.14
4	242.587	57.331
5	166.607	48.578

""".replace("\t", " ").split()

CSIs = [] # Prepare an empty list for the CSIs
avg_csi = 0
pairs = map(None,*[iter(input)]*3) # This splits the input into tuples
								   # (cell #, area, perimiter)
avg_area = 0 # Setup for average
avg_per  = 0 
for pair in pairs:
	area = float(pair[1])
	per  = float(pair[2])
	avg_area += area
	avg_per  += per
	csi = (4 * pi * area) / (per **2) # CSI formula
	avg_csi += csi
	CSIs.append(round(csi,ROUND_TO))  # This doesn't pad the end with
									  # zeros, eg: 1.5 instead of 1.50
									  # That can be done automatically
									  # In Excel

for each in CSIs:
	print each
avg_area /= len(pairs)
avg_per  /= len(pairs)
avg_csi  /= len(pairs)
avg_area = round(avg_area, ROUND_TO)
avg_per = round(avg_per, ROUND_TO)
avg_csi = round(avg_csi, ROUND_TO)
print "\nAverage Area: {}".format(avg_area)
print "Average Perimiter: {}".format(avg_per)
print "Average CSI: {}".format(avg_csi)
print """\n[*]Note: Average CSI is taken by calculating the mean of 
the CSIs, not the CSI of the avg Area & Perimeter"""

