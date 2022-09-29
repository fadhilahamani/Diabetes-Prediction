import streamlit as st
from streamlit_option_menu import option_menu 
from streamlit_lottie import st_lottie
import json
import requests
import eda
import prediction

# Membuat sidebar untuk navigasi
with st.sidebar:
    selected = option_menu('Menu',
                           ['Main Page',
                            'Exploratory Data Analysis (EDA)',
                            'Diabetes Prediction'],
                            icons = ['bookmark-check-fill','bar-chart-fill', 'activity'],
                            default_index = 0)

# Mengatur halaman
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_tbjuenb2.json")
if (selected == 'Main Page'):
    html_temp = """ 
    <div style ="background-color:#F1948A;padding:13px"> 
    <h1 style ="color:white;text-align:center;">Diabetes Detection</h1> 
    </div> 
    """
    #display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)
    st.write('*Made by: Fadhilah Amani*')
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            # Magic Syntax
            '''
            Diabetes adalah penyakit kronis yang ditandai dengan tingginya kadar gula darah.
            Glukosa merupakan sumber energi utama bagi sel tubuh manusia. 
            Akan tetapi, pada penderita diabetes, glukosa tersebut tidak dapat digunakan oleh tubuh.

            Machine Learning ini akan membantu untuk memprediksi apakah seseorang menderita diabetes atau tidak.
            '''
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")
elif (selected == 'Exploratory Data Analysis (EDA)'):
    eda.run()
else:
    prediction.run()