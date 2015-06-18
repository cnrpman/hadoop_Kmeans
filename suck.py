import csv

f_csv = csv.reader(file('glass.data', 'rb'))
themaxs = []
themins = []
for i in range(11):
	themaxs.append(0.0)
	themins.append(300.0)

for row in f_csv:
	colTot = 0
	for col in row:
		fcol = float(col)
		if fcol > themaxs[colTot]:
			themaxs[colTot] = fcol
		if fcol < themins[colTot]:
			themins[colTot] = fcol
		colTot += 1

print map(lambda a, b: ("%.2f" % (a - b)), themaxs, themins)