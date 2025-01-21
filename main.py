import streamlit as st
from scrap import scrap_Site

st.title('AI WEB SCRAPER')

url = st.text_input('Enter a website URL')

if st.button('Scrap Site'):
    st.write('Scraping the website')
    result=scrap_Site(url)
    print(result)
