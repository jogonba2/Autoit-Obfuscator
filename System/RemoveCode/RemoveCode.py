#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('../')

from Structures.Graphs import Graph
from Kernel import Utils
from re import sub,DOTALL

## Requiere el código estructurado ##
def remove_comments_by_semicolon(obj): 
    for i in xrange(len(obj)):
	obj[i] = obj[i][obj[i].rfind(";")+1:]
    return obj

def remove_comments_by_hash(obj):
    res = []
    for i in xrange(len(obj)): 
	aux = obj[i].strip()
	if len(aux)>0 and aux[0]!="#" and not "include" in aux: res.append(obj[i])
    return res
    
def remove_region_directive(obj):
    for i in xrange(len(obj)):
	aux = obj[i].lower().strip()
	if aux.find("#region")==0 or aux.find("#endregion")==0: obj[i] = "\n"
    return obj
	
def remove_comments_by_comment_tag(code): return sub(r"#comments-start.*#comments-end[^\n]*","",code,flags=DOTALL)
def remove_comments_by_c_tag(code): return sub(r"#cs.*#ce[^\n]*","",code,flags=DOTALL)
def remove_comments_by_tag(code): return remove_comments_by_c_tag(remove_comments_by_comment_tag(code))

########################################

if __name__ == "__main__":
    a = Utils.extract_code("runpe_danyfirex.au3")
    a = Utils.get_string_from_code(a)
    a = remove_comments(a)
    print a
