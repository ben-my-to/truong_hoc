#!/usr/bin/env python3

import os
import re
import shutil
from pathlib import Path


path = Path('submissions/')
list_files = (_ for _ in os.listdir(path) if Path(_).is_file())


def parser():
    """Parses each submission file's name and moves it to a new/existing folder"""
    os.chdir(path)

    for fd in list_files:
        name, ext = os.path.splitext(fd)
        title = re.search(r'([a-zA-Z]+)_.', name)
        rename = title.group(1)
        if not Path(rename).is_dir():
            Path(rename).mkdir(parents=True, exist_ok=True)
        shutil.move(fd, rename+"/"+rename+ext)


if __name__ == '__main__':
    parser()
