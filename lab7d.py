#!/usr/bin/env python3
# Student ID: Urmil Rohitkumar Patel
class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        total = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total)

    def change_time(self, seconds):
        new_sec = self.time_to_sec() + seconds
        new_time = sec_to_time(new_sec)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

    def time_to_sec(self):
        return (self.hour * 3600) + (self.minute * 60) + self.second

    def valid_time(self):
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

def sec_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t
