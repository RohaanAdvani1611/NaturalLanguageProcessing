# Extract Rules Dictionary from Grammar of following forms(NT -> NT | NT or NT -> T)
def extractRules(tmp):
    R, nt = {}, []
    sent = tmp[len(tmp)-1].split()
    tmp = tmp[0:len(tmp)-1]
    for i in range(len(tmp)):
        tmp[i] = tmp[i].strip()
        tmp[i] = tmp[i].replace(" ", "")
        tmp[i] = tmp[i].split('->')
        for j in range(len(tmp[i])):
            x = []
            if j == 1 and '|' in tmp[i][j]:
                tmp[i][j] = tmp[i][j].split('|')
            elif j == 1 and '|' not in tmp[i][j]:
                x.append(tmp[i][j])
                tmp[i][j] = x
    for i in tmp:
        if i not in nt:
            nt.append(i[0])
    nt = list(set(nt))
    for i in nt:
        tmp3 = []
        for j in tmp:
            if i == j[0]:
                tmp3.append(j[1])
        R[i] = tmp3
    return R, sent
    
def cykParse(w, R):
	n = len(w)
	# Create Table
	T = [[set([]) for j in range(n)] for i in range(n)]
	# Fill Table
	for j in range(0, n):
		for lhs, rule in R.items():
			for rhs in rule:
			    # If Terminal Found
				if len(rhs) == 1 and rhs[0] == w[j]:
					T[j][j].add(lhs)
		for i in range(j, -1, -1):
			for k in range(i, j + 1):	
				for lhs, rule in R.items():
					for rhs in rule:
						if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]:
							T[i][j].add(lhs)
	f1 = open("111903151_Assgn6_Output_CKY.txt", "w+")
	for i in T:
	    print(i)
	    x = str(i) + '\n'
	    f1.write(x)
	if len(T[0][n-1]) != 0:
		f1.write("Sentence belongs to the language generated by the grammar")
	else:
		f1.write("Sentence does not belong to the language generated by the grammar")
	f1.close()

tmp = []
with open('111903151_Assgn6_Input_CKY.txt') as f:
    [tmp.append(line) for line in f.readlines()]
R, sent = extractRules(tmp)
print(R)
print(sent)
cykParse(sent, R)
