import time

for h in range(24):
  for m in range(60):
    for s in range(60):
      print(f"{h:02}:{m:02}:{s:02}", end ="\r", flush=True)
      time.sleep(1)
      