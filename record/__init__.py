#!/usr/bin/env python
# coding: utf-8
import time
import csv
import os


def read_record(self):
    index = 0
    if os.path.exists(r'./record.csv'):
        with open('./record.csv', 'r') as f:
            f_csv = csv.reader(f)
            data = [[x.strip() for x in line.strip().split(',')] for line in f.readlines()][-1]
        print('当前地址索引为：' + str(data[0]))
        self.start_index = int(data[0])
    else:
        self.start_index = 0
        self.record_status(0, '', '', time.time())


def record_status(self, i, address, status, time):
    print('写入文件')
    with open('./zksync_record.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow([i, address, status, time])