import numpy as np
import pandas as pd
import os
import pickle
movie = pd.read_csv('./u.item', sep='|', header=None, encoding='ISO-8859-1')
print(movie[1][:])
# movie = movie[:,1]
# print(movie[1])
# movie = [movie[0], movie[1]]
# print(movie)
# data = np.loadtxt(os.path.join('./cos', 'cos_movieid.txt'), dtype=np.int32)
# # # print(data)
# re = []
# for i in data:
#     print(i)
#     re1 = []
#     for j in i:
#         re1.append(movie[1][j-1])
#         print(j)
#     re.append(re1)
# print(re[0])
# pickle.dump(re, open(os.path.join('./cos', 'cos_movie.pkl'), 'wb'))
# np.savetxt(os.path.join('./cos', 'cos_movie.txt'), re, delimiter=',', fmt='%s')






