import streamlit as st
import pandas as pd

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(data=
        [
           {"time": 0, "depth": 0, "pressure":1,"calculation":"diepte*tijd*verbruik=","air_used":0 }
       ]
    )
   
edited_df=st.data_editor(
df, 
column_config={
    "time": st.column_config.NumberColumn(
        "tijd (minuten)",
        help="how do you plan to take from the previous depth untill this one?",
        format="%d min",
        default=0
    ),
    "depth": st.column_config.NumberColumn(
        "diepte (m)",
        help="what depth do you plan to go to?",
        format="%d m",
        default=0
    ),
    
    "pressure": st.column_config.NumberColumn(
        "druk (bar)",
        help="difference in pressure (bar)",
        format="%.1f bar",
        disabled=True,
        default=0
    ),
    "calculation": st.column_config.TextColumn(
        "berekening",
        default="diepte*tijd*verbruik=",
        disabled=True
    )
    
        
},
num_rows="dynamic",
)

if st.button("recalculate"):
    edited_df["pressure"]=15
    st.write(edited_df)
