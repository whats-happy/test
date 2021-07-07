import numpy as np
import pandas as pd
from math import sqrt
import os
f = pd.read_csv('./u.data', sep='\t', header=None, encoding='gbk')
f = np.array(f)
user_item = f[:, 0:3]

print("正在构造用户-物品评分矩阵")
user_matrix = np.zeros([943, 1682])
for i in user_item:
    user_matrix[i[0]-1, i[1]-1] = i[-1]

user_dict = dict()
def addtwodimdict(thedict, key_a, key_b, val):
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a: {key_b: val}})

for i in user_item:
    addtwodimdict(user_dict, i[0], i[1], i[2])
# user_dict
print("用户-物品评分矩阵构造完成")
print("正在计算用户相似度")
w = dict()
for u in user_dict.keys():
    w.setdefault(u, {})
    for v in user_dict.keys():
        if u == v:
            continue
        u_set = set([key for key in user_dict[u].keys() if user_dict[u][key] > 0])
        v_set = set([key for key in user_dict[v].keys() if user_dict[v][key] > 0])
        w[u][v] = float(len(u_set & v_set)) / sqrt(len(u_set)*len(v_set))
print("用户相似度计算完成")

# usera = input("请输入想推荐的用户ID:")
all_movieid=[]
for usera in range(1, 944):
    usera = int(usera)
    a = sorted(w[usera].items(), key=lambda d: d[1], reverse=False)#按字典value进行升序排序，并返回排序后的列表
    sid = {}
    sim = {}
    for i in range(5):
        a[i] = np.array(a[-(i+1)])
    for i in range(5):
        sid[i] = a[i][0]
        sim[i] = a[i][-1]
    #     print(sid[i])

    re_all = dict()
    for user_id in sid.values():
    #     for i in user_dict[user_id].keys():
        b = sorted(user_dict[user_id].items(), key=lambda d:d[1],reverse=False)
        # new_user1 = dict()
        list1 = []
        list2 = []
        for i in range(10):
            b[i] = (b[-(i+1)])
            list1.append(b[i][0])
            list2.append(b[i][1])
        # new_user1 = dict(zip(list1, list2))
        # list1, list2, new_user1
        # new_user1.values(-1)
        list3=[]
        for v in list2:
            list3.append(sim[0] * v)
        new_user1 = dict(zip(list1, list3))
        recommend_movieid = []
        for movieid in new_user1.keys():
        #     print(movieid)
            for j in user_dict[usera].keys():
                if movieid != j:
                    recommend_movieid.append(movieid)
                elif movieid == j:
                    pass
                elif recommend_movieid.shape == 5:
                    break
        last = []
        for i in recommend_movieid:
            if i not in last:
                last.append(i)
            elif i in last:
                continue
        # print(recommend_movieid)
        for i in new_user1.keys():
            if i in last:
                continue
            elif i not in last:
                new_user1.pop(i)
        re_all.update(new_user1)
    # re_all
    re_last_movieid = []
    re_last = sorted(re_all.items(), key=lambda d:d[1],reverse=False)
    for i in range(5):
        re_last[i] = re_last[-(i+1)]
        re_last_movieid.append(re_last[i][0])
    print(re_last_movieid)
    all_movieid.append(re_last_movieid)
print(all_movieid)
np.savetxt(os.path.join('./cos', 'cos_movieid.txt'), all_movieid, fmt='%f')