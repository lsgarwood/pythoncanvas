import tkinter

print("To draw, hold down the left mouse button, and move your mouse")
print("To chnage your brush colour, click on one of the colours")

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=75, height=500, bg="white")
canvas.pack()

lastX, lastY = 0,0
colour = "black"

def store_position(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y

def on_click(event):
    store_position(event)

def on_drag(event):
    canvas.create_line(lastX, lastY, event.x, event.y, fill = colour, width = 3)
    store_position(event)

canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)

red_id = canvas.create_rectangle(10, 10, 30, 30, fill="red")
blue_id = canvas.create_rectangle(10, 35, 30, 55, fill="blue")
black_id = canvas.create_rectangle(10, 60, 30, 80, fill="black")
white_id = canvas.crerate_rcetngle(10, 85, 30, 105, fill="white")

window.mainloop()
