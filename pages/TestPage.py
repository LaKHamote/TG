import streamlit as st
from context.userContext import getUserContext
getUserContext()


print(st.session_state)