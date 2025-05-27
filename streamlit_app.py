from __future__ import annotations

import pandas as pd
import streamlit as st


def add_c(new_df: pd.DataFrame | None = None):
    if new_df is not None:
        if new_df.equals(st.session_state["df"]):
            return
        st.session_state["df"] = new_df

    df = st.session_state["df"]
    df["c"] = df["a"] + df["b"]
    st.session_state["df"] = df
    st.experimental_rerun()


if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(
        {"a": [1, 2, 3], "b": [4, 5, 6], "c": [None, None, None]}
    )
    add_c()


editable_df = st.data_editor(
    st.session_state["df"],
    key="data",
    column_config={"c": st.column_config.Column(disabled=True)},
    hide_index=True,
)

add_c(editable_df)
