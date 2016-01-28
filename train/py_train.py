import random

train = [ ]

text1 = open("submissions.csv", "r")
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

# print data3[i][2:5]

for i in range(1003):
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
	user_d[data2[i][0]] = data2[i][1:4]			#skill_count, solved_count, attempts
	# print user_d[data2[i][0]]
	# break	

for i in range(1,len(data3)):
	prob_d[data3[i][0]] = data3[i][1:5]			#level, accuracy, solved_count, error_count
	# print prob_d[data3[i][0]]
	# break
output=[]
output.append(0)
for i in range(1,len(data1)):
	# print user_d[data1[i][0]]
	# print prob_d[data1[i][1]]
	print i, len(data1)
	output[0]=0
	if data1[i][2] == "SO" and data1[i][3] == "AC":
		output[0] = 1
	train.append(user_d[data1[i][0]] + prob_d[data1[i][1]] + output)		#level, solved_count, attempts, accuracy, solved_count, error_count, output
	# break

random.shuffle(train)
# print train
f = open("../classifier/train_shuffle.csv","w")
for i in train:
	# f.write(i)
	for j in i:
		f.write(str(j)+",")
	f.write("\n")