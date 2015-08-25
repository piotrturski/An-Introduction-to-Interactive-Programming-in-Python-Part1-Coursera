import simplegui

counter,running,timer,tries,wins = 0,0,0,0,0

def format(t):
    tens_of_sec, all_secs = t % 10, t / 10
    only_secs = all_secs % 60
    sec01, sec10 = only_secs % 10, only_secs /10
    mins = (all_secs - only_secs) / 60
    return str(mins)+':'+ str(sec10)+str(sec01)+'.'+str(tens_of_sec)
    
def start():
    global running
    timer.start()
    running = True

def stop():
    global running, tries, wins
    timer.stop()
    if running:
        tries += 1
        if counter % 10 == 0:
            wins += 1
    running = False

def reset():
    global counter, running, tries, wins
    timer.stop()
    counter, tries, wins, running = 0,0,0, False

def tick():
    global counter
    counter += 1

def draw(canvas):
    canvas.draw_text(format(counter), (100,120), 34, 'White')
    canvas.draw_text(str(wins)+'/'+str(tries), (250,40), 24, 'Green')
    
frame = simplegui.create_frame("Stopwatch", 300,200)
frame.add_button('Start', start, 100)
frame.add_button('Stop', stop, 100)
frame.add_button('Reset', reset, 100)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)

reset()
frame.start()
