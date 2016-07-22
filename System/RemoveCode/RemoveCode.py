#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('../')

from Structures.Graphs import Graph
from Kernel import Utils
from re import sub,DOTALL

## Requiere el código estructurado ##
def remove_comments_by_semicolon(obj): 
    for i in xrange(len(obj)): obj[i] = obj[i][obj[i].rfind(";")+1:]
    return obj

	
def remove_comments_by_tag(code): return remove_comments_by_c_tag(remove_comments_by_comment_tag(code))
