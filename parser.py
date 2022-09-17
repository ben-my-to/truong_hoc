#!/usr/bin/env python3

import os
import re
import shutil
from pathlib import Path


path = Path('path/to/target/directory/')
list_files = (fp for fp in os.listdir(path) if Path(fp).is_file())


def parser():
    os.chdir(path)

    for name in list_files:
        title = re.search(r'([a-z|A-Z]+)_.', os.path.splitext(name)[0])
        new_name = title.group(1)

        if not Path(new_name).is_dir():
            Path(new_name).mkdir(parents=True, exist_ok=True)
        shutil.move(name, new_name)


if __name__ == '__main__':
    parser()
