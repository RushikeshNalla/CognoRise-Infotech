import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 6)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(5)
        seconds -= 1

    print("Time's up!")

countdown_time = 6

countdown_timer(countdown_time)



