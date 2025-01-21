import streamlit as st

st.write('hello')

st.title('AI WEB SCRAPER')

url = st.text_input('Enter a website URL')

if st.button('Scrape Site'):
    st.write('Scraping the website...')
