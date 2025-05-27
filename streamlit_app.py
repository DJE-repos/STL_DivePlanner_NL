from __future__ import annotations

import pandas as pd
import streamlit as st


def add_c(new_df: pd.DataFrame | None = None):
    if new_df is not None:
        if new_df.equals(st.session_state["df"]):
            return

        st.session_state["df"] = new_df

    st.session_state["df"]["c"] = 0
    st.session_state["df"]["c"] = (
        st.session_state["df"]["a"] + st.session_state["df"]["b"]
    )
    st.experimental_rerun()


if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(
        {"a": [1, 2, 3], "b": [4, 5, 6], "c": [None, None, None]}
    )
    add_c()


editable_df = st.experimental_data_editor(st.session_state["df"], key="data")

add_c(editable_df)
