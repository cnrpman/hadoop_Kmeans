maxcorrect = 0
mapping = []
dic = {}

for i in range(7):
	mapping.append(0)

def chk():
	file = open("kmeans_result")
	lines = file.readlines(100000)
	correct = 0
	for line in lines:
	    if mapping[int(line.split('	')[0])] == int(line.split(',')[10].replace('\n','')):
	    	correct += 1

	file.close()
	return correct

def recur(pos):
	global maxcorrect

	if pos == 7:
		rescorrect = chk()
		dic[rescorrect] = str(mapping)
		if rescorrect > maxcorrect:
			maxcorrect = rescorrect

	for i in range(1,8):
		if i == 4:
			continue
		flag = 0
		for j in range(1,pos):
			if i == mapping[j]:
				flag = 1
		if flag:
			continue
		mapping[pos] = i
		recur(pos+1)

recur(1)
print dic[maxcorrect] + ' ' + str(maxcorrect)


