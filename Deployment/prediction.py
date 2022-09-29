import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

def run():
  # Load Model
  with open('model.pkl', 'rb') as file_1:
    model = joblib.load(file_1) 

  # Membuat Title
  st.title('Diabetes Prediction')

  # Membuat sub header
  st.subheader('Form untuk Memprediksi Diabetes')
  st.markdown('---')

  # Membuat form
  with st.form(key='form_paramters'):
      name = st.text_input('Name').capitalize()
      age = st.number_input('Age', min_value=21, max_value=81, value=21)
      pregnancies = st.number_input('Pregnancies', min_value=0, max_value=17, value=0)
      glucose = st.number_input('Glucose', min_value=20, max_value=200, value=20)
      blood = st.number_input('BloodPressure', min_value=20, max_value=200, value=20)
      skin = st.number_input('SkinThickness', min_value=10, max_value=200, value=10)
      insulin = st.number_input('Insulin', min_value=10, max_value=850, value=10)
      bmi = st.number_input('BMI', min_value=10.0, max_value=70.0, value=10.0, format="%.1f")
      diabetes = st.number_input('DiabetesPedigreeFunction', min_value=0.0, max_value=3.0, value=0.0, format="%.3f")
      st.markdown('---')
          
      submitted = st.form_submit_button('Get Result')

      data_inf = {
          'Pregnancies': pregnancies,
          'Glucose': glucose,
          'BloodPressure': blood,
          'SkinThickness': skin,
          'Insulin': insulin,
          'BMI': bmi,
          'DiabetesPedigreeFunction': diabetes,
          'Age': age
      }

      st.write('Berikut ini merupakan data yang Anda submit:')

      data_inf = pd.DataFrame([data_inf])
      st.dataframe(data_inf)

      if submitted:
          y_pred_inf = model.predict(data_inf)
          if(y_pred_inf==1):
            st.write(name,', Anda terdiagnosis mengidap diabetes. Silahkan kunjungi dokter sesegera mungkin, untuk pemeriksaan lebih lanjut.')
          else:
            st.write(name,', Selamat! Anda tidak mengidap diabetes. Jaga terus kesehatan Anda')

if __name__ == '__main__':
    run()