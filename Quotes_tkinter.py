import tkinter as tk
import random

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

class QuoteApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("💬 Quote Machine")
        self.geometry("520x240")
        self.resizable(False, False)

        tk.Label(self, text="Choose category:").pack(pady=(12, 0))
        self.var = tk.StringVar(value="motivational")
        frame = tk.Frame(self)
        frame.pack(pady=6)
        for cat in quotes.keys():
            tk.Radiobutton(frame, text=cat.title(), variable=self.var, value=cat).pack(side="left", padx=8)

        self.status = tk.Label(self, text="", font=("Segoe UI", 10))
        self.status.pack(pady=(8,0))

        self.result = tk.Label(self, text="", wraplength=480, font=("Segoe UI", 12, "bold"), justify="center")
        self.result.pack(pady=(8, 0))

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=12)
        tk.Button(btn_frame, text="Get Quote", command=self.start_drama).pack(side="left", padx=6)
        tk.Button(btn_frame, text="Quit", command=self.quit).pack(side="left", padx=6)

        self._dot_count = 0

    def start_drama(self):
        self.result.config(text="")
        self._dot_count = 0
        self.status.config(text="Finding the perfect quote")
        self.after(300, self._drama_step)

    def _drama_step(self):
        # show growing dots and then display quote
        self._dot_count += 1
        dots = "." * self._dot_count
        self.status.config(text=f"Finding the perfect quote{dots}")
        if self._dot_count < 4:
            self.after(300, self._drama_step)
        else:
            cat = self.var.get()
            quote = random.choice(quotes[cat])
            self.status.config(text="Here you go:")
            self.result.config(text=f"👉 {quote}")

if __name__ == "__main__":
    QuoteApp().mainloop()
