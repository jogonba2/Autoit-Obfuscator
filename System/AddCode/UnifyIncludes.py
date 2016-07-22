#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('../')
from Kernel import Utils
from Kernel import ExtractKeywords as ex

def replace_includes(obj,directories_files):
    for i in xrange(len(obj)):
	include = ex.extract_includes(obj[i])
	if include:
	    if path_content!=None: obj[i] = Utils.read_file(path_content)
    return obj
	    
    
 

