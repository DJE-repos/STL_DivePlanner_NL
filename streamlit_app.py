import streamlit as st
import pandas as pd

df = pd.DataFrame(data=
    [
       {"time": 0, "depth": 0, "pressure":1,"calculation":"diepte*tijd*verbruik=","air_used":0 }
   ]
)

st.data_editor(
    df, 
    column_config={
        "time": st.column_config.NumberColumn(
            "tijd (minuten)",
            help="how do you plan to take from the previous depth untill this one?",
            format="%d min"
        ),
        "depth": st.column_config.NumberColumn(
            "diepte (m)",
            help="what depth do you plan to go to?",
            format="%d m"
        ),
        
        "pressure": st.column_config.NumberColumn(
            "druk (bar) (calculated)",
            help="difference in pressure (bar)",
            format="%.1f bar",
            disabled=True
        ),
        "calculation": st.column_config.TextColumn(
            "berekening"
            default="diepte*tijd*verbruik="
            disabled=True
        )
            
    },
    num_rows="dynamic",
    )
