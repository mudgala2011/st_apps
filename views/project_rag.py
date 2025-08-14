import streamlit as st

video_file = open("assets/RAG_demo.mp4", "rb")
video_bytes = video_file.read()
st.title("Retrieval Augmented Generation(RAG)")

st.video(video_bytes, autoplay=True)

st.divider()
st.subheader("Brief Description :material/short_text:")
st.write(
    """
    This business use case demonstrates that unstructured data sources(documents, images etc.) at Enterprise can be effectively
    converted to a form where a natural language Q&A front end can be utilized to fetch the information. The solution is an example 
    of intelligent information retrieval using the power of LLMs and Artificial Intelligence.
    
    - A large HR policy document (approximately 100+ pages) containing text, forms, images, is used as unstructured data source   
       
    """
)
st.divider()

st.subheader("Solution Approach :material/lightbulb:")
st.write(
    """
    - Chunk the HR policy document/s using Docling
    - Generate embeddings using the popular embedding models
    - Upsert the embeddings to a reliable vector store like lanceDB
    - Instance of lancedb is hosted locally
    - Develop the web applicaton capable connected to the local vector db (embedded policy document)
    - Use OpenAI (or any other text generation LLM) to generate natural language responses against the employee queries
    - Responses include the citations to establish the authenticity of the response
    - Suitable prompts to OpenAI LLM (gpt-4o-mini in this case) to prevent hallucinations and inappropriate responses from LLM
    - Deploy the web applicaton for end user   
    """
)
st.divider()

st.subheader("Benefits :material/workspace_premium:")
st.write(
    """
    - Creative use of AI to effectively convert the unstructured document to meaning ful textual input (Docling)
    - Embeddings uploaded to persistent indexed vector database instance, maintainable and efficient
    - Scaleable, resilient and responsive. Vector database instance can be scaled to any size
    - Flexible backend to adapt to any Generative AI LLM service provider (OpenAI, Anthropic, Google etc.)
    - Data pipeline independent of the generative component. Can accomodate both dynamic and static data source
    - Leverages the semantic search power of modern AI and Large language models
    - Portable codebase deployable to any environment or cloud
    - Easy to integrate in existing workflow        
    """
)
st.divider()

st.subheader("Assets :material/storage:")
st.link_button(
    "Codebase",
    "https://github.com/mudgala2011/RAG-demo",
    icon=":material/computer:",
)
st.link_button(
    "Docling",
    "https://docling-project.github.io/docling/",
    icon=":material/graph_5:",
)
