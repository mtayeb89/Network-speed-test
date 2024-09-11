import tkinter as tk
from tkinter import messagebox
import speedtest

# Function to perform the speed test
def test_speed():
    try:
        st = speedtest.Speedtest()
        st.download()  # Pre-fetch the server list and choose the best server
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping_result = st.results.ping

        # Update the labels with the results
        download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
        upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
        ping_label.config(text=f"Ping: {ping_result:.2f} ms")

    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

# Creating the tkinter GUI
root = tk.Tk()
root.title("Network Speed Test")
root.geometry("300x200")

# Labels for displaying the results
download_label = tk.Label(root, text="Download Speed: -- Mbps")
download_label.pack(pady=10)

upload_label = tk.Label(root, text="Upload Speed: -- Mbps")
upload_label.pack(pady=10)

ping_label = tk.Label(root, text="Ping: -- ms")
ping_label.pack(pady=10)

# Button to start the speed test
test_button = tk.Button(root, text="Test Speed", command=test_speed)
test_button.pack(pady=20)

# Start the tkinter main loop
root.mainloop()
