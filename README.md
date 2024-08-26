# Network Port Scanner - GUI Based

This project is a simple GUI-based port scanner tool written in Python. It allows users to scan a specified range of ports on a target host, save the scan results, and send the results via email. The tool uses multi-threading to perform fast scans and provides real-time updates through the GUI.

## Features

- **Port Scanning:** Scan a range of ports on a specified target to identify open ports.
- **GUI Interface:** Easy-to-use graphical user interface built with Tkinter.
- **Log Saving:** Save the results of the scan to a text file.
- **Email Notifications:** Send scan results via email using SMTP.

## Requirements

- Python 3.x
- Required Modules: `socket`, `threading`, `smtplib`, `tkinter`, `datetime`

## Usage

1. **Run the Script:**
   - Execute the Python script to launch the GUI.
   
2. **Configure Target and Port Range:**
   - Enter the target hostname or IP address.
   - Specify the port range to scan.

3. **Start the Scan:**
   - Click the "Start Scan" button to begin scanning.
   - The results will be displayed in the GUI.

4. **Save Results:**
   - Click the "Save Result" button to save the scan results to a text file.

5. **Send Email:**
   - Click the "Send Mail" button to email the scan results.

## Note

- Ensure to update the email credentials in the `mailScan` function before using the email feature.
