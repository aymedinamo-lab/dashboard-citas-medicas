import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el dataset generado previamente
df = pd.read_csv('citas_medicas.csv')

# Título del Dashboard
st.title('Dashboard de Gestión de Citas Médicas')

# Sección 1: Citas por Especialidad
st.subheader('Citas por Especialidad')
fig1 = px.bar(
    df['especialidad'].value_counts().reset_index(),
    x='especialidad',
    y='count',
    labels={'especialidad': 'Especialidad', 'count': 'Cantidad de Citas'},
    title='Total de Citas por Especialidad Médica'
)
st.plotly_chart(fig1)

# Sección 2: Estado de las Citas
st.subheader('Estado de las Citas')
fig2 = px.pie(
    df,
    names='estado',
    title='Distribución del Estado de las Citas'
)
st.plotly_chart(fig2)

# Procesamiento de fechas para la evolución mensual
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.month
citas_mes = df.groupby('mes').size().reset_index(name='cantidad')

# Sección 3: Citas por Mes
st.subheader('Evolución Mensual de Citas')
fig3 = px.line(
    citas_mes,
    x='mes',
    y='cantidad',
    markers=True,
    title='Tendencia Mensual de Citas Médicas',
    labels={'mes': 'Mes del Año', 'cantidad': 'Número de Citas'}
)
st.plotly_chart(fig3)
