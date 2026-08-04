import streamlit as st


def footer_home():
    logo_url = (
        "https://i.ibb.co/LXJW1b83/flamingtext-com-38026961738-Photoroom.png"
    )

    st.markdown(
        f"""
        <div style="margin-top:2rem; display:flex; gap:8px; justify-content:center; align-items:center;">
            <p style="font-weight:bold; color:white; margin:0; padding:0; font-size:16px;">Created with ❤️ by</p> 
            <img src='{logo_url}' style='height:60px; width:auto; display:block;' />
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer_dashboard():
    logo_url = (
        "https://i.ibb.co/LXJW1b83/flamingtext-com-38026961738-Photoroom.png"
    )

    st.markdown(
        f"""
        <div style="margin-top:2rem; display:flex; gap:8px; justify-content:center; align-items:center;">
            <p style="font-weight:bold; color:black; margin:0; padding:0; font-size:16px;">Created with ❤️ by</p> 
            <img src='{logo_url}' style='height:60px; width:auto; display:block;' />
        </div>
        """,
        unsafe_allow_html=True,
    )