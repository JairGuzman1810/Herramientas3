# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff

df = px.data.gapminder()
st.dataframe(df)
listPaises = df["country"].unique().tolist()
st.write(listPaises)
# fig = px.bar(data_canada, x='year', y='pop')
# fig.show()
option = "Canada"
with st.sidebar:
    st.write("HOLA MUNDO")
    option = st.selectbox(
        'Paises',
        listPaises)
    st.write(option)

datosPais = df.query("country == '"+option+"'")
fig = px.bar(datosPais, x="year", y="pop")
st.plotly_chart(fig, use_container_width=True)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    st.header("Hola desde Streamlit")
    st.subheader("1...2...3...dudududud")
    st.write("EXPLOTANDO")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
