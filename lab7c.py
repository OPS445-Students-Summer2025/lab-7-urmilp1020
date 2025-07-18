#!/usr/bin/env python3
from lab7a import Time
def time_to_sec(time):
    minutes = time.hour * 60 + time.minute
    return minutes * 60 + time.second

def sec_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    total_sec = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_sec)

def change_time(time, seconds):
    total_sec = time_to_sec(time) + seconds
    new_time = sec_to_time(total_sec)
    time.hour, time.minute, time.second = new_time.hour, new_time.minute, new_time.second
    return None
def format_time(t):
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

