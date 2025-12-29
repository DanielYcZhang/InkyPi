import time

# THE LEAKY BUCKET
# This program is supposed to process data, but it crashes after a while.
# Can you find the memory leak and fix it?

history = []

def process_sensor_data():
    # Simulate reading some data (1MB of text)
    data = "x" * 1024 * 1024 
    
    # SYSTEM STATUS: Processing...
    print(f"Processing chunk. History size: {len(history)} MB")

    # --- BUG ZONE STARTS HERE ---
    # We are mistakenly saving EVERY piece of data forever.
    # We only need to process it, not keep it!
    
    history.append(data)  # <--- THIS IS THE LEAK! 
    
    # --- BUG ZONE ENDS HERE ---

if __name__ == "__main__":
    print("Starting Sensor Processor...")
    try:
        while True:
            process_sensor_data()
            time.sleep(0.5) 
    except MemoryError:
        print("\nCRASH! System ran out of RAM!")
