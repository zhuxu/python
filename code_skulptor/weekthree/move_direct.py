import simplegui

# Initialize globals
width = 600
height = 400
ball_radius = 20

ball_pos = [width/2, height/2]

# define events handlers
def draw(canvas):
        canvas.draw_circle(ball_pos, ball_radius, 2, "Red", "White")

def keydown(key):
    vel = 4
    if key == simplegui.KEY_MAP["left"]:
        ball_pos[0] -= vel
    elif key == simplegui.KEY_MAP["right"]:
        ball_pos[0] += vel
    elif key == simplegui.KEY_MAP["down"]:
        ball_pos[1] += vel
    elif key == simplegui.KEY_MAP["up"]:
        ball_pos[1] -= vel

# create frame
frame = simplegui.create_frame("Positional ball control", width, height)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

frame.start()
