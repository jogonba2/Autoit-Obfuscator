#!/usr/bin/env python
# -*- coding: utf-8 -*-

def flip_two_modifier(s):
    r,i = "",0
    while i<len(s)-1:
	r += s[i+1] + s[i]
	i += 2
    if len(s)%2!=0: r += s[-1]
    return r
    

def binary_modifier(s,i,j):
    if i>=j: return ""
    else: return s[m] + binary_modifier(s,((i+j)//2)+1,j) + binary_modifier(s,i,(i+j)//2)
