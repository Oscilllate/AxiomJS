import time
import subprocess
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Get the directory where watcher.py lives
BASE_DIR = os.path.dirname(__file__)

# Watch the /module folder
WATCH_PATH = os.path.join(BASE_DIR, "module")

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("osc.module.js"):
            print("Change detected, rebuilding...")
            subprocess.run(["python", os.path.join(BASE_DIR, "autogenscript.py")])

if __name__ == "__main__":
    if not os.path.exists(WATCH_PATH):
        print(f"Watch path does not exist: {WATCH_PATH}")
        exit(1)

    event_handler = Handler()
    observer = Observer()

    observer.schedule(event_handler, path=WATCH_PATH, recursive=False)

    observer.start()
    print(f"Watching: {WATCH_PATH}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()