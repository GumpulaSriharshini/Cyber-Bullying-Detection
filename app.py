import streamlit as st
import pickle

# Load the trained model and vectorizer
with open('model.pkl', 'rb') as model_file:
    models = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)


# Custom CSS Styling
def local_css():
    st.markdown("""
        <style>
            body {
                background-color: #000000;
                color: white;
            }
            .title {
                text-align: center;
                font-size: 32px;
                font-weight: bold;
                color: #B287FF;
                text-shadow: 2px 2px 4px rgba(178, 135, 255, 0.6);
            }
            .subtitle {
                text-align: center;
                font-size: 16px;
                color: #B287FF;
            }
            .box {
                background-color: #1A093E;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px #B287FF;
            }
            .result-safe {
                text-align: center;
                font-size: 20px;
                font-weight: bold;
                color: black;
                padding: 10px;
                border-radius: 10px;
                background-color: green;
                box-shadow: 0px 0px 8px #FFFFFF;
            }
            .result-danger {
                text-align: center;
                font-size: 20px;
                font-weight: bold;
                color: white;
                padding: 10px;
                border-radius: 10px;
                background-color: red;
                box-shadow: 0px 0px 8px #FF0000;
            }
            .note {
                text-align: center;
                font-size: 14px;
                color: #FFD700;
                margin-top: 20px;
            }
        </style>
    """, unsafe_allow_html=True)


local_css()

# UI Layout
st.markdown("<h1 class='title'>⚖️ Cyberbullying Detection System</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Analyze comments for harmful language and prevent online abuse.</p>",
            unsafe_allow_html=True)

st.markdown("<h3 style='color: #B287FF;'>💬 Enter the Comment:</h3>", unsafe_allow_html=True)
user_input = st.text_area("Comment", "", height=100)

st.markdown("<h3 style='color: #B287FF;'>🎧 Detection Result:</h3>", unsafe_allow_html=True)
result_placeholder = st.empty()

if st.button("🚀 Analyze Comment"):
    if user_input.strip():
        input_vec = vectorizer.transform([user_input])
        prediction = models.predict(input_vec)[0]

        if prediction == 1:
            result_placeholder.markdown(
                "<p class='result-danger'>⚠️ This comment may contain cyberbullying content!</p>",
                unsafe_allow_html=True)
        else:
            result_placeholder.markdown("<p class='result-safe'>✅ This comment seems safe.</p>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a comment.")

st.markdown("<p class='note'>🔒 Note: This tool is designed to assist in detecting harmful language.</p>",
            unsafe_allow_html=True)