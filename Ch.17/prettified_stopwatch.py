
# stopwatch.py - A simple stopwatch program

import time, pyperclip

print("Press ENTER to begin. Afterwards, press ENTER to 'click' the stopwatch. Press Ctrl-C to quit.")
input()
print("Started.")
start_time = time.time()
last_time = start_time
lap_num = 1
# create list to store all the results
res = []
try:
    while True:
        input()
        lap_time = round(time.time()-last_time, 2)
        total_time = round(time.time()-start_time, 2)
        print(f"Lap # {lap_num:2}: {total_time:5} ({lap_time:4})", end='')
        output = f"Lap # {lap_num:2}: {total_time:5} ({lap_time:4})"
        res.append(output)
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    print("\nDone.")

# pyperclip could not copy list, therefore return the results in string
pyperclip.copy("\n".join(res))
