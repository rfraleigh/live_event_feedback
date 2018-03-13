import pandas as pd
import os
import json
import time
import random
import pprint
import copy
import names

def strTimeProp(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))

def sortTime(time_array):
    new = []
    for item in time_array:
        new.append(time.mktime(time.strptime(item, '%m/%d/%Y %H:%M')))
    new = sorted(new)
    new_array = []
    for item in new:
        new_array.append(time.strftime('%m/%d/%Y %H:%M', time.localtime(item)))
    return new_array

def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %H:%M', prop)

def generate_timestamps(iterations):
    event_start = "5/20/2018 12:00"
    event_end = "5/20/2018 18:00"
    time_array = [event_start,event_end]
    for i in range(0,iterations):
        temp = copy.deepcopy(time_array)
        first = random.choice(temp)
        temp.pop(time_array.index(first))
        second = random.choice(temp)
        new_date = randomDate(sortTime([first,second])[0],sortTime([first,second])[1],random.randrange(3,7)/10)
        time_array.append(new_date)
    timestamps = sortTime(time_array)
    return timestamps

def generate_name(iterations):
    name = names.get_full_name()
    return [name]*iterations

def generate_classification(iterations):
    name = random.choice(['student','faculty','adult','entrepreneur'])
    return [name]*iterations

def generate_booth(iterations):
    booth_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    booths = copy.deepcopy(booth_labels[0:iterations])
    return random.sample(booths, len(booths))


def generate_value_prop(iterations):
    values = [0,1,2,3,4,5]
    value_prop =[]
    for i in range(0,iterations):
        value_prop.append(random.choice(values))
    return value_prop

def main():
    columns = ['timestamp', 'name', 'group', 'location', 'value_1', 'value_2', 'value_3','location_previous']
    data =pd.DataFrame(columns=columns)
    people = 100
    iterations = 5

    for person in range(0,people):
        t = generate_timestamps(iterations)
        n = generate_name(iterations)
        g = generate_classification(iterations)
        l = generate_booth(iterations)
        v1 = generate_value_prop(iterations)
        v2 = generate_value_prop(iterations)
        v3 = generate_value_prop(iterations)
        l_prev = ['door']+l[0:iterations-1]
        rows = [[t[j],n[j],g[j],l[j],v1[j],v2[j],v3[j],l_prev[j]] for j in range(0,iterations)]
        temp = pd.DataFrame(columns=columns,index=range(0,iterations),data=rows)
        data = pd.concat([data,temp],axis=0,ignore_index=True)
    data.to_csv('dummy_data.csv',index=None)

main()