import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run():
    # Membuat Title
    st.title('Exploratory Data Analysis (EDA)')

    # Membuat sub header
    st.subheader('EDA untuk Analisis Dataset Diabetes Prediction')

    # Membuat Garis Lurus
    st.markdown('---')
    
    # Show dataframe
    data = pd.read_csv('h8dsft_Milestone2P1_fadhilah_amani_alam_aulia.csv')
    st.dataframe(data)

    # Membuat BarPlot
    st.write('### Bar Plot Diabetes Patient')
    fig = plt.figure(figsize = (13,5))
    ax = sns.countplot(x='Outcome', data=data)
    ax.bar_label(ax.containers[0])
    st.pyplot(fig)

    # Membuat histogram berdasarkan input user
    st.write('### Grafik Histogram')
    opt = st.selectbox('Select Columns : ', ('Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[opt], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat scatter plot
    st.write('### Scatter Plot')
    fig = plt.figure(figsize=(15,5))
    sns.scatterplot(x='Glucose', y='Age', hue='Outcome', data=data, s=60, alpha=0.8)
    plt.title('Glucose vs Age')
    st.pyplot(fig)

    fig1 = plt.figure(figsize=(15,5))
    sns.scatterplot(x='BMI', y='Age', hue='Outcome', data=data, s=60, alpha=0.8)
    plt.title('BMI vs Age')
    st.pyplot(fig1)

if __name__ == '__main__':
    run()