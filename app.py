import requests
from streamlit_lottie import st_lottie
import streamlit as st

st.set_page_config(page_title="Laptop Asset", page_icon=":heart_exclamation:", layout="wide")

# header section
with st.container():
    st.title("Laptop Asset Specification")
    st.write("---")


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


# load asset
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# about section
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            Here's a list about your product laptop: 
            - Display Name: Herlinda 2
            - User Principal Name: herlinda.sardi@gobel.co.id
            - Model Name: Lenovo Legion 5 16IRX9
            - PC Name: IIAPG-Linda
            - Laptop Code: IIAPG-NB24-002
            - Job Title: Procurement
            - Department: Legal
            - Email: herlinda.sardi@outlook.com
            - Password: Cawang*2024
            - Laptop PIN: 112233
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
