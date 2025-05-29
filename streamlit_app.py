import streamlit as st
import pandas as pd

st.title("Luchtplanner")



if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(data=
        [
           {"time": 0, "time_cumu":0, "depth": 0, "negative_depth":0, "pressure":1,"delta_pressure":0,"calc_pressure":0,"calculation":"diepte*tijd*verbruik=","air_used":0 },
           {"time": 0, "time_cumu":0.01, "depth": 0, "negative_depth":0, "pressure":1,"delta_pressure":0,"calc_pressure":0,"calculation":"diepte*tijd*verbruik=","air_used":0 },
           {"time": 0, "time_cumu":0.01, "depth": 0, "negative_depth":0, "pressure":1,"delta_pressure":0,"calc_pressure":0,"calculation":"diepte*tijd*verbruik=","air_used":0 },
           {"time": 0, "time_cumu":0.01, "depth": 0, "negative_depth":0, "pressure":1,"delta_pressure":0,"calc_pressure":0,"calculation":"diepte*tijd*verbruik=","air_used":0 },
           {"time": 0, "time_cumu":0.01, "depth": 0, "negative_depth":0, "pressure":1,"delta_pressure":0,"calc_pressure":0,"calculation":"diepte*tijd*verbruik=","air_used":0 },
           {"time": 0, "time_cumu":0.01, "depth": 0, "negative_depth":0, "pressure":1,"delta_pressure":0,"calc_pressure":0,"calculation":"diepte*tijd*verbruik=","air_used":0 },
           {"time": 0, "time_cumu":0.01, "depth": 0, "negative_depth":0, "pressure":1,"delta_pressure":0,"calc_pressure":0,"calculation":"diepte*tijd*verbruik=","air_used":0 },
           {"time": 0, "time_cumu":0.01, "depth": 0, "negative_depth":0, "pressure":1,"delta_pressure":0,"calc_pressure":0,"calculation":"diepte*tijd*verbruik=","air_used":0 },
           {"time": 0, "time_cumu":0.01, "depth": 0, "negative_depth":0, "pressure":1,"delta_pressure":0,"calc_pressure":0,"calculation":"diepte*tijd*verbruik=","air_used":0 },
           {"time": 0, "time_cumu":0.01, "depth": 0, "negative_depth":0, "pressure":1,"delta_pressure":0,"calc_pressure":0,"calculation":"diepte*tijd*verbruik=","air_used":0 },
           {"time": 0, "time_cumu":0.01, "depth": 0, "negative_depth":0, "pressure":1,"delta_pressure":0,"calc_pressure":0,"calculation":"diepte*tijd*verbruik=","air_used":0 }
       ]
    )
if "test" not in st.session_state:
    st.session_state.test=""
if "air_useage" not in st.session_state:
    st.session_state.air_useage=21


@st.fragment()
def air_plan_table():
    air_useage=st.session_state.air_useage
    edited_df=st.data_editor(
        st.session_state.df, 
        column_order=("time_cumu","time" ,"depth","pressure","calculation","air_used"),
        column_config={
            "time": st.column_config.NumberColumn(
                "tijd",
                help="how do you plan to take from the previous depth untill this one?",
                format="%.1f min",
                default=0.01
            ),
            "time_cumu": st.column_config.NumberColumn(
                "tijd (cumu)",
                help="how do you plan to take from the previous depth untill this one?",
                format="%.1f min",
                disabled=True,
                default=0
            ),
            "depth": st.column_config.NumberColumn(
                "diepte",
                help="what depth do you plan to go to?",
                format="%d m",
                default=0
            ),
            "pressure": st.column_config.NumberColumn(
                "druk",
                help="difference in pressure (bar)",
                format="%.1f bar",
                disabled=True,
                default=0
            ),
            "calculation": st.column_config.TextColumn(
                "berekening",
                default="diepte*tijd*verbruik=",
                disabled=True
            ),
            "air_used": st.column_config.NumberColumn(
                "lucht",
                format="%.1f bar",
                default=0
            )
        },
        num_rows="fixed",
        )
    
    edited_df.reset_index()
    edited_df.pressure=edited_df.depth/10+1
    edited_df.negative_depth=edited_df.depth*-1
    edited_df.delta_pressure=abs(edited_df.pressure - edited_df.pressure.shift(1)).fillna(0)
    print(edited_df.index)
    i=0
    while i<len(edited_df.index):

        j=i-1
        if edited_df.loc[i,"delta_pressure"]>0 and i>0:
            if edited_df.loc[i,"time"]==0:
                edited_df.loc[i,"time"]=edited_df.loc[i,"delta_pressure"]
        if i>0:
            edited_df.loc[i,"calc_pressure"]=edited_df.loc[i,"delta_pressure"]+min(edited_df.loc[i,"pressure"],edited_df.loc[i-1,"pressure"])
            if edited_df.loc[i,"time"]==0.01:
                edited_df.loc[i,"time"]=abs(edited_df.loc[i,"depth"]-edited_df.loc[j,"depth"])/10
                
        else:
            edited_df.loc[i,"calc_pressure"]=1

        edited_df.loc[i,"calculation"]=str(edited_df.loc[i,"time"]) + " min *"+str(edited_df.loc[i,"pressure"])+ " bar *"+str(air_useage)+" l/min ="
        i+=1
    edited_df.time_cumu=edited_df.time.cumsum()
    edited_df.air_used=edited_df.calc_pressure*edited_df.time*air_useage
    
    if st.button("Bereken", type="primary"):
        st.session_state.df=edited_df
        st.rerun()
    
st.area_chart(st.session_state.df,x="time_cumu",y="negative_depth", x_label="tijd (minuten) -->",y_label="<-- diepte",height=180)
air_plan_table()
