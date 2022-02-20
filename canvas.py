import tkinter

print("To draw, hold down the left mouse button, and move your mouse")
print("To change your brush colour, click on one of the colours")

window = tkinter.Tk()  #creates a tkinter window and gives it a name
canvas = tkinter.Canvas(window, width=750, height=500, bg="white") #.Canvas() creates a blank tkinter canvas, arguments set the size
canvas.pack() #.pack() puts the canvas in the tkinter window

lastX, lastY = 0,0 #top left hand corner ofthe canvas
colour = "black"

def store_position(event):
    global lastX, lastY #this allows function to access lastX and lastY created previously
    lastX = event.x #These keep track of x and y coordinates of the mouse pointer as it moves
    lastY = event.y

def on_click(event): #the parameter for this functin is the event of clicking the mouse
    store_position(event) #this is the function created in the previous step

def on_drag(event):      #\/ calls .create_line() and runs it on the canvas     #fill allows you to set colour ofthe line and width thickness in pixels
    canvas.create_line(lastX, lastY, event.x, event.y, fill = colour, width = 2)  #event .x & .y contain current x and y coordinates, where the ponter has been dragged to
    store_position(event)   #lastX & Y contain coordinates of the pointer when last clicked or dragged, start position
    #^ records position of the mouse-pointer when you finish dragging
canvas.bind("<Button-1>", on_click) #binds a left mouse click to the on_click() function *note num1 not l for left*
canvas.bind("<B1-Motion>", on_drag) #any mouse movemnet while left button is clicked...this binds that action to the on_drag() function

red_id = canvas.create_rectangle(10, 10, 30, 30, fill="red")        #each sq gets its own id. used to identify it
blue_id = canvas.create_rectangle(10, 35, 30, 55, fill="blue")      #each sq is outlined using x and y. left x, top y, right x, bottom y
black_id = canvas.create_rectangle(10, 60, 30, 80, fill="black")       #fill tells the computer to fill each sq with the named colour
white_id = canvas.create_rectangle(10, 85, 30, 105, fill="white")
#when you create an object on a canvas comp gives it an id, to keep track of it
def set_colour_red(event): #the parameter for this functin will be the event of clicking on the red sq
    global colour #global allows you to change the global 'colour' variable defined earlier
    colour="red"

def set_colour_blue(event):
    global colour
    colour="blue"

def set_colour_black(event):
    global colour
    colour="black"

def set_colour_white(event): #white is useful for erasing things
    global colour
    colour="white"

canvas.tag_bind(red_id, "<Button-1>", set_colour_red) #<Button-1> means a left mouse click
canvas.tag_bind(blue_id, "<Button-1>", set_colour_blue)
canvas.tag_bind(black_id, "<Button-1>", set_colour_black) # these call the set_colour functions created last step
canvas.tag_bind(white_id, "<Button-1>", set_colour_white)
    #^tag_bind() is used to link an event on an object (that is one of the squares) to a particular function
window.mainloop() #this line has to saty at the end of the programme
