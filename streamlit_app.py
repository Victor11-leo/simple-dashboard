import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_excel(
    'data.xlsx',
    engine='openpyxl',
    sheet_name='New Data'    
)

# Profit by market and product
def profit_by_market():
    df2 = df[['Country','Profit','Product']]
    if country:
        df2 = df2.loc[df2['Country'].isin(country)]
    if product:
        df2 = df2.loc[df2['Product'].isin(product)]        
    profit_market = df2.groupby(by='Country' )['Profit'].sum()
    fig = px.bar(profit_market, title='Profit by market')
    return fig

def profit_by_product():
    df2 = df[['Product','Profit','Country']]
    if country:
        df2 = df2.loc[df2['Country'].isin(country)]
    if product:
        df2 = df2.loc[df2['Product'].isin(product)]   
    profit_market = df2.groupby(by='Product')['Profit'].sum()
    fig = px.bar(profit_market, title='Profit by product')
    return fig

def units_by_month():
    df2 = df[['Units Sold','Date','Product','Country']]
    if country:
        df2 = df2.loc[df2['Country'].isin(country)]
    if product:
        df2 = df2.loc[df2['Product'].isin(product)]   
    units_month = df2.groupby(by='Date')['Units Sold'].sum()
    fig = px.line(units_month, y='Units Sold', title='Units sold per month')
    return fig

def profit_by_month():
    df2 = df[['Profit','Date','Country','Product']]
    if country:
        df2 = df2.loc[df2['Country'].isin(country)]
    if product:
        df2 = df2.loc[df2['Product'].isin(product)]   
    units_month = df2.groupby(by='Date')['Profit'].sum()
    fig = px.line(units_month, y='Profit', title='Profit per month')
    return fig


# Streamlit now
st.set_page_config(
    page_title='Simple Dashboard', 
    page_icon=':bar_chart:', 
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items=None
    )
st.title(':bar_chart: Simpe dashboard')


# Sidebar
with st.sidebar:
    country_selections = (df['Country'].unique())
    product_selections = (df['Product'].unique())
    
    # st.write(country_selections)
    country = st.multiselect('Select your country',(country_selections))
    product = st.multiselect('Select your product',(product_selections))

col1,col2 = st.columns(2)

with col1:
    st.plotly_chart(profit_by_market())
    st.plotly_chart(profit_by_month())

with col2:
    st.plotly_chart(profit_by_product())
    st.plotly_chart(units_by_month())

# st.write(country)
# st.table(df.head())
# st.write(df.dtypes)

