import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os

st.header('基于数据库movielens-100k的电影推荐系统')
data = pickle.load(open(os.path.join('./cos', 'cos_movie.pkl'), 'rb'))
rating = np.loadtxt('./cos/cos_predict_rating.txt', dtype=np.float32)
user = pd.read_csv('./u.user', sep='|', header=None, encoding='gbk')
user = np.array(user)
user = user[:, 0:4]
option0 = st.selectbox('请选择用户ID以查看用户信息（用户ID范围为1-943）', range(1, 944))
st.write('用户   ID    年龄    性别(F:女 M:男)     职业   ', user[:][option0 - 1: option0])
movie = pd.read_csv('./test_python/u.item', sep='|', header=None, encoding='ISO-8859-1')
movie = np.array(movie)
movie = movie[:, 0:3]
option1 = st.selectbox('请选择电影ID以查看电影信息（电影ID范围为1-1682）', range(1, 1683))
st.write('电影  ID  电影名 电影上映日期 ', movie[:][option1-1:option1])

select = st.radio('请选择功能', ('为用户推荐电影', '预测用户对电影的评分'))
if select == '为用户推荐电影':
    userid = st.selectbox('请选择你想推荐的用户ID', (range(1, 944)))
    userid = int(userid)
    st.write('为该用户推荐以下5部电影:', data[userid - 1])
elif select == '预测用户对电影的评分':
    userid = st.selectbox('请选择你想预测的用户ID', (range(1, 944)))
    userid = int(userid)
    movieid = st.selectbox('请选择你想预测的电影ID', (range(1, 1683)))
    movieid = int(movieid)
    st.write('该用户对该电影的评分为:', rating[userid - 1][movieid - 1])
