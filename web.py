import streamlit as st
import functions

st.markdown(
    """
    <style>
    .stApp {
        background-color: #D768F7; /* Change this to your desired background color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Sentiment Analysis App")
st.subheader("Thought.....")
st.write("How you feel today?")

user_input=st.text_area("Enter your thought here...")

if st.button("Submit"):
    if user_input:
        functions.write_thought(user_input)
        sentiment=functions.get_sentiment(user_input)
        st.write(f'The sentiment of your thought is: {sentiment}')
    else:
        st.write("Enter a thought before submitting...")

past_thought=functions.read_thought()
st.write(past_thought)