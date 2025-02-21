import tkinter as tk
from random import shuffle

# Thai consonants with names
thai_consonants = [
    ("ก", "gor kai"), ("\u0E02", "kho khai"), ("\u0E03", "kho khuat"),
    ("\u0E04", "kho khwai"), ("\u0E05", "kho khon"), ("\u0E06", "kho rakhang"),
    ("\u0E07", "ngo ngu"), ("\u0E08", "cho chan"), ("\u0E09", "cho ching"),
    ("\u0E0A", "cho chang"), ("\u0E0B", "so so"), ("\u0E0C", "cho choe")
]
shuffle(thai_consonants)

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.current_index = 0
        self.flipped = False
        
        self.card_frame = tk.Frame(root, width=300, height=200, bg="white", relief="raised", bd=3)
        self.card_frame.pack(pady=20)
        
        self.label = tk.Label(self.card_frame, text="", font=("Arial", 50), bg="white")
        self.label.pack(expand=True)
        
        self.card_frame.bind("<Button-1>", self.flip_card)
        self.label.bind("<Button-1>", self.flip_card)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack()
        
        self.show_card()
    
    def show_card(self):
        self.flipped = False
        self.label.config(text=thai_consonants[self.current_index][0], font=("Arial", 50))
    
    def flip_card(self, event):
        if not self.flipped:
            self.label.config(text=thai_consonants[self.current_index][1], font=("Arial", 20))
            self.flipped = True
        else:
            self.label.config(text=thai_consonants[self.current_index][0], font=("Arial", 50))
            self.flipped = False
    
    def next_card(self):
        self.current_index = (self.current_index + 1) % len(thai_consonants)
        self.show_card()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
