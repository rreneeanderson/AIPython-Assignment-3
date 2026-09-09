

import tkinter as tk

root = tk.Tk()
root.title("Maze")

size = 40

with open("shape.txt", "r") as file:
    maze = file.read().splitlines()

rows = len(maze)
cols = max(len(row) for row in maze)

canvas = tk.Canvas(
    root,
    width=cols * size,
    height=rows * size,
    bg="white"
)
canvas.pack()

for row in range(rows):
    for col in range(len(maze[row])):

        x1 = col * size
        y1 = row * size
        x2 = x1 + size
        y2 = y1 + size

        if maze[row][col] == "*":
            canvas.create_rectangle(
                x1, y1, x2, y2,
                outline="black"
            )

        elif maze[row][col] == "P":
            canvas.create_arc(
                x1 + 5, y1 + 5,
                x2 - 5, y2 - 5,
                start=25,
                extent=315,
                fill="#ffff00",
                outline="#000",
                width=2
            )

            canvas.create_oval(
                x1 + 18, y1 + 10,
                x1 + 22, y1 + 14,
                fill="#000",
                width=0
            )

root.mainloop()