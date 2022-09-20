def clear_redondance(myList):
	resultantList = []
	for element in myList:
		if element not in resultantList :
			resultantList.append(element)

	return resultantList

def sort_list(myList):
	myList.sort()
	return myList

def smooch(myList):
	smooched_list = '-'.join(myList)

	return smooched_list

def get_classes(result):
	classes = []
	for i in result:
		smooched = smooch(i[2])
		classes.append(smooched)

	return clear_redondance(classes)

def create_table(attributs, classes):
	empty = np.zeros((len(attributs), len(classes)))
	table = pd.DataFrame(data = empty, columns = classes, index = attributs)
	
	return table

def switch(x):
    if x == "A":
        return "Asthme"
    elif x == "P":
        return "BPCO"
    elif x == "B":
        return "Bronchiolite"
    elif x == "19":
        return "COVID-19"
    elif x == "séche":
        return "Toux séche"
    elif x == "grâce":
        return "Tout grâce"
    elif x == "Géne":
        return "Géne respiratoire"
    elif x == "Maux":
        return "Maux de tête"
    elif x == "Perte":
        return "Perte"
    else:
        return x


def simplify(FCs):
    result = []
    for i in range(len(FCs)):
      s = list(FCs[i][1])
      cls ,atr = [], []
      for j in range(len(s)):
        k = s[j].split('-')
        k_0, k_1 = switch(k[0]), switch(k[1])
        atr.append(k_0)
        cls.append(k_1)
      final_atr = list(dict.fromkeys(atr))
      final_cls = list(dict.fromkeys(cls))
      print((FCs[i][0], final_atr, final_cls))
      result.append('\n')
      result.append((FCs[i][0], final_atr, final_cls))
      
    return result