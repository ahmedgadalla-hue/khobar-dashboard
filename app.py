import streamlit as st
import pandas as pd

st.title("Khobar Sales Dashboard")

file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if file:
    df = pd.read_excel(file)

    st.dataframe(df)

    if "Revenue" in df.columns:
        total_sales = df["Revenue"].sum()
        st.metric("Total Sales", f"{total_sales:,.0f}")

    if "SBU" in df.columns:
        chart = df.groupby("SBU")["Revenue"].sum()
        st.bar_chart(chart)