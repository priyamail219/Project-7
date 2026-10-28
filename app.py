import re
from pathlib import Path

import joblib
import streamlit as st

MODEL_PATH = Path("disaster_tweet_model.joblib")

def clean_tweet(text):
    text = str(text).lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"@\w+", " ", text)
    text = text.replace("#", "")
    text = re.sub(r"[^a-z0-9\s']", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

st.set_page_config(page_title="Disaster Tweet Classifier", page_icon="🆘", layout="centered")
st.title("🆘 Disaster Tweet Classifier")
st.write(
    "Enter a tweet to estimate whether it is related to a real disaster. "
    "This is an educational NLP demo and should not be used as an official emergency alert system."
)

if not MODEL_PATH.exists():
    st.error("Model file not found. Run the notebook first and create disaster_tweet_model.joblib in this folder.")
    st.stop()

@st.cache_resource
def load_model(path):
    return joblib.load(path)

model = load_model(str(MODEL_PATH))
tweet = st.text_area("Tweet text", placeholder="Example: Emergency teams are helping residents after severe flooding...", height=140)

if st.button("Classify tweet", type="primary"):
    if not tweet.strip():
        st.warning("Please enter some tweet text first.")
    else:
        cleaned = clean_tweet(tweet)
        prediction = int(model.predict([cleaned])[0])
        if prediction == 1:
            st.error("Prediction: Disaster-related tweet")
        else:
            st.success("Prediction: Not disaster-related")
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba([cleaned])[0]
            classes = list(model.classes_)
            if 1 in classes:
                confidence = float(probabilities[classes.index(1)])
                st.caption(f"Model-estimated probability for the disaster class: {confidence:.1%}")
        st.info("Predictions can be wrong, especially when language is figurative or lacks context. Verify important information independently.")
