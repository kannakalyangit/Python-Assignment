# cpu_monitor.py

import psutil  # Library to get CPU usage and system info
import time    # Used to pause between checks

# Set the CPU usage threshold
THRESHOLD = 80  # You can change this if needed

try:
    print("🖥️ Monitoring CPU usage... Press Ctrl+C to stop.")
    
    # Infinite loop to keep checking
    while True:
        # Get the current CPU usage as a percentage
        usage = psutil.cpu_percent(interval=1)  # interval=1 means check every second

        # Display the current usage
        print(f"Current CPU usage: {usage}%")

        # If it exceeds the threshold, show an alert
        if usage > THRESHOLD:
            print(f"⚠️ Alert! CPU usage is high: {usage}%")

        # Wait for 1 second before checking again (optional since interval does that too)
        # time.sleep(1)

except KeyboardInterrupt:
    # This runs if the user presses Ctrl+C to stop the script
    print("\n🛑 Monitoring stopped by user.")

except Exception as e:
    # Catches any other errors that might occur
    print(f"❌ An error occurred: {e}")
