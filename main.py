import streamlit as st
st.session_state.counter = 1
print(st.session_state)


from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(layout="wide")

sections = st.sidebar.toggle("Sections", value=True, key="use_sections")

nav = get_nav_from_toml(".streamlit/pages_sections.toml")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()