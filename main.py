# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import json
import accessAPI as servicio


st.write('Predicción de Créditos Bancarios')

# Define the form fields
age = st.text_input('Age')
job = st.selectbox('Job', ['technician', 'unknown', 'blue-collar', 'admin.', 'housemaid', 'retired', 'services', 'entrepreneur', 'unemployed', 'management', 'self-employed', 'student'])
marital = st.selectbox('Marital', ['married', 'divorced', 'single', 'unknown'])
education = st.selectbox('Education', ['high.school', 'unknown', 'basic.9y', 'professional.course', 'university.degree', 'basic.4y', 'basic.6y', 'illiterate'])
default = st.selectbox('Default', ['no', 'unknown', 'yes'])
housing = st.selectbox('Housing', ['no', 'unknown', 'yes'])
loan = st.selectbox('Loan', ['no', 'unknown', 'yes'])
contact = st.selectbox('Contact', ['cellular', 'telephone'])
month = st.selectbox('Month', ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])
duration = st.text_input('Duration')
campaign = st.text_input('Campaign')
pdays = st.text_input('Pdays')
previous = st.text_input('Previous')
poutcome = st.selectbox('Poutcome', ['failure', 'nonexistent', 'success'])
emp_var_rate = st.text_input('Emp. Var. Rate')
cons_price_idx = st.text_input('Cons. Price. Idx')
cons_conf_idx = st.text_input('Cons. Conf. Idx')
euribor3m = st.text_input('Euribor3m')
nr_employed = st.text_input('Nr.employed')

form_fields = [age, duration, campaign, pdays, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed]
form_fieldsNames = ["Age", "Duration", "Campaign", "Pdays", "Emp. Var. Rate", "Cons. Price. Idx", "Cons. Conf. Idx", "Euribor3m", "Nr.employed"]


if st.button('Predict'):
    isValid = True
    for field, name in zip(form_fields, form_fieldsNames):
        try:
            float(field)
            isValid = True
        except ValueError:
            isValid = False
            st.warning(f'Please enter a valid number for {name}')

    if isValid:
        response = servicio.predict_loan_approval(age, job, marital, education, default, housing, loan, contact, month, duration, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed)
        result_dict = json.loads(response.decode("utf-8"))
        result = result_dict["Results"][0]
        if result == "yes":
            st.success("Usted puede recibir credito bancario")
        else:
            st.error("Usted no puede recibir credito bancario")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
