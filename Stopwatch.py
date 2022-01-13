#run at https://py2.codeskulptor.org/#user48_DFoYmu69eqhACa5_0.py

# template for "Stopwatch: The Game"
import simplegui

# define global variables
current_time = 0
formatted_time = "0:00.0"
running = False
attempts = 0
successes = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global formatted_time
    minutes = t / 600
    seconds = int(round((t-(minutes*600))/10))
    tenths_of_seconds = int(round((t-(minutes*600))%10))
    
    if seconds < 10:
        formatted_time = str(minutes) + ":0" + str(seconds) + "." + str(tenths_of_seconds)
    else:
        formatted_time = str(minutes) + ":" + str(seconds) + "." + str(tenths_of_seconds)

    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    running = True
    timer.start()
    
def stop():
    global running, attempts, successes
    
    if running == True:
        attempts += 1
        if current_time % 10 == 0:
            successes += 1
    
    running = False
    timer.stop()

def reset():
    global current_time, running, attempts, successes
    timer.stop()
    running = False
    current_time = 0
    format(current_time)
    attempts = 0
    successes = 0    
    

# define event handler for timer with 0.1 sec interval
def tick():
    global current_time
    current_time += 1
    format(current_time)

# define draw handler
def draw(canvas):
    canvas.draw_text(formatted_time, (100, 110), 40, "Red")
    canvas.draw_text(str(successes) + "/" + str(attempts), (25,25), 20, "Blue")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()

# Please remember to review the grading rubric
