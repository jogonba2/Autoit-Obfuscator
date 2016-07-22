#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('../')

from Structures.Graphs import Graph
from Kernel import Utils
from Kernel import ExtractKeywords as ex

def generate_graph(obj):
    obj   = [obj[i] for i in xrange(len(obj)) if not not obj[i].strip()]
    flags = [0,0,0,0,0,0,0,0,0] # while_,do_while_,for_TO,for_IN,func_,if_,select_,switch_,with_
    for line in obj:
	print line
	# Ajustar con Kernel.ExtractKeywords // Cuidado con el orden -> Do While antes de While y demás ..#
	if ex.is_do_while(line): flags[1] = 1
	if ex.is_while(line): flags[0] = 1
	if ex.is_for_to(line): flags[2] = 1
	if ex.is_for_in(line): flags[3] = 1
	if ex.is_func(line): flags[4] = 1
	if ex.is_if(line): flags[5] = 1
	if ex.is_select(line): flags[6] = 1
	if ex.is_switch(line): flags[7] = 1
	if ex.is_with(line): flags[8] = 1
	
	
	
	if ex.is_end_while(line): flags[0] = 0
	if ex.is_until(line): flags[1] = 0
	if ex.is_next(line):
	    if flags[2]==1: flags[2] = 0 # Si es TO #
	    else:           flags[3] = 0 # Si es IN #
	if ex.is_end_func(line): flags[4] = 0
	if ex.is_end_if(line): flags[5] = 0
	if ex.is_end_select(line): flags[6] = 0
	if ex.is_end_switch(line): flags[7] = 0
	if ex.is_end_with(line): flags[8] = 0
	raw_input()
	print flags
    
    
if __name__ == "__main__":
    obj = Utils.remove_comments(Utils.extract_code("test.au3"))
    print generate_graph(obj)
    
