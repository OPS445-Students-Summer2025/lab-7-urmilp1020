#!/usr/bin/env python3
from lab7a import Time, valid_time, format_time

def change_time(time, seconds):
    time.second += seconds
    if valid_time(time) != True:
        while time.second < 0:
            time.second += 60
            time.minute -= 1
        while time.second >= 60:
            time.second -= 60
            time.minute += 1
        while time.minute < 0:
            time.minute += 60
            time.hour -= 1
        while time.minute >= 60:
            time.minute -= 60
            time.hour += 1
    return None
