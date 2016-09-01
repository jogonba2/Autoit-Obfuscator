#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint,choice
import Config,Globals

def generate_value_by_vocabulary(vocabulary,length_min,length_max):
    return "".join([choice(vocabulary) for _ in xrange(randint(length_min,length_max))])
    
def generate_comment(comment_length_min,comment_length_max):
    return choice(Config.COMMENT_TYPES).replace("*",generate_value_by_vocabulary(Config.COMMENT_VOCABULARY,comment_length_min,comment_length_max))
    
def generate_comments(n_comments_min,n_comments_max,comment_length_min,comment_length_max):
    res        = []
    for i in xrange(randint(n_comments_min,n_comments_max)):
	res.append(generate_comment(comment_length_min,comment_length_max))
    return res

def generate_variable(id_length_min,id_length_max,case_array_min,case_array_max):
    case_array = randint(0,1)
    var_name = "$"+generate_value_by_vocabulary(Config.VARIABLE_VOCABULARY,id_length_min,id_length_max)
    var        = choice(Config.VARIABLE_TYPES).replace("*",var_name)
    Globals.defined_new_variables.append(var_name)
    return var
    
def generate_variables(n_vars_min,n_vars_max,id_length_min,id_length_max,case_array_min,case_array_max):
    res        = []
    for i in xrange(randint(n_vars_min,n_vars_max)):
	res.append(generate_variable(id_length_min,id_length_max,case_array_min,case_array_max))
    return res

#print len(generate_comments(5,15,100,200))
#print generate_variables(1,5,5,10,100,200)
