import math
import numpy as np
import pandas as pd
class UserCF:
    def __init__(self):
        self.user_score_dict = self.initUserScore()
        self.users_sim = self.userSimilarity()

    def initUserScore(self):
        f = pd.read_csv('./u.data', sep='\t', header=None)
        f = np.array(f)
        user_item = f[:, 0:3]
        user_score_dict = dict()

        def addtwodimdict(thedict, key_a, key_b, val):
            if key_a in thedict:
                thedict[key_a].update({key_b: val})
            else:
                thedict.update({key_a: {key_b: val}})

        for i in user_item:
            addtwodimdict(user_score_dict, i[0], i[1], i[2])
        # user_score_dict = {
        #     "A": {"a": 3.0, "b": 4.0, "c": 0.0, "d": 3.5, "e": 0.0},
        #     "B": {"a": 4.0, "b": 0.0, "c": 4.5, "d": 0.0, "e": 3.5},
        #     "C": {"a": 0.0, "b": 3.5, "c": 0.0, "d": 0.0, "e": 3.0},
        #     "D": {"a": 0.0, "b": 4.0, "c": 0.0, "d": 3.5, "e": 3.0},
        # }
        return user_score_dict

    def userSimilarity(self):
        W = dict()
        for u in self.user_score_dict.keys():
            W.setdefault(u, {})
            for v in self.user_score_dict.keys():
                if u == v:
                    continue
                u_set = set([key for key in self.user_score_dict[u].keys() if self.user_score_dict[u][key] > 0])
                v_set = set([key for key in self.user_score_dict[v].keys() if self.user_score_dict[v][key] > 0])
                W[u][v] = float(len(u_set & v_set)) / math.sqrt(len(u_set)*len(v_set))
        return W

    def preUserItemScore(self, userA, item):
        score = 0.0
        for user in self.users_sim[userA].keys():
            if user != userA:
                score += self.users_sim[userA][user] * self.user_score_dict[user][item]
        return score
    def recommend(self, userA):
        user_item_score_dict = dict()
        for item in self.user_score_dict[userA].keys():
            if self.user_score_dict[userA][item] <= 0:
                user_item_score_dict[item] = self.preUserItemScore(userA, item)
        return user_item_score_dict

if __name__ == "__main__":
    ub = UserCF()
    print(ub.recommend(12))





