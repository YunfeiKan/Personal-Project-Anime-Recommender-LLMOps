import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender", layout="wide")

load_dotenv()

# Initialize and cache the pipeline so that it doesn't re-initialize every query
@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your preferences, e.g.: Shonen combat anime with fantasy settings")
if query:
    with st.spinner("Fetching recommendations for you......"):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)