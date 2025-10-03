import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Título de la aplicación
st.title('Análisis de Datos de Vehículos Usados')

# Leer los datos del archivo CSV
car_data = pd.read_csv(r'C:\Users\ADMIN\Documents\TripleTen\Project 7\vehicles_us.csv')

# Mostrar una vista previa
st.subheader('Vista previa del conjunto de datos')
st.dataframe(car_data.head())

# Casilla de verificación para histograma
build_histogram = st.checkbox('Mostrar histograma del odómetro')

if build_histogram:
    st.subheader('Histograma del Odómetro')
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro', xaxis_title='Odómetro', yaxis_title='Frecuencia')
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión: Precio vs Odómetro')

if build_scatter:
    st.subheader('Gráfico de Dispersión')
    st.write('Creación de un gráfico de dispersión entre precio y odómetro')
    fig2 = go.Figure(data=go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers',
        marker=dict(color='royalblue', opacity=0.6)
    ))
    fig2.update_layout(title_text='Precio vs Odómetro', xaxis_title='Odómetro', yaxis_title='Precio')
    st.plotly_chart(fig2, use_container_width=True)
