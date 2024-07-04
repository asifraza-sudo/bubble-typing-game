import tkinter as tk
import random

class BubbleTypingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Bubble Typing Game")
        self.master.geometry("800x600")

       
        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack()
        self.draw_gradient()

       
        self.bubbles = []

        
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

        self.start_game()

    def draw_gradient(self):
        
        colors = ['#ff9999', '#66ccff']  
        for i in range(600):
            color = self.interpolate_color(colors[0], colors[1], i / 600)
            self.canvas.create_line(0, i, 800, i, fill=color)

    def interpolate_color(self, color1, color2, ratio):
       
        r = int(color1[1:3], 16) * (1 - ratio) + int(color2[1:3], 16) * ratio
        g = int(color1[3:5], 16) * (1 - ratio) + int(color2[3:5], 16) * ratio
        b = int(color1[5:7], 16) * (1 - ratio) + int(color2[5:7], 16) * ratio
        return f"#{int(r):02x}{int(g):02x}{int(b):02x}"

    def start_game(self):
      
        self.create_bubble()
        self.master.after(2000, self.start_game)

    def create_bubble(self):
       
        x = random.randint(50, 750)
        y = random.randint(50, 550)
        size = random.randint(20, 50)
        letter = random.choice(self.alphabet)
        bubble = self.canvas.create_oval(x-size, y-size, x+size, y+size, outline="black", fill="white")
        text = self.canvas.create_text(x, y, text=letter, font=("Helvetica", 12, "bold"))
        self.bubbles.append((bubble, text))
        self.master.bind("<Key>", lambda event, letter=letter: self.pop_bubble(event, letter))

    def pop_bubble(self, event, letter):
       
        key = event.char.lower()
        for bubble, text in self.bubbles:
            if key == letter:
                self.canvas.delete(bubble)
                self.canvas.delete(text)
                self.bubbles.remove((bubble, text))
                break

def main():
    root = tk.Tk()
    game = BubbleTypingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
