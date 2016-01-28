import random

text1 = open("test.csv", "r")
data1 = [ ]
for line in text1:
    data1.append( line.strip().split(",") )

text2 = open("users.csv", "r")
data2 = [ ]
for line in text2:
    data2.append( line.strip().split(",") )
    
for i in range(len(data2)):
	data2[i][1] = len(data2[i][1].split("|"))

text3 = open("problems.csv", "r")
data3 = [ ]
for line in text3:
    data3.append( line.strip().split(",") )
    
# print data2[1][2:4]

for i in range(len(data3)):
	if data3[i][1]=='E':
		data3[i][1] = 1
	elif data3[i][1]=='E-M':
		data3[i][1] = 2
	elif data3[i][1]=='M':
		data3[i][1] = 3
	elif data3[i][1]=='M-H':
		data3[i][1] = 4
	elif data3[i][1]=='H':
		data3[i][1] = 5
	else:
		data3[i][1] = 0

user_d = {}
prob_d = {}

for i in range(1,len(data2)):
	user_d[data2[i][0]] = data2[i][1:4]			#solved_count, attempts
	# print user_d[data2[i][0]]
	# break	

for i in range(1,len(data3)):
	prob_d[data3[i][0]] = data3[i][1:5]			#level, accuracy, solved_count, error_count
	# print prob_d[data3[i][0]]
	# break

test = [ ]
for i in range(1,len(data1)):
	test.append(user_d[data1[i][1]] + prob_d[data1[i][2]])		#solved_count, attempts, level, accuracy, solved_count, error_count, output
	# break

random.shuffle(test)
# print test
f = open("../classifier/test_shuffle.csv","w")
for i in test:
	# f.write(i)
	for j in i:
		f.write(str(j)+",")
	f.write("\n")