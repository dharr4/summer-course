name = input("What is your name?")

rank = input("What is your rank?")

pu_raw = input("How many push ups did you do?")

run_raw = input("How fast did you run in minutes?")

pu = int(pu_raw)

run = int(run_raw)

average_run = run/2

messege = f"Okay {rank} {name}, you performed {pu} push ups, and ran 2-miles in {run} minutes."

messege_averge_run = f"Your average run time was {average_run} minutes per mile. Dismissed."

print(messege)
print(messege_averge_run)

print("==AFTER ACTION REPORT==")
print(f"Soldier: {rank} {name}")
print(f"PUSH UPS = {pu}")
print(f"2-MILE RUN = {run}")
print(f"AVERAGE PACE = {average_run}")
print("DISMISSED")
