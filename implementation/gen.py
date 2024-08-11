import csv
import random

animals = []
areas = []
abundances = []

with open('animals.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		animals.append(row)


with open('areas_hec.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		areas.append(row)

for area in areas:
	samples = random.sample(animals,int(area[0]))
	for sam in samples:
		r = random.random()
		abundance = ""
		if r < 0.25:
			abundance = "L"
		elif r < 0.75:
			abundance = "M"
		else:
			abundance = "H"
		
		abundances.append([area[1],sam[0],"SEASON START","SEASON END",abundance])


with open('/dev/stdout', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for a in abundances:
		writer.writerow(a)
