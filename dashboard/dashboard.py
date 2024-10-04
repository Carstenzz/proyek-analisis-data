import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

#Mengambil data
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
 

 
# with col1:
#     total_orders = daily_orders_df.order_count.sum()
#     st.metric("Total orders", value=total_orders)
 
# with col2:
#     total_revenue = format_currency(daily_orders_df.revenue.sum(), "AUD", locale='es_CO') 
#     st.metric("Total Revenue", value=total_revenue)
 

mean = main_df.groupby('hr').agg({"casual":"mean", "registered":"mean", "cnt":"mean"}).reset_index()

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(mean['hr'], mean['cnt'], label='total', marker='o')
ax.plot(mean['hr'], mean['casual'], label='casual', marker='o', color='orange')
ax.plot(mean['hr'], mean['registered'], label='registered', marker='o', color='green')
ax.legend()
ax.grid(True)
 
st.pyplot(fig)

col1, col2 = st.columns(2)




st.title("") 

st.subheader('Bike uses during a season')


fig, ax = plt.subplots(figsize=(16, 8))
sns.scatterplot(data=main_df, x="dteday", y="cnt", hue="season", palette="coolwarm", s=50)
plt.xticks(rotation=45)
ax.legend()
ax.grid(True)
 
st.pyplot(fig)