#!/usr/bin/env python
# -*- coding: utf-8 -*-

try: import pickle as pickle
except: import cpickle as pickle
from re import sub,DOTALL
from random import shuffle
import hashlib as h
from random import choice,randint
from string import lowercase,uppercase
from math import e,log
from os import getcwd,walk
from sys import argv
import Globals

def extract_code(f):
    with open(f,'r') as fd: return fd.read().split('\n')
    
def write_code(obj,f):
    with open(f,'w') as fd: fd.write(obj)

def serialize_code(obj,f):
    with open(f,'wb') as fd: pickle.dump(obj,fd)
    
def unserialize_code(f):
    with open(f,'rb') as fd: return pickle.load(fd)

def get_string_from_obj(obj):
    return '\n'.join(obj)

def shuffle_string(s): return shuffle([c for c in s])

def generate_identifier(length_min=10,length_max=15): return "".join([choice(lowercase+uppercase) for i in xrange(randint(length_min,length_max))])

def mod_names_hash(names):
    replaces = []
    for name in names:
	hash_func = h.new(choice(list(h.algorithms_available))) ; hash_func.update(name)
	replaces.append(hash_func.hexdigest())
    return replaces
    
def mod_names_identifier(names,length_min=10,length_max=30):
    replaces = []
    for name in names: replaces.append(generate_identifier(length_min,length_max))
    return replaces

def get_obj_from_code(code): return code.split("\n")

def generate_char_repeated_randomly(c,f_min,f_max): return c*randint(min(f_min,f_max),max(f_min,f_max))

def generate_random_line(vocabulary,len_line,end="_"): 
    line = [" "]
    for i in xrange(len_line): line.append(r)
    return "".join(line+end)

def escape_quotes(code):
    code = sub('"',"'",code)
    return code

def standar_quotes(code):
    return sub('"',"'",code)
    
def extract_directories_files():
    name_orig = argv[1][argv[1].rfind("/")+1:]
    for t in walk(getcwd()):
        for i in t[2]:
            if name_orig != i and i.split(".")[-1] == "au3": Globals.directories_files[i] = t[0]+"\\"+i

def read_file(path_file):
    with open(path_file,"r") as fd: return fd.read()
    
def generate_random_string(length_min=5,length_max=10,ext=".exe"): return "".join([choice(lowercase+uppercase) for i in xrange(randint(min(length_min,length_max),max(length_min,length_max)))])+ext

def generate_random_key(B): return "".join([choice(lowercase+uppercase) for i in xrange(B)])

def generate_random_declarator(): return choice([low_up_string("Dim "),low_up_string("Local "),low_up_string("Global ")])

def generate_true_statement(n_min_value=100,n_max_value=300):
    statement = choice(["=","<=",">=","<",">","<>"])
    n_min_value,n_max_value = min(n_min_value,n_max_value),max(n_min_value,n_max_value)
    if statement == "=": 
	rnd = str(randint(n_min_value,n_max_value))
	return  rnd + " " + statement + " " + rnd
	
    elif statement == "<=":
	rnd_left   = randint(n_min_value,n_max_value)
	rnd_right  = randint(rnd_left,n_max_value)+1 # +1 para cubrirme, rnd_left también valdría #
	return  str(rnd_left) + " " + statement + " " + str(rnd_right)
	
    elif statement == ">=":
	rnd_left   = randint(n_min_value,n_max_value)
	rnd_right  = randint(n_min_value,rnd_left)-1 # Lo mismo con -1 #
	return  str(rnd_left) + " " + statement + " " + str(rnd_right)
    
    elif statement == "<":
	rnd_left   = randint(n_min_value,n_max_value)
	rnd_right  = randint(rnd_left,n_max_value)+1
	return  str(rnd_left) + " " + statement + " " + str(rnd_right)
	
    elif statement == ">":
	rnd_left   = randint(n_min_value,n_max_value)
	rnd_right  = randint(n_min_value,rnd_left)-1
	return  str(rnd_left) + " " + statement + " " + str(rnd_right)
	
    elif statement == "<>":
	rnd_left   = randint(n_min_value,n_max_value)
	rnd_right  = rnd_left
	while rnd_right==rnd_left: rnd_right = randint(n_min_value,n_max_value)
	return  str(rnd_left) + " " + statement + " " + str(rnd_right)
	
def low_up_string(s):
    res = ""
    for i in xrange(len(s)):
	rnd = randint(0,1)
	if rnd==0: res += s[i].lower()
	else:      res += s[i].upper()
    return res

def add_random_char_between_string(s,c):
    r = ""
    for i in xrange(len(s)):
	rnd = randint(0,1)
	if rnd==1: r += s[i]+c
	else:      r += s[i]
    return r
	
def sum(a,b): return a+b
#def sub(a,b): return a-b
def dot(a,b): return a*b
def div(a,b): return a/b
def exp(a): return e**a
def log(a): return log(a)

if __name__ == "__main__":
    #for i in xrange(1000000):
    #	print eval(generate_true_statement(5,10))
    #print add_random_char_between_string("holaamigo","s")
    #a = extract_code("test.au3")
    #a = get_string_from_code(a)
    #a = remove_comments(a)
    #print a
    """
    write_code(a,"test2.au3")
    serialize_code(a,"test2.bin")
    b = unserialize_code("test2.bin")
    print b
    """
