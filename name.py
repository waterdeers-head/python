import streamlit as st
import random
import time

name = "이태경"
colors = ["#f30000", "#fc7703", "#f2cb08", "#43f308", "#08c8f3", "#2308f3", "#7907f2"]

num_names = 4

if "step" not in st.session_state:
    st.session_state.step = 0

placeholder = st.empty()


html_code = """
<div style='
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    justify-items: center;
    align-items: center;
    text-align: center;
'>
"""

for _ in range(4):
    color = random.choice(colors)
    html_code += f"""
    <h1 style='
        margin: 10px;
        color: {color};
        font-size: 80px;
    '>{name}</h1>
    """

html_code += "</div>"


placeholder.markdown(html_code, unsafe_allow_html=True)

time.sleep(0.01)
st.session_state.step += 1
st.rerun()
