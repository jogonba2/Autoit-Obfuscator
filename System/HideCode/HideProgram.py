#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('../')
from Kernel import Utils
from Kernel import ExtractKeywords as ex
from GenerateCode import Grammar as g

def hide_code_with_string(obj):
    code  = Utils.get_string_from_obj(obj)
    code  = Utils.standar_quotes(code)
    obj   = Utils.get_obj_from_code(code)
    s_var = g.variable()
    res   = "Local "+s_var+' = "'+obj[0]+'" & _ \n'
    for i in xrange(1,len(obj)-1):
	res += '"'+obj[i]+'" & _ \n'
    res += '"'+obj[len(obj)-1]+'"\n'
    res  += "Local "+g.variable()+" = Execute("+s_var+")\n"
    return res

if __name__ == "__main__":
    obj = Utils.extract_code("test_m3.au3")
    #obj = hide_variable_names(obj)
    #obj = hide_function_names(obj)
    print hide_code_with_string(obj)
    #Utils.write_code(Utils.get_string_from_obj(obj),"test_m3_mod.au3")
    #print generate_graph(obj)
    
