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

def extract_directories_files():
    name_orig = argv[1][argv[1].rfind("/")+1:]
    for t in walk(getcwd()):
        for i in t[2]:
            if name_orig != i and i.split(".")[-1] == "au3": Globals.directories_files[i] = t[0]+"\\"+i

def read_file(path_file):
    with open(path_file,"r") as fd: return fd.read()
    
def generate_random_string(length_min=5,length_max=10,ext=".exe"): return "".join([choice(lowercase+uppercase) for i in xrange(randint(min(length_min,length_max),max(length_min,length_max)))])+ext

def generate_random_key(B): return "".join([choice(lowercase+uppercase) for i in xrange(B)])

def sum(a,b): return a+b
def sub(a,b): return a-b
def dot(a,b): return a*b
def div(a,b): return a/b
def exp(a): return e**a
def log(a): return log(a)

