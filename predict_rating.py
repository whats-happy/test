import numpy as np
import pandas as pd
from math import sqrt
import os
f = pd.read_csv('./u.data', sep='\t', header=None, encoding='gbk')
f = np.array(f)


user_item = f[:, 0:3]


user_matrix = np.zeros([943, 1682])
# user_matrix
for i in user_item:
#     print(i)
    user_matrix[i[0]-1,i[1]-1] = i[-1]


user_dict = dict()
movie_dict = dict()
def addtwodimdict(thedict, key_a, key_b, val):
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})

for i in user_item:
    addtwodimdict(user_dict, i[0], i[1], i[2])

for i in user_item:
    addtwodimdict(movie_dict, i[1], i[0], i[2])
w = dict()

for u in user_dict.keys():
    w.setdefault(u,{})
    for v in user_dict.keys():
        if u == v:
            continue
        u_set = set([key for key in user_dict[u].keys() if user_dict[u][key] > 0])
        v_set = set([key for key in user_dict[v].keys() if user_dict[v][key] > 0])
        w[u][v] = float(len(u_set & v_set)) / sqrt(len(u_set)*len(v_set))
all_rating = user_matrix
for i in range(1, 944):
    for j in range(1, 1683):
        if all_rating[i - 1][j - 1] != 0:
            continue
        elif all_rating[i - 1][j - 1] == 0:
            rating = 0
            t = 0
            for k in movie_dict[j]:
                if k == i:
                    continue
                else:
                    t += 1
                    rating += w[i][k] * user_dict[k][j]
                    all_rating[i - 1][j - 1] = ((rating / t) * 5)
                    if all_rating[i - 1][j - 1] >= 5:
                        all_rating[i - 1][j - 1] = 5
                    else:
                        all_rating[i - 1][j - 1] = all_rating[i - 1][j - 1]

np.savetxt(os.path.join('./cos', 'cos_predict_rating.txt'), all_rating, fmt='%f')
