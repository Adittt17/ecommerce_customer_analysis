import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
top_customers = pd.read_csv("dashboard/top_customers.csv")
customers_df = pd.read_csv("dashboard/customers_df.csv")

# Global setup
st.set_page_config(page_title="Customer Dashboard", layout="wide")
sns.set_style("whitegrid")

# --- Header ---
st.title("🛒 E-Commerce Customer Dashboard")
st.markdown(
    """
    Welcome to my first data analysis project, built with using Streamlit.  
    This dashboard highlights key insights from customer transaction data.
    """
)

# --- Top Customers Section ---
st.markdown("### Top Customers by Number of Orders")

col1, col2 = st.columns([2, 1])

with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(
        x='order_count',
        y='customer_unique_id',
        data=top_customers.sort_values(by="order_count", ascending=False),
        palette='viridis',
        ax=ax
    )
    ax.set_title('Top Customers by Order Count', fontsize=14)
    ax.set_xlabel('Order Count')
    ax.set_ylabel('Customer ID')
    st.pyplot(fig)

with col2:
    max_order = top_customers['order_count'].max()
    top_customer_id = top_customers.loc[top_customers['order_count'].idxmax(), 'customer_unique_id']
    avg_orders = round(top_customers['order_count'].mean(), 2)

    st.info(f"""
    **Top Customer ID:** `{top_customer_id}`  
    **Number of Orders:** {max_order}  
    **Average Orders per Customer:** {avg_orders}
    """)

# --- Top Cities Section ---
st.markdown("### Top Cities by Unique Customers")

# Aggregate city data
city_counts = customers_df.groupby("customer_city")['customer_id'].nunique().reset_index()
city_counts.columns = ['customer_city', 'unique_customers']
top_cities = city_counts.sort_values(by='unique_customers', ascending=False).head(5)

col3, col4 = st.columns([1, 2])

with col3:
    st.dataframe(top_cities, use_container_width=True)

    st.success(f"""
    The city with the most unique customers is **{top_cities.iloc[0,0]}**
    with **{top_cities.iloc[0,1]:,}** customers.
    """)

with col4:
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(
        y='customer_city',
        x='unique_customers',
        data=top_cities,
        palette='coolwarm',
        ax=ax2
    )
    ax2.set_title('Top 5 Cities with Most Unique Customers', fontsize=14)
    ax2.set_xlabel('Number of Unique Customers')
    ax2.set_ylabel('City')
    st.pyplot(fig2)

# --- Footer ---
st.markdown("---")
st.caption("Made by Adityo Pangestu · Built with Streamlit")
