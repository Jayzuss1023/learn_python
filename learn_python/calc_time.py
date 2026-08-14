import time


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1



        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60


        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}", flush=True)
    
    print("YOU'RE TIME IS UP!")

minutes = int(input("Number of minutes: "))
seconds = int(input("Number of seconds: "))
total_time = minutes * 60 + seconds
alarm(total_time)