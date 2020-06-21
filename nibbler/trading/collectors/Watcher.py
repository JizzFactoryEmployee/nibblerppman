import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import nibbler.trading.collectors.futures_collector as futures


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        event_list = event.src_path.split('\\')
        filename = event_list[-1]
        print(filename)
        if "BTC" in filename:
            print('success')

def runner():

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

runner()