import streamlit as st

###########################################################################
### Page Set up
###########################################################################

about_page = st.Page(
    page="views/about_me.py",
    title="About me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    page="views/project_rag.py",
    title="RAG",
    icon=":material/robot_2:",
)

project_2_page = st.Page(
    page="views/project_classify.py",
    title="Topic Modeling ",
    icon=":material/smart_toy:",
)

project_4_page = st.Page(
    page="views/project_smedia.py",
    title="Services",
    icon=":material/apps:",
)
###########################################################################
### Navigation Set up
###########################################################################
pg = st.navigation(
    {
        "General Information": [about_page, project_4_page],
        "Sample Projects": [project_1_page, project_2_page],
    }
)

###########################################################################
### Run Navigation
###########################################################################
st.logo("assets/Swaapana_logo.png", size="large")

st.sidebar.text("Trust, Transparency & Truth")
pg.run()
