#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint,shuffle

def shuffle_string(s):
    list1_shuf = []
    index_shuf = range(len(s))
    shuffle(index_shuf)
    for i in index_shuf: list1_shuf.append(s[i])
    return "".join(list1_shuf),",".join(map(str,index_shuf))
    
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

def hexify_string(s): return "0x"+"".join("{:02x}".format(ord(c)) for c in s).upper()

if __name__ == "__main__":
    #print rotate_string("abcdef ghijkl mnopqr stuvwx")
    #print hex_string("{8384-3442-2324}")
    print shuffle_string("")
