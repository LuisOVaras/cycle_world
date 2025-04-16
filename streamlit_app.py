# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
import matplotlib.pyplot as plt
import pandas as pd
# Write directly to the app
st.title(f"Analisis 📊 Cycle World")
st.write(
  """
  """
)

cnx = st.connection("snowflake")
session = cnx.session()

df_1 = session.table("CYCLE_WORLD.PUBLIC.REPORT_1")
#st.dataframe(data=df_1, use_container_width=True)

# 
df_2_llegada = session.table("CYCLE_WORLD.PUBLIC.REPORT_2_LLEGADA")
#st.dataframe(data=df_2_llegada, use_container_width=True)
# 
df_2_salida = session.table("CYCLE_WORLD.PUBLIC.REPORT_2_SALIDA")
#st.dataframe(data=df_2_salida, use_container_width=True)

# 
df_3_llegada_marylebone = session.table("CYCLE_WORLD.PUBLIC.REPORT_2_LLEGADA").filter(col("sector") == ' Marylebone')
#st.dataframe(data=df_3_llegada_marylebone, use_container_width=True)

df_3_salida_marylebone = session.table("CYCLE_WORLD.PUBLIC.REPORT_2_SALIDA").filter(col("sector") == ' Marylebone')
#st.dataframe(data=df_3_salida_marylebone, use_container_width=True)

# Convertir a pandas DataFrame
df1 = df_1.to_pandas()
df2_llegada = df_2_llegada.to_pandas()
df2_salida = df_2_salida.to_pandas()
df3_llegada_marylebone = df_3_llegada_marylebone.to_pandas()
df3_salida_marylebone = df_3_salida_marylebone.to_pandas()

# Reporte 1: Viajes por estación
st.subheader("Reporte 1 – Cantidad de viajes por estación")


fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(df1["STATION_NAME"], df1["UNIQUE_JOURNEY_ID"], color='steelblue')
ax.set_title("Cantidad de viajes por estación", fontsize=16)
ax.set_xlabel("STATION_NAME")
ax.set_ylabel("UNIQUE_JOURNEY_ID")
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)
