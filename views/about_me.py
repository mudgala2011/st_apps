import streamlit as st
import plotly.express as px
import pandas as pd


##############################################################################################################
# Hero Section
##############################################################################################################

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("assets/Abhishek_profile_pic.jpg", width=230)
with col2:
    st.title("Abhishek Mudgal", anchor=False)
    st.write("AI Architect/Senior Data Scientist")
    st.write("📳 + 91-977-913-2735")
    st.write("📧 abhishek.opstat@gmail.com")

## Professional Summary
st.write("\n")
st.subheader("Professional Summary :material/quick_reference:")
st.write(
    """
    - Result Oriented Data Science & AI Professional with over 15+ years of Industry experience
    - Conceptualized, planned, executed and managed complex Data Science delivery programs
    - Built, supervised and mentored diverse high performing teams of software architects, data scientists, project managers, business analysts and other specialists & also worked as individual contributor

    """
)
## Tech Stack
st.write("\n")
st.subheader("Tech Stack :material/construction:")
st.write(
    """
    - AI Stack : Large Language Models(LLMs), Transformers architecture, Encoder and Decoder models, tokenizers, Embedding models and vector stores, naive, advanced and modular RAG(Retrieval augmented generation) and semantic search, data pipeline and maintenance, RAG monitoring and evaluation metrics  
    - Tool Set : Python 3.X, OpenAI, Huggingface, pinecone, deeplake, lancedb, keras, scikit-learn, pandas  
    - Machine Learning : Regression &  Classification, Decision trees, Cluster analysis, Market Basket analysis, Segmentation Studies, Deep Learning 
    
    """
)

## Work Experience
st.write("\n")
st.subheader("Industry Experience :material/simulation:")
df = pd.DataFrame(
    [
        dict(
            Title="Programmer Analyst",
            Start="2004-12-01",
            End="2005-04-24",
            Org="Syntel India Ltd",
            Clients="Hallmark International",
        ),
        dict(
            Title="Advisory System Analyst",
            Start="2005-04-27",
            End="2014-06-15",
            Org="IBM",
            Clients="Wells Fargo,Suntrust Bank,Panasonic,BCBS NY,Wachovia Bank",
        ),
        dict(
            Title="Account Manager",
            Start="2014-06-15",
            End="2015-03-20",
            Org="Sutherland Global Services",
            Clients="PayPal,Bank Mandiri,Cox Comm",
        ),
        dict(
            Title="Assistant General Manager",
            Start="2015-03-21",
            End="2017-11-15",
            Org="Spice Digital Ltd",
            Clients="Govt of India, Indian Railways, Spice Money",
        ),
        dict(
            Title="Enterprise Delivery Head",
            Start="2017-11-20",
            End="2022-04-28",
            Org="Trantor Software Inc.",
            Clients="ThermoFischer USA,Apple Pie Capital, Buck Consultants USA",
        ),
        dict(
            Title="Senior AI Architect",
            Start="2022-09-20",
            End="2024-09-28",
            Org="Aboitiz Data Innovation",
            Clients="Asian Development Bank,Aboitiz Power & Utilities,Aboitiz Cement",
        ),
    ]
)
## Work Exp - generate a gnatt chart
fig = px.timeline(
    df,
    x_start="Start",
    x_end="End",
    y="Org",
    color="Title",
)

st.plotly_chart(fig, use_container_width=True)

# Certifications
st.write("\n")
st.subheader("Certifications :material/approval:")
st.write("""
         - AWS Certified Solution Architect (2024)
         - AWS Certified AI Practitioner (2024)
         - Salesforce Certified Einstien and Tableau Consultant (2022)
         - Salesforce Certified Administrator (2021)
         - AWS Certified Cloud Practitioner (2020)
         - IBM & OpenGroup Certified Senior IT Specialist (2013)         
         """)
# Education
st.write("\n")
st.subheader("Education :material/school:")
st.write("""
         - Master of Science (O.R. & C.A.) 2003
           
         """)
