# File Integrity Monitor

This Python script is a simple file integrity monitor that uses the `watchdog` library to observe changes to a specified file. It detects and reports file modifications, creations, and deletions, as well as providing a unified diff of the file contents when changes are detected.

## Features

- Monitors a specified file for changes in real-time.
- Reports when the file is created, modified, or deleted.
- Displays a unified diff of the file contents upon modification.

## Requirements

- Python 3.x
- `watchdog` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Install the required Python library:**

    ```bash
    pip install watchdog
    ```

## Usage

1. **Run the script:**

    ```bash
    python file_integrity_monitor.py
    ```

2. **Enter the file path to monitor when prompted:**

    ```text
    Enter the file path to monitor: /path/to/your/file.txt
    ```

3. **The script will output messages to the console whenever the file is created, modified, or deleted. If the file is modified, it will display the differences between the old and new contents.**

## Example Output

```text
Started monitoring /path/to/your/file.txt
The file /path/to/your/file.txt has been created at Fri Jun  7 15:52:55 2024
The file /path/to/your/file.txt has been changed at Fri Jun  7 16:01:00 2024
--- before
+++ after
The file /path/to/your/file.txt has been deleted at Fri Jun  7 16:05:00 2024
