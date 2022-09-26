#!/usr/bin/env python3

import sys
import re
from math import ceil

pattern = r'^(?P<Date>.*?)(?P<Hours>\d):(?P<Minutes>\d{2})'

def extract_time(regex, time):
    for _ in time.split('\n'):
        t = regex.match(_).groupdict()
        yield t['Date'], int(t['Hours'])*60, int(t['Minutes'])


def time_converter(time):
    regex = re.compile(pattern)
    return [{d: sum(map(lambda m: 6*ceil(m/6)/60, _))} \
        for d, *_ in extract_time(regex, time)]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(time_converter(sys.argv[1]))