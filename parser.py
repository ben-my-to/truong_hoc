#!/usr/bin/env python3

import os
import re
import shutil
import multiprocessing, threading
from pathlib import Path


path = Path('submissions/')
list_files = (_ for _ in os.listdir(path) if Path(_).is_file())

lock = multiprocessing.Lock()

def parse(name):
    """Synthesizes each submission's file name and
    moves it to a new/existing folder
    """

    title = re.search(r'([a-z|A-Z]+)_.', os.path.splitext(name)[0])
    new_name = title.group(1)

    lock.acquire()  # enforce mutual-exclusion as condition should be autonomously checked
    if not Path(new_name).is_dir():
        Path(new_name).mkdir(parents=True, exist_ok=True)
    lock.release()

    shutil.move(name, new_name)


if __name__ == '__main__':
    os.chdir(path)

    for tid, name in enumerate(list_files):
        t = threading.Thread(target=parse, name=tid, args=[name])
        t.start()
        t.join()
