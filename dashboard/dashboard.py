import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime


top_customers = pd.read_csv("dashboard/top_customers.csv")
customers_df = pd.read_csv("dashboard/customers_df.csv")

st.title('Proyek Dicoding Analisis Data')

st.write(
    """
    Halo Semuanya.
    Perkenalkan nama saya Adityo Pangestu.
    Ini adalah proyek pertama saya dalam analisis data.
    """
)

st.header('Pelanggan dengan Pembelian Terbanyak')

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='order_count', y='customer_unique_id', data=top_customers, palette='viridis', ax=ax)
ax.set_title('Pelanggan dengan Pembelian Terbanyak', fontsize=16)
ax.set_xlabel('Jumlah Pesanan', fontsize=12)
ax.set_ylabel('ID Pelanggan', fontsize=12)
st.pyplot(fig)



st.header('Daftar asal kota pelanggan paling banyak')


customer_city_counts = customers_df.groupby(by="customer_city").agg({
    "customer_id": "nunique"  
}).reset_index()

customer_city_counts.columns = ['customer_city', 'unique_customers']

customer_city_counts = customer_city_counts.sort_values(by='unique_customers', ascending=False)

top_5_cities = customer_city_counts.head(5)

st.write(top_5_cities)

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(top_5_cities['customer_city'], top_5_cities['unique_customers'], color='#FF5733')

ax.set_title('5 Kota dengan Jumlah Pelanggan Unik Terbanyak', fontsize=16)
ax.set_xlabel('Jumlah Pelanggan Unik', fontsize=14)
ax.set_ylabel('Kota', fontsize=14)

st.pyplot(fig)

st.write("Grafik 5 kota teratas sudah ditampilkan.")


