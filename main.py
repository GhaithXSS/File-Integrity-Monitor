import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileCreatedEvent, FileDeletedEvent
import difflib

class FileMonitorHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file_path = file_path
        # Get the last modified time if the file exists, otherwise set to None
        self.last_modified = os.path.getmtime(file_path) if os.path.exists(file_path) else None
        # Read the initial content of the file if it exists, otherwise set to empty list
        self.previous_content = self.read_file_content() if os.path.exists(file_path) else []

    def read_file_content(self):
        # Read the content of the file and return it as a list of lines
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return file.readlines()
        return []

    def on_modified(self, event):
        # Handle file modification events
        if event.src_path == self.file_path:
            current_modified = os.path.getmtime(self.file_path)
            # Check if the modification time has changed
            if current_modified != self.last_modified:
                self.last_modified = current_modified
                current_content = self.read_file_content()
                # Print the difference between the old and new content
                self.print_diff(self.previous_content, current_content)
                self.previous_content = current_content

    def on_created(self, event):
        # Handle file creation events
        if event.src_path == self.file_path:
            print(f"The file {self.file_path} has been created at {time.ctime(os.path.getctime(self.file_path))}")
            self.last_modified = os.path.getmtime(self.file_path)
            self.previous_content = self.read_file_content()

    def on_deleted(self, event):
        # Handle file deletion events
        if event.src_path == self.file_path:
            print(f"The file {self.file_path} has been deleted at {time.ctime(time.time())}")
            self.last_modified = None
            self.previous_content = []

    def print_diff(self, old_content, new_content):
        # Print the differences between the old and new content
        diff = difflib.unified_diff(old_content, new_content, fromfile='before', tofile='after', lineterm='')
        print(f"The file {self.file_path} has been changed at {time.ctime(self.last_modified)}")
        for line in diff:
            if line.startswith('@@'):
                continue
            print(line)

def monitor_file(file_path):
    # Set up the file monitoring
    event_handler = FileMonitorHandler(file_path)
    observer = Observer()
    # Monitor the directory containing the file
    observer.schedule(event_handler, path=os.path.dirname(file_path), recursive=False)
    observer.start()
    print(f"Started monitoring {file_path}")

    try:
        # Keep the script running to continue monitoring
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the observer when interrupted
        observer.stop()
        print(f"Stopped monitoring {file_path}")

    observer.join()

if __name__ == "__main__":
    # Prompt the user for the file path
    file_path = input("Enter the file path to monitor: ")
    # Check if the path is a valid file or if the file does not exist yet
    if os.path.isfile(file_path) or not os.path.exists(file_path):
        monitor_file(file_path)
    else:
        print("The provided path is not a valid file.")
