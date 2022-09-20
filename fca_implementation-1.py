import pandas as pd
import numpy as np

from utils import clear_redondance, smooch, get_classes, create_table, simplify, switch
from concepts import concepts, clean_concepts, populate_table


# Initialize the table
C = {'Id': [1,2,3,4,5,6,7,8,9,10,11,12,13,14],
'Toux séche': [1,0,1,1,0,1,0,1,1,1,0,0,1,1],
'Tout grâce': [0,1,0,0,1,0,0,0,0,0,1,1,0,0],
'Géne respiratoire': [1,0,1,0,1,1,0,1,1,1,1,0,1,1],
'Sifflement':[1,1,0,0,0,0,0,1,0,0,1,0,0,1],
'Fièvre':[1,1,1,1,0,1,1,1,0,1,1,1,1,0],
'Maux de tête':[0,0,1,1,0,1,1,1,0,1,0,0,1,0],
'Perte de goût':[0,0,1,1,0,1,1,0,0,1,0,0,1,0],
'Courbature':[0,1,1,1,1,1,1,1,1,1,0,0,1,0],
'Dyspnée':[0,1,0,0,1,0,0,0,0,0,1,1,0,0],
'Asthme':[1,1,1,0,0,1,0,1,0,0,1,0,0,1],
'Bronchiolite':[1,0,0,0,0,1,0,1,1,1,1,0,0,0],
'BPCO':[0,1,0,0,1,0,0,0,0,0,1,1,0,0],
'COVID-19':[0,0,1,1,0,1,1,1,0,1,0,0,1,0],
}

df = pd.DataFrame(C)
attributs = df.iloc[ : ,1:10]
classes = df[['Asthme','Bronchiolite','BPCO','COVID-19']]


def make_KOMR(attributs, classes):
    array = np.zeros((14, attributs.shape[1]*classes.shape[1]))
    mushed_cols = ['séche-A', 'grâce-A', 'Géne-A', 'Sifflement-A','Fièvre-A','Maux-A','Perte-A','Courbature-A','Dyspnée-A', 
    				'séche-B', 'grâce-B', 'Géne-B', 'Sifflement-B','Fièvre-B','Maux-B','Perte-B','Courbature-B','Dyspnée-B',
    				'séche-P', 'grâce-P', 'Géne-P', 'Sifflement-P','Fièvre-P','Maux-P','Perte-P','Courbature-P','Dyspnée-P',
    				'séche-19', 'grâce-19', 'Géne-19', 'Sifflement-19','Fièvre-19','Maux-19','Perte-19','Courbature-19','Dyspnée-19']

    KOMR = pd.DataFrame(data = array, columns = mushed_cols)
    p = 0
    l = df.shape[0]
    for i in range(0, 14):
        p = 0
        for k in range(0,classes.shape[1]):
            for j in range(0, attributs.shape[1]):
                if attributs.iloc[i, j] & classes.iloc[i, k] == 1:
                    KOMR.loc[i, mushed_cols[p]] = 1
                    p +=1
                else:
                    p += 1
    id = {'Id': [1,2,3,4,5,6,7,8,9,10,11,12,13,14]}
    KOMR['Id'] = id['Id']
    first_column = KOMR.pop('Id')
    KOMR.insert(0, 'Id', first_column)
    return KOMR


KOMR = make_KOMR(attributs, classes)
test = []
for i in range(KOMR.shape[0]):
    for j in range(1, KOMR.shape[1]):
        if KOMR.iloc[i, j] == 1:
            t = (i+1, KOMR.columns[j])
            test.append(t)

fst = lambda x: x[0]
snd = lambda x: x[1]

print('\n','CREATION DES CONCEPTS FORMELS','\n')
FCs = concepts((set(list(map(fst, test))), set(list(map(snd, test))), test))
result = simplify(FCs)
for r in result:
    print(r)


#Nettoyage des concepts
print('\n','CONCEPTS APRES NETTOYAGE','\n')   
result_clean = clean_concepts(result)
for r in result_clean:
    print(r)

print('\n','CREATION DE LA TABLE D\'IMPORTANCE','\n')

attributs = ['Toux séche', 'Tout grâce', 'Géne respiratoire','Sifflement','Fièvre','Maux de tête',
            'Perte de goût','Courbature','Dyspnée']

classes = get_classes(result_clean)

table = create_table(attributs, classes)

importance_table = populate_table(table, result_clean)
print(importance_table)
