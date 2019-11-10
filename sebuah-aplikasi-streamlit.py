#OG package
import streamlit as st

# Simulates Jupyter Notebook (?)
# from IPython import get_ipython

# Data Analysis
import pandas as pd
import numpy as np

# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns
# another way of saying "%matplotlib inline", because vanilla Python doesn't suppport % but IPython does.
# get_ipython().run_line_magic('matplotlib', 'inline')

#Prevent warnings
import warnings
warnings.simplefilter('ignore')

st.title('JUDI BOLA')

@st.cache
def load_data():
    data = pd.read_csv('EPL_Set.csv')
    return data

data_load_state = st.text('Loading data, mohon ditunggu...')
data = load_data()
data_load_state.text('Load data selesai!')

if st.checkbox('Tampilkan CSV'):
    st.subheader('Raw data')
    st.write(data)

data_1 = []
data_2 = []
data_3 = []
data_4 = []

for x in range(0,len(data)):
    if(data.iloc[x]['FTR'] == 'H'):
        data_1.append(data.iloc[x]['HomeTeam'])
    elif(data.iloc[x]['FTR'] == 'A'):
        data_2.append(data.iloc[x]['AwayTeam'])
    else:
        data_3.append(data.iloc[x]['HomeTeam'])
        data_4.append(data.iloc[x]['AwayTeam'])

df1 = pd.DataFrame({'H':data_1})
df2 = pd.DataFrame({'A':data_2})
df3 = pd.DataFrame({'HD':data_3,'AD':data_4})

st.subheader('Home Team')

data_home1 = pd.DataFrame(df1['H'].value_counts().head(10))
data_home1.plot(kind='pie',subplots=True,figsize=(8,8))
plt.pie(data_home1,labels=data_home1.index.values,autopct='%1.0f%%')

st.pyplot()

height = data_home1['H']
bars = data_home1.index.values
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(y_pos, bars)
plt.show()

st.pyplot()

st.subheader('Away Team')

data_home2 = pd.DataFrame(df2['A'].value_counts().head(10))
data_home2.plot(kind='pie',subplots=True,figsize=(8,8))
plt.pie(data_home2,labels=data_home2.index.values,autopct='%1.0f%%')

st.pyplot()

height = data_home2['A']
bars = data_home2.index.values
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(y_pos, bars)
plt.show()

st.pyplot()