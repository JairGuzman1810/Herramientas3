# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import json
import accessAPI as servicio
import pandas as pd

df = pd.read_csv("Herramientas3_2023_banco.csv")

st.title('Predicción de Créditos Bancarios')
st.write('Realizado por: Jair Francisco Guzman Hernandez')


# Define the form fields
age = st.text_input('Age')
job = st.selectbox('Job', df['job'].unique().tolist())
marital = st.selectbox('Marital', df['marital'].unique().tolist())
education = st.selectbox('Education', df['education'].unique().tolist())
default = st.selectbox('Default', df['default'].unique().tolist())
housing = st.selectbox('Housing', df['housing'].unique().tolist())
loan = st.selectbox('Loan', df['loan'].unique().tolist())
contact = st.selectbox('Contact', df['contact'].unique().tolist())
month = st.selectbox('Month', ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])
day_of_week = st.selectbox('Day of Week', df['day_of_week'].unique().tolist())
poutcome = st.selectbox('Poutcome', df['poutcome'].unique().tolist())

duration = st.text_input('Duration')
pdays = st.text_input('Pdays')
nr_employed = st.text_input('Nr.employed')

previous = st.slider(min_value=min(df['previous'].unique().tolist()), max_value=max(df['previous'].unique().tolist()), label="Previous")
emp_var_rate = st.slider(min_value=min(df['emp.var.rate'].unique().tolist()), max_value=max(df['emp.var.rate'].unique().tolist()), label="Emp. Var. Rate")
cons_price_idx = st.slider(min_value=min(df['cons.price.idx'].unique().tolist()), max_value=max(df['cons.price.idx'].unique().tolist()), label="Cons. Price. Idx")
cons_conf_idx = st.slider(min_value=min(df['cons.conf.idx'].unique().tolist()), max_value=max(df['cons.conf.idx'].unique().tolist()), label="Cons. Conf. Idx")
euribor3m = st.slider(min_value=min(df['euribor3m'].unique().tolist()), max_value=max(df['euribor3m'].unique().tolist()), label="Euribor3m")
campaign = st.slider(min_value=min(df['campaign'].unique().tolist()), max_value=max(df['campaign'].unique().tolist()), label="Campaign")


form_fields = [age, duration, campaign, pdays, nr_employed]
form_fieldsNames = ["Age", "Duration", "Campaign", "Nr.employed"]


if st.button('Predecir'):
    isValid = True
    for field, name in zip(form_fields, form_fieldsNames):
        try:
            float(field)
            isValid = True
        except ValueError:
            isValid = False
            st.warning(f'Ingresa un numero valido para {name}')

    if isValid:
        response = servicio.predict_loan_approval(age, job, marital, education, default, housing, loan, contact, month, duration, day_of_week, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed)
        result_dict = json.loads(response.decode("utf-8"))
        result = result_dict["Results"][0]
        if result == "yes":
            st.success("Usted puede recibir credito bancario")
        else:
            st.error("Usted no puede recibir credito bancario")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
