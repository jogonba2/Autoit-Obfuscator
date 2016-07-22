#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('../')
from Kernel import Utils,ExtractKeywords,Config,Globals
from random import randint,choice,uniform
from string import lowercase,uppercase,letters
from re import findall

def variable(length_min=30,length_max=50):   return "$"+"".join([choice(lowercase+uppercase) for i in xrange(randint(length_min,length_max))])

def ascii_char(): return "'"+choice(letters)+"'"

def macro(): return choice(Config.MACROS)

def function(arity): return choice(Config.FUNCTIONS_ONE_ARITY)

# Permitir usar los parámetros #
def value(min_range=-1000,max_range=1000):
    # 0 -> integer, 1-> char , 2 -> string , 3 -> float, 4 -> macro#
    random_value = randint(0,4)#,2)
    if random_value==0:      return integer(min_range,max_range)
    if random_value==1:      return ascii_char()
    elif random_value==2:    return string()
    elif random_value==3:    return real()
    elif random_value==4:    return macro()

def relational_operation(): return choice([">","<",">=","<=","<>","="])

def logical_operation(): return choice(["And","Or"])

def logical_statement(spaces_min=1,spaces_max=5): return variable()+" "+relational_operation()+" "+value() # Facilita las cosas un formato estándar #

def logical_statements(n_statements,spaces_min=1,spaces_max=5):
    statements = ""
    for i in xrange(n_statements):
	statements += logical_statement(spaces_min,spaces_max) 
	if i<n_statements-1: statements += " " + logical_operation() + " "
    return statements

def assign_by_var_name(var_name): return var_name+" = "+value()

def assign_full(var_name,value): return var_name+" = "+str(value)

# n_else_if al menos 1 para Switch! #
def block(deep_act,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000): 
    res = ""
    if deep_act>=deep_max: res += simple_block(n_statements_min,n_statements_max)+"\n"
    else:
	block_type = randint(0,2)# 0->simple,1->if,2->for,3->switch,4->while #
	if block_type==0:   res += simple_block(n_statements_min,n_statements_max)+"\n"
	elif block_type==1: res += block_if(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
	elif block_type==2: res += block_for(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
	elif block_type==3: res += block_switch(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)

    return res
    
def simple_block(n_statements_min=10,n_statements_max=20): # Solo asignaciones (extender con expresiones sobre definiciones)
    n_statements = randint(min(n_statements_min,n_statements_max),max(n_statements_min,n_statements_max))
    variables    = [variable() for i in xrange(n_statements)]
    values       = [value() for i in xrange(n_statements)]
    res = ""
    for i in xrange(n_statements/2):
	arity = randint(-1,2) # Aridades 0,1 y 2 #
	if arity==-1:   
	    r,rp  = randint(0,len(variables)-1),randint(0,len(variables)-1)
	elif arity==0:  res  += choice(Config.FUNCTIONS_ZERO_ARITY) + "()\n"
	elif arity==1:  
	    r,rf,rp  = randint(0,len(variables)-1),randint(0,len(Config.FUNCTIONS_ONE_ARITY)-1),randint(0,len(variables)-1)
	    res  += variables[r]+" "+arithmetic_assign()+" "+Config.FUNCTIONS_ONE_ARITY[rf]+"("+variables[rp]+")\n"
	elif arity==2:
	    r,rf,rp,rt = randint(0,len(variables)-1),randint(0,len(Config.FUNCTIONS_TWO_ARITY)-1),randint(0,len(variables)-1),randint(0,len(variables)-1)
	    res  += variables[r]+" "+arithmetic_assign()+" "+Config.FUNCTIONS_TWO_ARITY[rf]+"("+variables[rp]+","+variables[rt]+")\n"
    return res
    
def block_if(deep_act,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000): 
    res = "If "
    declarations = ""
    n_guard_statements = randint(min(n_guard_statements_min,n_guard_statements_max),max(n_guard_statements_min,n_guard_statements_max))
    log_statements = logical_statements(n_guard_statements) + " Then\n"
    logic_variables = ExtractKeywords.extract_variables(log_statements)
    for i in logic_variables: declarations += "Local "+assign_by_var_name(i)+"\n"
    res += log_statements
    res += block(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)+"\n"
    else_type = randint(0,1) # 0 -> Else if, 1 -> Else #
    if else_type==0: 
	n_else_if = randint(min(n_else_if_min,n_else_if_max),max(n_else_if_min,n_else_if_max))
	for i in xrange(n_else_if):	    
	    log_statements = logical_statements(randint(min(n_guard_statements_min,n_guard_statements_max),max(n_guard_statements_min,n_guard_statements_max)))
	    logic_variables = ExtractKeywords.extract_variables(log_statements)
	    res += "Else \n"+block(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)+"\n"
    res += "EndIf\n"
    return declarations+res
    
def block_for(deep_act,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000): 
    a,b = integer(),integer()
    a,b = min(a,b),max(a,b)
    v   = variable()
    declaration = "Local "+assign_by_var_name(v)+"\n\n"
    res = "For "+assign_full(v,a)+" To "+b+"\n"+block(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)+"\n Next\n"
    return declaration+res


def block_while(deep_act,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000): 
    n_guard_statements = randint(min(n_guard_statements_min,n_guard_statements_max),max(n_guard_statements_min,n_guard_statements_max))
    log_statements,declarations = logical_statements(n_guard_statements),""
    #print logic_variables,relational_operators,const_values
    for i in logic_variables: declarations += "Local "+assign_by_var_name(i)+"\n"
    res = declarations+"\nWhile "+log_statements
    #print res
    return res # Acabar #
    
def block_switch(deep_act,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000): 
    v = variable()
    declaration = "Local "+assign_by_var_name(v)+"\n"
    n_cases = randint(min(n_else_if_min,n_else_if_max),max(n_else_if_min,n_else_if_max))
    res = "Switch "+v+"\n" 
    for i in xrange(n_cases):
	a,b = integer(min(case_values_min,case_values_max),max(case_values_min,case_values_max)),integer(min(case_values_min,case_values_max),max(case_values_min,case_values_max))
	res += "Case "+a+" To "+b+"\n"+block(deep_act,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
    res += "\nEndSwitch\n"
    return declaration+res
    
def block_func(arity_min=1,arity_max=4,identifiers_length_min=5,identifiers_length_max=10,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000):
    id_func,arity = Utils.generate_identifier(identifiers_length_min,identifiers_length_max),randint(min(arity_min,arity_max),max(arity_min,arity_max))
    Config.TDS_FUNCTIONS[id_func]=arity # ¿Sobra?
    res = "Func "+id_func+"("
    for i in xrange(arity): pass
    res += ")\n\n\n"+block(0,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)+"\n EndFunc\n"
    Globals.arity_new_functions.append(arity)
    return res
