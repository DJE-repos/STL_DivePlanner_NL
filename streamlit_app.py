import streamlit as st
import pandas as pd

st.title("my awesome app")
air_useage=21

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(data=
        [
           {"time": 0, "depth": 0, "pressure":1,"calculation":"diepte*tijd*verbruik=","air_used":0 }
       ]
    )

@st.fragment()
def air_plan_table():
    edited_df=st.data_editor(
        st.session_state.df, 
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
        i=0
        while i<len(st.session_state.df.index):
            st.session_state.df.loc[i,"calculation"]=str(st.session_state.df.loc[i,"time"] + "min *"+st.session_state.df.loc[i,"pressure"])
            i+=1
        st.rerun()
        st.markdown("test")
        
air_plan_table()



    
