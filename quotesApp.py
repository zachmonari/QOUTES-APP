# quotes_app.py
import random
import streamlit as st

# Dictionary with categories
quotes = {
    "Motivational": [
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "It always seems impossible until it's done. – Nelson Mandela",
        "The best way to get started is to quit talking and begin doing. – Walt Disney",
    ],
    "Funny": [
        "I'm not arguing, I'm just explaining why I'm right. – Unknown",
        "Why don’t scientists trust atoms? Because they make up everything!",
        "I'm on a seafood diet. I see food and I eat it. – Unknown",
    ],
    "Tech": [
        "Talk is cheap. Show me the code. – Linus Torvalds",
        "Programs must be written for people to read. – Harold Abelson",
        "First, solve the problem. Then, write the code. – John Johnson",
    ]
}

# Streamlit UI
st.title("💬 Quote Machine")

# Dropdown for category
category = st.selectbox("Choose a category", list(quotes.keys()))

if st.button("Get Random Quote"):
    quote = random.choice(quotes[category])
    st.success(quote)

# Optionally show all quotes in that category
st.subheader(f"📖 All {category} Quotes")
for q in quotes[category]:
    st.write(f"👉 {q}")
