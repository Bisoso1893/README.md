import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

# Encabezado de la aplicación
st.header('Cuadro de Mandos: Análisis de Vehículos Usados')

# Construir la ruta al archivo CSV desde la carpeta superior
csv_path = os.path.join(os.getcwd(), 'vehicles_us.csv')

# Leer los datos del archivo CSV
car_data = pd.read_csv(csv_path)

# Casillas de verificación para mostrar gráficos
build_histogram = st.checkbox('Mostrar histograma de odómetro')
build_scatter = st.checkbox('Mostrar dispersión entre odómetro y precio')

# Histograma
if build_histogram:
    st.write('Histograma de la columna "odometer"')
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig_hist, use_container_width=True)

# Diagrama de dispersión
if build_scatter:
    st.write('Dispersión entre "odometer" y "price"')
    fig_scatter = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers',
        marker=dict(color='orange', opacity=0.6)
    )])
    fig_scatter.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig_scatter, use_container_width=True)