import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import statsmodels.formula.api as smf
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

st.set_page_config(layout = "wide")

df = pd.read_csv('messy_data.csv', skipinitialspace=True)
df.replace({" " : np.nan}, inplace=True)

string_columns = ['clarity', 'color', 'cut']
df[string_columns] = df[string_columns].apply(lambda x: x.str.lower())

numeric_columns = ['carat', 'x dimension', 'y dimension', 'z dimension', 'depth', 'table', 'price']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

threshold_price = 100000
df = df[df['price'] <= threshold_price]

df = df.drop_duplicates()

df.fillna(df.mean(), inplace=True)


st.header("Data table")
if st.checkbox("Show/hide data"):
    st.dataframe(df)


st.header("Diamonds")

page = st.sidebar.selectbox('Select page',['Price data', 'Rozkład zmiennych numerycznych', 'Liczebność kategorii', 'Fitted Values vs. Original Values of Diamonds']) 


if page == 'Price data':
    vlist = ['carat', 'x dimension', 'y dimension', 'z dimension', 'depth', 'table']
    column = st.selectbox("Cena vs : ", vlist)
    fig = px.scatter(df, x=column, y='price', title=f'Cena vs {column}')
    st.plotly_chart(fig, use_container_width = True)

elif page == 'Rozkład zmiennych numerycznych':
    vlist = ['carat', 'x dimension', 'y dimension', 'z dimension', 'depth', 'table', 'price']
    column = st.selectbox("Rozkład zmiennych numerycznych dla : ", vlist)
    fig = px.histogram(df,
                       x=column,
                       title=f'Rozkład zmiennych numerycznych dla {column}'
                       )
    st.plotly_chart(fig, use_container_width = True)

elif page == 'Liczebność kategorii':
    vlist = ['clarity', 'color', 'cut']
    column = st.selectbox("Liczebność kategorii : ", vlist)
    category_counts = df[column].value_counts()

    fig = px.bar(df,
                       x=category_counts.index, y=category_counts,
                       title=f'Liczebność kategorii {column}',
                       labels={'x':column, 'y': 'Liczebność'}
                       )
    st.plotly_chart(fig, use_container_width = True)

elif page == 'Fitted Values vs. Original Values of Diamonds':
    df = df.rename(columns={'x dimension': 'x_dimension', 'y dimension': 'y_dimension', 'z dimension': 'z_dimension'})
    model = smf.ols(formula="price ~ carat + x_dimension + y_dimension + z_dimension + depth + table", data=df).fit()
    df["fitted"] = model.fittedvalues
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["price"], y=df["fitted"], mode='markers', name='Price'))
    fig.add_trace(go.Scatter(x=df["price"], y=df["price"], mode='lines', name='X vs Y Line'))
    fig.update_layout(title="Fitted Values vs. Original Values of Diamonds",
                  xaxis_title="Original Values of Diamonds",
                  yaxis_title="Fitted Values")
    st.plotly_chart(fig, use_container_width = True)

