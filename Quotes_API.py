from fastapi import FastAPI
import random

app = FastAPI()

# Store quotes in a simple list (in-memory for now)
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
    "Happiness is not something ready made. It comes from your own actions. – Dalai Lama"
]

@app.get("/")
def root():
    return {"message": "Welcome to the Quotes API! Visit /quotes or /random"}

# Get all quotes
@app.get("/quotes")
def get_quotes():
    return {"quotes": quotes}

# Get a random quote
@app.get("/random")
def get_random_quote():
    return {"quote": random.choice(quotes)}

# Add a new quote
@app.post("/add")
def add_quote(quote: str):
    quotes.append(quote)
    return {"message": "Quote added successfully!", "total_quotes": len(quotes)}

