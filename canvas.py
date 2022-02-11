import tkinter

print("To draw, hold down the left mouse button, and move your mouse")
print("To chnage your brush colour, click on one of the colours")

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=75, height=500, bg="white")
canvas.pack()

