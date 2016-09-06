#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

def rotate_string(s):
    rnd = randint(0,len(s)-1)
    return (s[rnd:]+s[:rnd],rnd)
    
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

def split_string(s,chunk_size=3): 
    r        = ""
    chunks   = []
    for i in xrange(0,len(s),chunk_size):
	chunk = s[i:i+chunk_size]
	if "'" in chunk:   chunks.append('"'+chunk+'"')
	elif '"' in chunk: chunks.append("'"+chunk+"'")
	else:              chunks.append('"'+chunk+'"')
    new_line = randint(1,15)
    for i in xrange(len(chunks)):
	if i % new_line == 0 and i != 0: r += " _ \n"
	r += chunks[i]
	if i<len(chunks)-1: r += " & "
    return r

if __name__ == "__main__":
    print rotate_string("abcdef ghijkl mnopqr stuvwx")

