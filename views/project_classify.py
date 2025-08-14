import streamlit as st

st.title("Topic Modeling: Financial News")
st.divider()
st.subheader("Brief Description :material/short_text:")
st.write(
    """
    This case study uses the dataset which has multiple Financial news headlines. The dataset is available at Huggingface 
    (zeroshot/twitter-financial-news-topic) and is available to use. Each row in the dataset is a news related to financial world,
    altogether having around 16K rows of tweets. 

    - Is there a way to cluster these tweets in similar groups and also label the group aka give it a Topic ?
       
    """
)
st.divider()

st.subheader("Solution Approach :material/lightbulb:")
st.write(
    """
    - Convert the input texts to embeddings using a standard embeddings model
    - Reduce the dimensionality of the embeddings with a dimensionality reduction model (UMAP etc.)
    - Find groups of semantically similar tweets using a cluster model (HDBSCAN etc.)
    - Use BERTopic to generate topics 
    - Use various comparison models on improvement of topic identification. Refining the topics for end user
    - Use Generative AI to generate or suggest a topic based on keywords identified to cluster the tweets
        
    """
)
st.divider()

st.subheader("Benefits :material/workspace_premium:")
st.write(
    """
    - Creative use of AI to decipher meaning from mounds of meaningless natural language text
    - Effective use of Generative AI to assign topics and reduce the number of expensive LLM calls
    - Flexible backend to adapt to any Generative AI LLM service provider (OpenAI, Anthropic, Google etc.)
    - Portable codebase deployable to any environment or cloud
    - Easy to integrate in existing workflow
        
    """
)
st.divider()

st.subheader("Assets :material/storage:")
st.link_button(
    "Notebook",
    "https://www.kaggle.com/code/abhishekmudgal2021/financial-news-topic-modeling-using-bertopic",
    icon=":material/computer:",
)
st.link_button(
    "BERTopic",
    "https://maartengr.github.io/BERTopic/index.html",
    icon=":material/graph_5:",
)
st.link_button(
    "Dataset",
    "https://huggingface.co/datasets/zeroshot/twitter-financial-news-topic",
    icon=":material/dataset:",
)
