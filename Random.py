#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:09:17 2021

@author: jacobusking
"""
from Problem_Instance import Problem_Instance
from itertools import combinations
import numpy as np
rnd = np.random
import math

def generate_random_problem_instance(n,p,fleet, dataset_number = 1, demand_min = 10, demand_max = 20, storage_min = 10, storage_max = 20, service_rate = 3, service_fixed = 10, customers_loc_min = 0, customers_loc_max = 100, depot_loc_min = 50,depot_loc_max = 50, max_tw = 540):
    rnd.seed(dataset_number-1)
    locations = generate_locations(range(1,n+1), customers_loc_min, customers_loc_max, depot_loc_min, depot_loc_max)
    q = generate_demand(range(1,n+1), demand_min, demand_max)
    s = generate_service_times(q, service_rate, service_fixed)
    distance_matrix = {(i,j): math.hypot(locations['x'][i] - locations['x'][j], locations['y'][i] - locations['y'][j]) for i in range(n+1) for j in range(n+1)}
    a, b = generate_time_windows(n, max_tw)
    storage = generate_storage(range(1,n+1), storage_min, storage_max)
    f = generate_visitation_frequencies(range(1,n+1), storage, q)
    #f = generate_visitation_frequencies(range(1,n+1))
    pi = generate_problem_instance_visiting_patterns(range(1,n+1), range(1,p+1), f)
    g = generate_fleet_compatibility(n, fleet.nu_vehicle_types)
    return Problem_Instance(n,p,fleet,f,pi,g,q,s,locations,distance_matrix,a,b)

def generate_storage(customers, storage_min, storage_max):
    storage = {}
    for i in customers:
        storage[i] = (storage_min + storage_max)/2
    return storage
    
def generate_demand(customers, demand_min, demand_max):
    demand_range = demand_max - demand_min
    q = {i:rnd.random()*demand_range+demand_min for i in customers}
    return q

def generate_service_times(q, service_rate, service_fixed):
    s = {}
    for i in list(q.keys()):
        s[i] = q[i]*service_rate + service_fixed
    return s

def generate_locations(customers, customers_loc_min, customers_loc_max, depot_loc_min, depot_loc_max):
    customers_loc_range = customers_loc_max - customers_loc_min
    depot_loc_range = depot_loc_max - depot_loc_min
    x = {0:rnd.random()*depot_loc_range + depot_loc_min}
    y = {0:rnd.random()*depot_loc_range + depot_loc_min}
    for i in customers:
        x[i] = rnd.random()*customers_loc_range + customers_loc_min
        y[i] = rnd.random()*customers_loc_range + customers_loc_min
    locations = {'x':x, 'y':y}
    return locations

def generate_time_windows(n, max_tw):
    a = {0:0}
    b = {0:max_tw+60}
    counter = 0
    for i in range(1,n+1):
        if rnd.random() <= 0.5:
        #if counter%2 == 0:
            a[i] = 0
            b[i] = max_tw/2
            #b[i] = max_tw
        else:
            a[i] = max_tw/2
            #a[i] = 0
            b[i] = max_tw
        counter = counter +1
    return a,b

# =============================================================================
# def generate_visitation_frequencies(customers):
#     f_values = {1:1, 2:2, 3:1, 4:2, 5:1, 6:2, 7:1, 8:2, 9:1, 0:3} #Verander 10 na 3
#     f = {i:f_values[i%10+1] for i in customers}
#     return f
# =============================================================================

def generate_visitation_frequencies(customers, storage, q):
    f = {i:math.ceil(q[i]/storage[i]) for i in customers}
    return f
    
def generate_problem_instance_visiting_patterns(customers, periods, f):
    pi = {}
    for i in customers:
        pi[i] = generate_customer_visiting_patterns(periods,f[i])
    return pi

def generate_customer_visiting_patterns(periods, f):
    patterns = list(combinations(periods, f))
    length = len(patterns)
    for i in range(length):
        patterns[i] = set(patterns[i])
    return patterns
    
def generate_fleet_compatibility(n, nu_vehicle_types):
    g = {}
    for i in range(1,n+1):
        g[i] = set(range(1,nu_vehicle_types+1))
    return g
    
    
    
    
    
    
    