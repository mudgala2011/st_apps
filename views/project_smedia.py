import streamlit as st

st.title("Services")
st.image("assets/AI_services.jpg", width=500)

## Advisory Services
st.write("\n")
st.subheader("AI Advisory Services :material/enterprise:")
st.write(
    """
    - Impact analysis: Artificial Intelligence Project assessment & Evaluation 
    - Infrastructure: choice of cloud, out of the box AI service. Cost benefit analysis
    - Vendor assessment: AI service/tool or framework evaluation, integration assessment
    - AI Roadmap: Enterprise Architecture and AI infusion (planning & roadmap)

    """
)

## Development Services
st.write("\n")
st.subheader("AI Engineering :material/build_circle:")
st.write(
    """
    - Custom Development: Develop and deploy the solutions (LLM powered applications, AI/ML Models)
    - Maintenance : Support services, enhancement, maintenance of deployed assets
    - Training: Train the team members to use the enterprise AI applications
    - Monitoring: Monitor the deployed AI/ML applications for accuracy & success metrices 

    """
)
