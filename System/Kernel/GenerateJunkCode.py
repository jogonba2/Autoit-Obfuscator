#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint,choice
import Config,Globals


def generate_comments(n_comments_min,n_comments_max,comment_length_min,comment_length_max):
    res        = []
    for i in xrange(randint(n_comments_min,n_comments_max)):
	res.append(generate_comment(comment_length_min,comment_length_max))
    return res


    
def generate_variables(n_vars_min,n_vars_max,id_length_min,id_length_max,case_array_min,case_array_max):
    res        = []
    for i in xrange(randint(n_vars_min,n_vars_max)):
	res.append(generate_variable(id_length_min,id_length_max,case_array_min,case_array_max))
    return res
