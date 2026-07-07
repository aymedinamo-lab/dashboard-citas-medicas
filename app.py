import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Analítico - Riesgo de Morosidad Bancaria")
df=pd.read_excel("dataset_personal_7003116552.xlsx")
st.metric("Tasa de Morosidad", f"{df['moroso'].mean()*100:.2f}%")
fig,ax=plt.subplots()
df['empleo_estable'].value_counts().plot(kind='bar',ax=ax)
st.pyplot(fig)
fig2,ax2=plt.subplots()
ax2.hist(df['ingreso_mensual'],bins=20)
st.pyplot(fig2)
