import random
import time

quotes = {
    "motivational": [
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "It always seems impossible until it's done. – Nelson Mandela",
        "The best way to get started is to quit talking and begin doing. – Walt Disney",
    ],
    "funny": [
        "I'm not arguing, I'm just explaining why I'm right. – Unknown",
        "Why don’t scientists trust atoms? Because they make up everything!",
        "I'm on a seafood diet. I see food and I eat it. – Unknown",
    ],
    "tech": [
        "Talk is cheap. Show me the code. – Linus Torvalds",
        "Programs must be written for people to read. – Harold Abelson",
        "First, solve the problem. Then, write the code. – John Johnson",
    ]
}

print("💬 Welcome to the Quote Machine!")
print("Available categories: motivational, funny, tech")

while True:
    category = input("\nWhich type of quote would you like? ").strip().lower()
    if category in quotes:
        print("\nSearching for the perfect quote...", end="", flush=True)
        # dramatic dots
        for _ in range(3):
            time.sleep(0.6)         # pause for drama
            print(".", end="", flush=True)
        time.sleep(0.4)
        quote = random.choice(quotes[category])
        print("\n\n👉 {}".format(quote))
    else:
        print("❌ That category doesn't exist. Try again!")

    again = input("\nWant another one? (y/n): ").strip().lower()
    if again != 'y':
        print("👋 See you next time! Stay inspired!")
        break
