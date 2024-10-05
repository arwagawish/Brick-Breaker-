from tkinter import Tk, Canvas
from settings import WIDTH, HEIGHT
from game import run_game

root = Tk()
screen = Canvas(root, width=WIDTH, height=HEIGHT, background="black")

if __name__ == "__main__":
    screen.pack()
    screen.focus_set()
    run_game(root, screen)  # Start the game
    root.mainloop()
