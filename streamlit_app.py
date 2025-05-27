import streamlit as st
import pandas as pd

df = pd.DataFrame(data=
    [
       {"time": 0, "depth": 0, "pressure":1}
   ]
)

st.data_editor(
    df, 
    column_config={
        "time": st.column_config.NumberColumn(
            "time (minutes)"
            help="how do you plan to take from the previous depth untill this one?"
            format="%d minutes"
        )
    }
    num_rows="dynamic",
