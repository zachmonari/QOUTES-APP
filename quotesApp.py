# quotes_app.py
import random
import streamlit as st

# Dictionary with categories
quotes = {
    "Motivational": [
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "It always seems impossible until it's done. – Nelson Mandela",
        "The best way to get started is to quit talking and begin doing. – Walt Disney",
        "The future belongs to those who believe in the beauty of their dreams — Eleanor Roosevelt",
        "Success is not final; failure is not fatal: it is the courage to continue that counts — Winston Churchill",
        "The only way to do great work is to love what you do — Steve Jobs"
    ],
    "Funny": [
        "I'm not arguing, I'm just explaining why I'm right. – Unknown",
        "Why don’t scientists trust atoms? Because they make up everything!",
        "I'm on a seafood diet. I see food and I eat it. – Unknown",
        "I'm not lazy, I'm just in energy-saving mode",
        "I always wanted to be somebody, but now I realize I should have been more specific",
        "My fake plants died because I did not pretend to water them",
        "People say nothing is impossible, but I do nothing every day",
        "I told my wife she was drawing her eyebrows too high. She looked surprised"
    ],
    "Tech": [
        "Talk is cheap. Show me the code. – Linus Torvalds",
        "Programs must be written for people to read. – Harold Abelson",
        "First, solve the problem. Then, write the code. – John Johnson",
        "The best way to predict the future is to invent it. — Alan Kay",
        "The tools of the future are being built by those willing to think beyond today. — Various authors",
        "Technology is best when it brings people together. — Matt Mullenweg"
    ]
}

# Streamlit UI
st.title("💬 Quote Machine")
st.sidebar.markdown("### © Zach Techs 2025")
st.sidebar.write("🌍 Inspiring one quote at a time")


# Dropdown for category
category = st.selectbox("Choose a category", list(quotes.keys()))

if st.button("Get Random Quote"):
    quote = random.choice(quotes[category])
    st.success(quote)
