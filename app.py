import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data(1990) by Xuanqi Zhang')
df = pd.read_csv('housing.csv')

price_filter = st.slider('Minimal Median House Price:', 0.0, 500001.0, 200000.0)

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

income_level=st.sidebar.radio(
    'Select income level:',
    ('Low','Medium','High')
)

st.title('See more filters in the sidebar:')

if income_level=='Low':
    df=df[df['median_income']<=2.5]
elif income_level=='Medium':
    df=df[(df['median_income']>2.5)  &  (df['median_income']<4.5)]
else:
    df=df[df['median_income']>4.5]

df = df[df.median_house_value >= price_filter]

df = df[df.ocean_proximity.isin(location_filter)]

# show on map
st.map(df)

# show the plot
st.subheader('Histogram of The Median House Value')
fig, ax = plt.subplots()
plt.hist(df['median_house_value'], bins=30, edgecolor='none')
st.pyplot(fig)