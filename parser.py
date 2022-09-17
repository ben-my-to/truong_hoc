#!/usr/bin/env python3

import os
import re
import shutil
import multiprocessing, threading
from pathlib import Path


# path = Path('path/to/target/directory/')
path = Path('submissions/')
list_files = (fp for fp in os.listdir(path) if Path(fp).is_file())

lock = multiprocessing.Lock()

def parse():
    title = re.search(r'([a-z|A-Z]+)_.', os.path.splitext(name)[0])
    new_name = title.group(1)

    lock.acquire()
    if not Path(new_name).is_dir():
        Path(new_name).mkdir(parents=True, exist_ok=True)
    lock.release()

    shutil.move(name, new_name)


if __name__ == '__main__':
    os.chdir(path)

    for tid, name in enumerate(list_files):
        t = threading.Thread(target=parse, name=tid, args=[])
        t.start()
        t.join()
