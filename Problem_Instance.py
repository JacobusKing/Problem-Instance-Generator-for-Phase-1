#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:48:00 2021

@author: jacobusking
"""
class Problem_Instance():
    def __init__(self,n,p,fleet,f,pi,g,q,s,locations,distance_matrix,a,b):
        self.n = n
        self.p = p
        self.fleet = fleet
        self.nodes = range(0,n+1)
        self.customers = range(1,n+1)
        self.periods = range(1,p+1)
        self.pairs = [(i,j) for j in self.periods for i in self.fleet.vehicle_types]
        self.f = f
        self.pi = pi
        self.g = g
        self.q = q
        self.s = s
        self.locations = locations
        self.distance_matrix = distance_matrix
        self.t = self.distance_matrix
        self.a = a
        self.b = b
    

class Settings():
    def __init__(self,w_q,w_tw,mu,lamda,n_close,nbElite, It_div, It_NI, T_max, h):
        self.w_q = w_q
        self.w_tw = w_tw
        self.mu = mu
        self.lamda = lamda
        self.n_close = n_close
        self.nbElite = nbElite
        self.It_div = It_div
        self.It_NI = It_NI
        self.T_max = T_max
        self.h = h