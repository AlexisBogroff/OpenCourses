from datetime import datetime

t_s = datetime.now()
txt = input("Write your text as you like:\n")
t_end = datetime.now()

# Stats
total_time = (t_end - t_s).total_seconds()
length = len(txt)
avg_speed = length / total_time

results = "{},{},{}\n".format(avg_speed, total_time, length)

with open('results.txt', 'a') as f:
    f.write(results)
