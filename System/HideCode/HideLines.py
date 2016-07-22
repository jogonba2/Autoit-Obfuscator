#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('./System')
from random import randint,sample
from Kernel import Utils
from Kernel import Config

def add_random_tabs(obj,tabs_min=10,tabs_max=30):
    tabs = randint(min(tabs_min,tabs_max),max(tabs_min,tabs_max))
    for i in xrange(len(obj)): obj[i] = obj[i].replace(" ","\t"*tabs)
    return obj
    
def add_non_sense_characters_end_line(obj): pass
