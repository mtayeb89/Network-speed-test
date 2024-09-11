# Network-speed-test
Network Speed Test GUI

A simple Python application with a graphical user interface (GUI) built using tkinter to measure internet speed (download, upload, and ping) using the speedtest-cli library.
Features

    Test and display download speed in Mbps.
    Test and display upload speed in Mbps.
    Measure and display ping in milliseconds (ms).
    Simple and user-friendly graphical interface.
    Error handling with pop-up messages for any issues (e.g., no internet connection).

# Prerequisites

Make sure you have Python installed. You can download it from the official Python website.
Required Libraries

    tkinter: The standard Python interface for creating graphical user interfaces.
    speedtest-cli: A Python library to perform internet speed tests.

# Installation of Required Libraries

    Install speedtest-cli:

    bash

    pip install speedtest-cli

    tkinter: Pre-installed with most Python distributions, no need to install it separately.

# How to Run the Program

    Clone or download this repository to your local machine.

    Open a terminal (or command prompt) in the directory where your Python script is saved.

    Run the Python script:

    bash

    python network_speed_test.py

        Note: If you get an error saying No module named 'speedtest', make sure your Python script is not named speedtest.py, as it may conflict with the installed speedtest-cli library.

    Use the application:
        Click the Test Speed button to measure your internet's download speed, upload speed, and ping.
        The results will be displayed in the application window.

# Code Overview
test_speed() Function

    Connects to a speed test server.
    Measures download speed, upload speed, and ping.
    Displays the results in the GUI.
    Handles errors and displays an error message using tkinter.messagebox.

# GUI Elements

    Labels: Display download speed, upload speed, and ping.
    Button: Starts the speed test when clicked.


# Error Handling

If there is any issue while performing the speed test (e.g., no internet connection), an error message will appear with relevant details.
Troubleshooting

    Module Import Error: Ensure you have installed speedtest-cli by running:

    bash

    pip install speedtest-cli

    Conflicting Script Name: Ensure your Python script is not named speedtest.py. Rename it to something else, like network_speed_test.py.
