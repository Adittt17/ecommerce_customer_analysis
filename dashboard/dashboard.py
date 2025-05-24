import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime

# Load data
top_customers = pd.read_csv("dashboard/top_customers.csv")
customers_df = pd.read_csv("dashboard/customers_df.csv")

# Title and Introduction
st.title('Dicoding Data Analysis Project')

st.write(
    """
    Hello everyone 👋  
    My name is Adityo Pangestu.  
    This is my first project in data analysis.
    """
)

# Top Customers by Order Count
st.header('Top Customers by Order Count')

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='order_count', y='customer_unique_id', data=top_customers, palette='viridis', ax=ax)
ax.set_title('Top Customers by Order Count', fontsize=16)
ax.set_xlabel('Number of Orders', fontsize=12)
ax.set_ylabel('Customer ID', fontsize=12)
st.pyplot(fig)

# Top Cities by Number of Unique Customers
st.header('Top Cities by Number of Unique Customers')

customer_city_counts = customers_df.groupby(by="customer_city").agg({
    "customer_id": "nunique"  
}).reset_index()

customer_city_counts.columns = ['customer_city', 'unique_customers']
customer_city_counts = customer_city_counts.sort_values(by='unique_customers', ascending=False)
top_5_cities = customer_city_counts.head(5)

st.write(top_5_cities)

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(top_5_cities['customer_city'], top_5_cities['unique_customers'], color='#FF5733')
ax.set_title('Top 5 Cities with Most Unique Customers', fontsize=16)
ax.set_xlabel('Number of Unique Customers', fontsize=14)
ax.set_ylabel('City', fontsize=14)

st.pyplot(fig)

st.write("The chart of the top 5 cities has been displayed.")
