# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
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

# ——— 2. Convertimos a pandas ———
df1     = df1_snow.to_pandas()
df2_arr = df2_arr_snow.to_pandas()
df2_dep = df2_dep_snow.to_pandas()
df3_arr = df3_arr_snow.to_pandas()
df3_dep = df3_dep_snow.to_pandas()

# (Opcional) chequeá dtypes y un preview:
st.subheader("Preview de datos")
st.write("df1:", df1.dtypes.to_dict())
st.dataframe(df1.head(), use_container_width=True)

# ——— 3. Preparamos el índice para que st.bar_chart lo use como eje X ———
df1.set_index("estacion", inplace=True)
df2_arr.set_index("sector", inplace=True)
df2_dep.set_index("sector", inplace=True)

# ——— 4. Reporte 1: viajes por estación ———
st.subheader("Reporte 1 – Cantidad de viajes por estación")
# IMPORTANTE: usamos la serie con nombre, no df.iloc[:,0] que a veces trae name=None
st.bar_chart(df1["viajes"])

# ——— 5. Reporte 2: llegadas y salidas por sector ———
st.subheader("Reporte 2 – Llegadas por sector")
st.bar_chart(df2_arr["llegadas"])

st.subheader("Reporte 2 – Salidas por sector")
st.bar_chart(df2_dep["salidas"])

# ——— 6. Reporte 3: comparativo en Marylebone ———
st.subheader("Reporte 3 – Llegadas vs Salidas en Marylebone")
# Creamos un DataFrame con índice y una sola columna 'cantidad'
df_mary = pd.DataFrame({
    "cantidad": [
        df3_arr["llegadas"].sum(),
        df3_dep["salidas"].sum()
    ]
}, index=["Llegadas", "Salidas"])
st.bar_chart(df_mary)
