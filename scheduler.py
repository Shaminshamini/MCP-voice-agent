import schedule
import time
import subprocess

# Schedule the voice agent to run at 10 AM every day
schedule.every().day.at("10:00").do(lambda: subprocess.run(["python", "app.py"]))

print("Scheduler started. Waiting for tasks...")

while True:
    schedule.run_pending()
    time.sleep(60)
