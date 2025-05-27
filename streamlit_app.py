import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"time": 0, "depth": 0, "pressure":1}
   ]
)


edited_df = st.data_editor(df, num_rows="dynamic")
