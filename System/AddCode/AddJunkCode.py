#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('./System')
from Kernel import GenerateJunkCode,Utils,Globals
from Kernel import ExtractKeywords as ex
from Hardcoded import HardcodedPrograms as hp
from GenerateCode import Grammar as g
from GenerateCode import Directives as d
from random import sample,randint,choice,shuffle
from re import split

def add_true_guard_statements(obj,n_true_guard_statements_min=3,n_true_guard_statements_max=5):
    for i in xrange(len(obj)):
	n_guard_statements = randint(min(n_true_guard_statements_min,n_true_guard_statements_max),
				     max(n_true_guard_statements_min,n_true_guard_statements_max))
				     
	if ex.is_if(obj[i]) or ex.is_else_if(obj[i]) or  \
			    ex.is_while(obj[i]) or ex.is_until(obj[i]):
	    true_guard_statements = ""
	    obj[i] = obj[i].strip()
	    splitted              = split("\s",obj[i])
	    for j in xrange(n_guard_statements):
		true_guard_statements += Utils.generate_true_statement(n_min_value=100,n_max_value=300)
		true_guard_statements += Utils.low_up_string(" And ")
	    obj[i] = splitted[0] + " " + true_guard_statements + " " + " ".join(splitted[1:]) + " "
    return obj
	    
def add_comments(obj,n_comments_min=5,n_comments_max=20,comment_length_min=30,comment_length_max=200):
    comments = GenerateJunkCode.generate_comments(n_comments_min,n_comments_max,comment_length_min,comment_length_max)
    pos = sample(range(max(len(obj),len(comments))),max(len(obj),len(comments)))
    for i in xrange(len(comments)): 
	if pos[i]==0: obj.insert(pos[i],comments[i]); continue 
	else: 
	    if pos[i]-1>len(obj): obj.append(comments[i])
	    else:
		bl = obj[pos[i]-1].strip()
		if len(bl)>0 and '_' not in bl: obj.insert(pos[i],comments[i])
    return obj
    
def add_variables(obj,n_vars_min=5,n_vars_max=10,id_length_min=100,id_length_max=500,case_array_min=10,case_array_max=100):
    variables = GenerateJunkCode.generate_variables(n_vars_min,n_vars_max,id_length_min,id_length_max,case_array_min,case_array_max)
    pos = sample(range(max(len(obj),len(variables))),max(len(obj),len(variables)))
    for i in xrange(len(variables)):
	if pos[i]==0: obj.insert(pos[i],variables[i]); continue 
	else: 
	    if pos[i]-1>len(obj): obj.append(variables[i])
	    else:
		bl = obj[pos[i]-1].strip()
		if len(bl)>0 and '_' not in bl: obj.insert(pos[i],variables[i])
    return obj

def add_to_eof(obj,char="_",size=64):
    size = size*1024*8 # In b #
    n_elems = size/8 # -> size*1024 #
    obj.append(char*n_elems)
    return obj

def add_block(obj,pos,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000):
    obj.insert(pos,g.block(0,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max))
    return obj

def add_blocks_to_init(obj,min_blocks_init=10,max_blocks_init=20,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000):
    n_blocks = randint(min(min_blocks_init,max_blocks_init),max(min_blocks_init,max_blocks_init))
    for i in xrange(n_blocks):
	obj = add_block(obj,0,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
    return obj

def add_blocks_to_end(obj,min_blocks_end=10,max_blocks_end=20,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000):
    n_blocks = randint(min(min_blocks_end,max_blocks_end),max(min_blocks_end,max_blocks_end))  
    for i in xrange(n_blocks):
	obj = add_block(obj,len(obj)-1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
    return obj
    
def add_blocks(obj,prob_add_block=0.7,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000):
    block_lines = sample(range(len(obj)),int(len(obj)*prob_add_block))
    for i in xrange(len(block_lines)):
	if block_lines[i]==0: obj = add_block(obj,0,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
	else:
	    ant_line = obj[block_lines[i]-1].strip()
	    if len(ant_line)>0 and ant_line[-1]!='_': 
		obj = add_block(obj,block_lines[i],n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
    return obj
    
def add_user_function(obj,pos,arity_min=1,arity_max=4,identifiers_length_min=5,identifiers_length_max=10,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000):
    obj.insert(pos,g.block_func(arity_min,arity_max,identifiers_length_min,identifiers_length_max,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max))
    Globals.defined_new_functions.append(obj[pos][obj[pos].find(" "):obj[pos].find("(")])
    return obj
    
def add_user_functions(obj,n_functions_min=5,n_functions_max=10,arity_min=1,arity_max=4,identifiers_length_min=5,identifiers_length_max=10,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000):
    n_functions = randint(min(n_functions_min,n_functions_max),max(n_functions_min,n_functions_max))
    for i in xrange(n_functions):
	random_pos = choice([0,len(obj)])
	obj = add_user_function(obj,random_pos,arity_min,arity_max,identifiers_length_min,identifiers_length_max,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
    return obj

def add_pragma_directives(obj,n_directives_min=5,n_directives_max=20):
    obj.insert(0,d.random_pragma_directives(n_directives_min,n_directives_max))
    return obj
    
def add_include_directives(obj,n_includes_min=10,n_includes_max=20):
    obj.insert(0,d.random_includes(n_includes_min,n_includes_max))
    return obj

def add_autoit_on_start_directive(obj,func_name=Utils.generate_random_string(ext="")): 
    obj.insert(0,d.on_autoit_start_register(func_name))
    return obj

def add_no_tray_icon_directive(obj):
    obj.insert(0,d.no_tray_icon())
    return obj

def add_include_once_directive(obj):
    obj.insert(0,d.include_once())
    return obj

# Prob 1/n constante para toda directiva #
def add_random_directives(obj,n_directives_min=5,n_directives_max=20,n_includes_min=10,n_includes_max=20,func_name=Utils.generate_random_string(ext="")):
    pragma,include,start,tray,once = randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1)
    if start:   obj = add_autoit_on_start_directive(obj,func_name)
    if tray:    obj = add_no_tray_icon_directive(obj)
    if include: obj = add_include_directives(obj,n_includes_min,n_includes_max)
    if once:    obj = add_include_once_directive(obj)
    if pragma:  obj = add_pragma_directives(obj,n_directives_min,n_directives_max)
    return obj

def add_regions(obj,n_regions_min=5,n_regions_max=10,id_length_min=5,id_length_max=10):
    n_regions       = randint(n_regions_min,n_regions_max)
    pos_regions     = [randint(0,len(obj)-1) for i in xrange(n_regions)]
    pos_end_regions = [randint(pos_regions[i]+1,len(obj)-1) for i in xrange(n_regions) if pos_regions[i]+1<len(obj)-1]
    while len(pos_end_regions)<n_regions: pos_end_regions.append(randint(0,len(obj)-1))
    for i in xrange(n_regions):
	id_length = randint(id_length_min,id_length_max)
	if pos_regions[i]>0 and pos_end_regions[i]>0:
	    ant_line_init_region = obj[pos_regions[i]-1].strip()
	    ant_line_end_region  = obj[pos_end_regions[i]-1].strip()
	    if len(ant_line_init_region)>0 and len(ant_line_end_region)>0 and ant_line_init_region[-1]!='_' and ant_line_end_region[-1]!='_':
		obj.insert(pos_regions[i],"#region "+Utils.generate_random_key(id_length)+"\n")
		obj.insert(pos_end_regions[i],"#endregion\n\n")
    return obj
    
def add_function_calls(obj,functions=Globals.defined_new_functions,arity=Globals.arity_new_functions):
    for i in xrange(len(functions)):
	param_names = [g.value() for j in xrange(arity[i])]
	random_pos  = choice([0,-1])
	obj.insert(random_pos,functions[i]+"("+",".join(param_names)+")\n\n")
    return obj

def add_hardcoded_funcs(obj,add_calls=False,functions=Globals.defined_new_functions,arity=Globals.arity_new_functions,n_funcs_min=3,n_funcs_max=5):
    n_funcs = randint(min(n_funcs_min,n_funcs_max),max(n_funcs_min,n_funcs_max))
    shuffle(hp.HARDCODED_PROGRAMS)
    funcs   = hp.HARDCODED_PROGRAMS[:n_funcs]
    for i in xrange(n_funcs):
	function_code   = funcs[i]()
	obj.insert(0,function_code+"\n\n")
	if add_calls:
	    arity           = Globals.arity_new_functions[-1]
	    identifier      = Globals.defined_new_functions[-1]
	    params          = ",".join([g.value() for i in xrange(arity)])
	    obj.insert(0,Utils.low_up_string(Utils.generate_random_declarator()) + \
		       g.variable() + " = " + identifier + "("+params+")\n\n")
    return obj

def add_hardcoded_string_modifiers(obj,hardcoded_function):
    obj.insert(0,hardcoded_function()+"\n\n")
    return obj

if __name__ == "__main__":
    obj = Utils.extract_code("test.au3")
    obj = add_comments(obj)
    obj = add_variables(obj)
    Utils.write_code(Utils.get_string_from_code(obj),"test_mod.au3")
    
