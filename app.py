import streamlit as st
from textblob import TextBlob

st.title('Sentiment Analyser')

st.divider()

st.write('Enter a sentence to analyze sentiment.')

user_input = st.text_input('Enter the sentence:')

if user_input:
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        st.write('Sentence is positive:)')

    elif sentiment < 0:
        st.write('Sentiment Negative:(')
    
    else:
        st.write('Sentiment Neutral: I')

    st.write(f'Sentiment Score:',{sentiment})