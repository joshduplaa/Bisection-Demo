#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Joshua Duplaa
Problem 1b
"""

#Approximation of the root of f(x) = x^(3)-25
#Using interval[a,b] [2,3]

n = 14      #Iterations
a = 2       #initial lower bound
b = 3       #initial upper bound
i = 1       #current iteration

for x in range(n):
    fun_a = a**3-25
    fun_b = (b**3)-25
    c = (a+b)/2         #Midpoint between a,b
    fun_c = (c**3)-25   
    if(fun_c < 0):
        a = c
    elif(fun_c > 0):
        b = c
    print("Iteration: ", i, "\n", "Approximation: ", c)
    i = i+1
