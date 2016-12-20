
#Example 1
items = [(5, 10), (10, 1), (100, 50), (500, 100), (11, 99), (53, 33), (12, 100), (66, 500), (13, 5), (7, 77),
         (5, 10), (10, 1), (100, 50), (500, 100), (11, 99), (53, 33), (12, 100), (66, 500), (13, 5), (7, 77),
         (5, 10), (10, 1), (100, 50), (500, 100), (11, 99), (53, 33), (12, 100), (66, 500), (13, 5), (7, 77),
         (5, 10), (10, 1), (100, 50), (500, 100), (11, 99), (53, 33), (12, 100), (66, 500), (13, 5), (7, 77),
         (5, 10), (10, 1), (100, 50), (500, 100), (11, 99), (53, 33), (12, 100), (66, 500), (13, 5), (7, 77),
         (5, 10), (10, 1), (100, 50), (500, 100), (11, 99), (53, 33), (12, 100), (66, 500), (13, 5), (7, 77),
         (5, 10), (10, 1), (100, 50), (500, 100), (11, 99), (53, 33), (12, 100), (66, 500), (13, 5), (7, 77),
         (5, 10), (10, 1), (100, 50), (500, 100), (11, 99), (53, 33), (12, 100), (66, 500), (13, 5), (7, 77),
         (5, 10), (10, 1), (100, 50), (500, 100), (11, 99), (53, 33), (12, 100), (66, 500), (13, 5), (7, 77),
         (5, 10), (10, 1), (100, 50), (500, 100), (11, 99), (53, 33), (12, 100), (66, 500), (13, 5), (7, 77),]
max_weight = 100
filestr = 'proj1-ex2-output.txt'



def knapsack(max_weight, n):
	global items
	#initialize backing 2-d array with i, j indices
	table = [[0 for i in range(max_weight + 1)] for j in range(n)]
	#create dynamic programming 2-d array
	for i in range(0, n, 1):
		for j in range(0, max_weight + 1, 1):
			weight_i = (items[i])[0]
			value_i = (items[i])[1]
			#recurrence relation
			if (j - weight_i) >= 0:
				table[i][j] = max(table[i-1][j], value_i + table[i - 1][j - weight_i])
			elif (j - weight_i) < 0:
				table[i][j] = table[i-1][j]
	return table

def get_selection(table, max_weight, n):
	global items
	#initialize selection vector
	vector = [0 for x in range(n)]
	currweight = max_weight
	num = 0
	#walk up, if different, walk left, repeat
	for i in range(n-1, 0, -1):
		for j in range(currweight, 0, -1):
			if table[i][j] != table[i-1][j]:
				vector[num - i] = 1 
				currweight = currweight - (items[i - 1])[0]
				num = num + 1
				break
	return vector

#length of items list
n = len(items)

#call functions
data = knapsack(max_weight, n)
vector = get_selection(data, max_weight, n)
solution = data[n-1][max_weight]

#print solutions
maxstr = 'Max Value = ' + str(solution)
selvec = 'Selection Vector = ' + str(vector)
print(vector)
print(solution)
#write solutions to file
output = open(filestr, 'w')
output.write(maxstr + '\n' + selvec)
print(maxstr)
#print(selvec)
