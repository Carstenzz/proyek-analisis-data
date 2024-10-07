import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

#Mengambil data
try:
    main_data = pd.read_csv('dashboard/main_data.csv')   
except:
    main_data = pd.read_csv('main_data.csv') 

#mengubah objek menjadi datetime
main_data['dteday'] = pd.to_datetime(main_data['dteday'])


min_date = main_data["dteday"].min()
max_date = main_data["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = main_data[(main_data["dteday"] >= str(start_date)) & 
                (main_data["dteday"] <= str(end_date))]




st.title('Bike Sharing Dataset')
st.text("Nama: Carstenz Meru Phantara")
st.text("Email: carstenzmp@gmail.com")
st.text("id: carstenz")



st.title("") 


st.subheader('Average bike uses')
 

mean = main_df.groupby('hr').agg({"casual":"mean", "registered":"mean", "cnt":"mean"}).reset_index()

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(mean['hr'], mean['cnt'], label='total', marker='o')
ax.plot(mean['hr'], mean['casual'], label='casual', marker='o', color='orange')
ax.plot(mean['hr'], mean['registered'], label='registered', marker='o', color='green')
ax.legend()
ax.grid(True)
 
st.pyplot(fig)

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Casual user")
    st.text("max : " + str(round(main_df.groupby('hr')['casual'].mean().max(),2)))
    st.text("min : " + str(round(main_df.groupby('hr')['casual'].mean().min(),2)))
    st.text("avg : " + str(round(main_df.groupby('hr')['casual'].mean().mean(),2)))

with col2:
    st.subheader("Registered user")
    st.text("max : " + str(round(main_df.groupby('hr')['registered'].mean().max(),2)))
    st.text("min : " + str(round(main_df.groupby('hr')['registered'].mean().min(),2)))
    st.text("avg : " + str(round(main_df.groupby('hr')['registered'].mean().mean(),2)))

with col3:
    st.subheader("Total user")
    st.text("max : " + str(round(main_df.groupby('hr')['cnt'].mean().max(),2)))
    st.text("min : " + str(round(main_df.groupby('hr')['cnt'].mean().min(),2)))
    st.text("avg : " + str(round(main_df.groupby('hr')['cnt'].mean().mean(),2)))




st.title("") 

st.subheader('Bike uses during a season')


fig, ax = plt.subplots(figsize=(16, 8))
sns.scatterplot(data=main_df, x="dteday", y="cnt", hue="season", palette="coolwarm", s=50)
plt.xticks(rotation=45)
ax.legend()
ax.grid(True)
 
st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Spring season")
    st.text("max : " + str(round(main_df[main_df['season'] == 1]['cnt'].max(),2)))
    st.text("avg : " + str(round(main_df[main_df['season'] == 1]['cnt'].mean(),2)))

    st.subheader("")
    st.subheader("Fall season")
    st.text("max : " + str(round(main_df[main_df['season'] == 3]['cnt'].max(),2)))
    st.text("avg : " + str(round(main_df[main_df['season'] == 3]['cnt'].mean(),2)))

with col2:
    st.subheader("Summer season")
    st.text("max : " + str(round(main_df[main_df['season'] == 2]['cnt'].max(),2)))
    st.text("avg : " + str(round(main_df[main_df['season'] == 2]['cnt'].mean(),2)))

    st.subheader("")
    st.subheader("Winter season")
    st.text("max : " + str(round(main_df[main_df['season'] == 4]['cnt'].max(),2)))
    st.text("avg : " + str(round(main_df[main_df['season'] == 4]['cnt'].mean(),2)))
