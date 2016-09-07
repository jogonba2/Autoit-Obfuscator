#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('../')
from Kernel import Utils
from Kernel import ExtractKeywords as ex
from re import sub,search

def hide_variable_names(obj):
    identifiers = list(ex.extract_defined_variables_from_obj(obj)) # Extraer solo las que se definen en el script #
    replaces = Utils.mod_names_hash(identifiers)
    boundary = "\n"+Utils.generate_random_string(20,30)+"\n"
    obj      = boundary.join(obj)
    for i in xrange(len(identifiers)):
	obj = sub(r"\$"+identifiers[i][1:]+r"\b","$"+replaces[i],obj)
	
    return obj.split(boundary)
    
def hide_function_names(obj):
    identifiers = list(ex.extract_func_names_from_obj(obj))
    replaces    = Utils.mod_names_identifier(identifiers)
    obj         = "\n".join(obj)
    for i in xrange(len(identifiers)):
	obj     = sub(r""+identifiers[i]+r"\s*\(",replaces[i]+"(",obj)
    return obj.split("\n")

if __name__ == "__main__":
    obj = Utils.extract_code("test.au3")
    obj = hide_variable_names(obj)
    obj = hide_function_names(obj)
    Utils.write_code(Utils.get_string_from_obj(obj),"testmod.au3")
    #print generate_graph(obj)
    
