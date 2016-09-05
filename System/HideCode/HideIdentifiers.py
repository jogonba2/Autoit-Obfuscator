#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('../')
from Kernel import Utils
from Kernel import ExtractKeywords as ex


def hide_variable_names(obj):
    identifiers = list(ex.extract_defined_variables_from_obj(obj)) # Extraer solo las que se definen en el script #
    replaces = Utils.mod_names_hash(identifiers)
    for i in xrange(len(obj)):
	for j in xrange(len(identifiers)): obj[i] = obj[i].replace(identifiers[j],"$"+replaces[j]) if not not identifiers[j] else obj[i]
    return obj
    
def hide_function_names(obj):
    identifiers = list(ex.extract_func_names_from_obj(obj))
    replaces    = Utils.mod_names_identifier(identifiers)
    for i in xrange(len(obj)):
	for j in xrange(len(identifiers)): obj[i] = obj[i].replace(identifiers[j],replaces[j]) if not not identifiers[j] else obj[i]
    return obj

if __name__ == "__main__":
    obj = Utils.extract_code("test.au3")
    obj = hide_variable_names(obj)
    obj = hide_function_names(obj)
    Utils.write_code(Utils.get_string_from_obj(obj),"testmod.au3")
    #print generate_graph(obj)
    
