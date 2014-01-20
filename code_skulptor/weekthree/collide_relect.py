import simplegui

# Initialize globals
width = 600
height = 400
ball_radius = 20

ball_pos = [width/2, height/2]
vel = [-40/60, 5/60]

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
                    
    # collide and relect off of left hand size of canvas
    if ball_pos[0] <= ball_radius:
        vel[0] = -vel[0]
    if ball_pos[0] >= width-1-ball_radius:
        vel[0] =  -vel[0]
                                                            
# Draw ball
canvas.draw_circle(ball_pos, ball_radius, 2, "Red", "White")
                                                                        
# create frame
frame = simplegui.create_frame("Ball physics",width, height)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
