#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('../')
from Kernel import Utils
from Kernel import ExtractKeywords as ex
from GenerateCode import Grammar as g
from random import uniform


def hide_definitions_with_assign(obj):
    for i in xrange(len(obj)):
	obj[i] = obj[i].strip()
	aux    = obj[i].lower()
	res = ""
	if len(obj[i])>0 and obj[i][-1]!="_" and aux.find("eval(")==-1 and aux.find("assign(")==-1:
	    if obj[i][0]=="$":
		assign_expression = ex.extract_assign_expressions(obj[i])
		if len(assign_expression)>0:
		    assign_expression = assign_expression[0]
		    make = 0 if "'" in assign_expression[2] and '"' in assign_expression[2] else 1
		    if make and ',' not in assign_expression[2] and ';' not in assign_expression[2] and '#' not in assign_expression[2]:
			if assign_expression[1]  == "=":
			    #print assign_expression
			    res += Utils.low_up_string(" Assign('")+assign_expression[0][1:]+"',"+assign_expression[2]+")\n"
			    obj[i] = res
    return obj
	    
def hide_expressions_with_execute(obj):
    for i in xrange(len(obj)):
	obj[i] = obj[i].strip()
	aux    = obj[i].lower()
	prob_execute = 0.75
	res    = ""
	if len(obj[i])>0 and obj[i][-1]!="_" and aux.find("execute(")==-1 and aux.find("eval(")==-1 and aux.find("assign(")==-1:
	    local,dim,glbal = aux.find("local"),aux.find("dim"),aux.find("global")

	    if local==0:
		res += Utils.low_up_string(" Local ")
		
	    elif dim==0:
		res += Utils.low_up_string(" Dim ")
		
	    elif glbal==0:
		res += Utils.low_up_string(" Global ")

	    r = uniform(0,1)
	    if (local==0 or dim==0 or glbal==0 or obj[i][0]=="$") and r<=prob_execute:
		assign_expression = ex.extract_assign_expressions(obj[i])
		if len(assign_expression)>0:
		    assign_expression = assign_expression[0]
		    make = 0 if "'" in assign_expression[2] and '"' in assign_expression[2] else 1
		    if make and "," not in assign_expression[2] and ',' not in assign_expression[2] and ';' not in assign_expression[2] and '#' not in assign_expression[2]: # Evitar definiciones multiples #
			if assign_expression[1]  == "=":
			    quote = repr(assign_expression[2])[0]
			    res  += assign_expression[0] + Utils.low_up_string(" = Execute(")+quote+assign_expression[2]+quote+") \n"
			    obj[i] = res
			elif assign_expression[1] == "+=":
			    quote = repr(assign_expression[2])[0]
			    res += assign_expression[0] + Utils.low_up_string(" = Execute(")+quote+assign_expression[0]+" + "+assign_expression[2]+quote+")\n"
			    obj[i] = res
			elif assign_expression[1] == "-=":
			    quote = repr(assign_expression[2])[0]
			    res += assign_expression[0] + Utils.low_up_string(" = Execute(")+quote+assign_expression[0]+" - "+assign_expression[2]+quote+")\n"
			    obj[i] = res
			elif assign_expression[1] == "*=":
			    quote = repr(assign_expression[2])[0]
			    res += assign_expression[0] + Utils.low_up_string(" = Execute(")+quote+assign_expression[0]+" * "+assign_expression[2]+quote+")\n"
			    obj[i] = res
			elif assign_expression[1] == "/=":
			    quote = repr(assign_expression[2])[0]
			    res += assign_expression[0] + Utils.low_up_string(" = Execute(")+quote+assign_expression[0]+" / "+assign_expression[2]+quote+")\n"
			    obj[i] = res
			elif assign_expression[1] == "&=":
			    quote = repr(assign_expression[2])[0]
			    res += assign_expression[0] + Utils.low_up_string(" = Execute(")+quote+assign_expression[0]+" & "+assign_expression[2]+quote+")\n"
			    obj[i] = res
			    
    return obj
	  
	
if __name__ == "__main__":
    pass
    
