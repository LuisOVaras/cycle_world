# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
import seaborn as sns
import matplotlib.pyplot as plt
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
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=df1, x="estacion", y="viajes", ax=ax)
ax.set_title("Cantidad de viajes por estación")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
st.pyplot(fig)
