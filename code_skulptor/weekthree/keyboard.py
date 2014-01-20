# Keyboard echo
import simplegui

# Initialize state
current_key = ' '

# event handlers
def keydownkey):
    global current_key
    current_key = chr(key)

def keyup(key):
    global current_key
    current_key = chr(key)

def draw(canvas):
    canvas.draw_text(current_key, [10, 25], 20, "Red")

# Create frame
frame = simplegui.create_frame("Echo", 35, 35)

# register event handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

frame.start()
