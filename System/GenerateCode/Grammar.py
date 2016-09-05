#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('../')
from Kernel import Utils,ExtractKeywords,Config,Globals
from random import randint,choice,uniform
from string import lowercase,uppercase,letters
from re import findall

def variable(length_min=30,length_max=50):   return "$"+"".join([choice(lowercase+uppercase) for i in xrange(randint(length_min,length_max))])

def integer(min_range=-1000,max_range=1000): return str(randint(min_range,max_range))

def abs_integer(min_range=-1000,max_range=1000): return str(abs(randint(min_range,max_range)))

def real(min_range=-1000,max_range=1000):   return str(uniform(min_range,max_range))

def abs_real(min_range=-1000,max_range=1000): return str(abs(uniform(min_range,max_range)))

def string(length_min=5,length_max=10):      return '"'+variable(length_min,length_max)[1:]+'"'

def ascii_char(): return "'"+choice(letters)+"'"

def macro(): return choice(Config.MACROS)

def function(arity): return choice(Config.FUNCTIONS_ONE_ARITY)

def enum(n_enumeration_min=1,n_enumeration_max=3,length_min=5,length_max=10):
    rnd_enum = randint(n_enumeration_min,n_enumeration_max)
    r        = Utils.low_up_string("Local Enum ")
    rnd_step = randint(0,1)
    if rnd_step==1:       r   += Utils.low_up_string("Step ")+enum_stepval()+" "
    for i in xrange(rnd_enum):
	var = variable(length_min,length_max)
	val = value()
	r  += var_definition(var,val)
	if i != rnd_enum-1: r += ", "
	else:               r += " "
    return r
    
def enum_stepval(): return choice([abs_integer(),'*'+abs_integer(),'+'+abs_integer(),'-'+abs_integer()])

def ternary_operation(n_guard_statements_min=1,n_guard_statements_max=3):
    res          = ""
    declarations = ""
    var          = variable()
    n_guard_statements = randint(min(n_guard_statements_min,n_guard_statements_max),
				 min(n_guard_statements_min,n_guard_statements_max))
    log_statements = logical_statements(n_guard_statements)
    logic_variables = ExtractKeywords.extract_variables(log_statements)
    res += Utils.generate_random_declarator()+var+"\n"
    for i in logic_variables: declarations += Utils.generate_random_declarator()+assign_by_var_name(i)+"\n"
    res         += var+" = (" + log_statements + ") ? " + value() + " : " + value()
    return declarations+res+"\n"
    
# Permitir usar los parámetros #
def value(min_range=-1000,max_range=1000):
    # 0 -> integer, 1-> char , 2 -> string , 3 -> float, 4 -> macro #
    random_value = randint(0,4)#,2)
    rnd_eval     = randint(0,1)
    if random_value==0:      
	if rnd_eval == 0: return integer(min_range,max_range)
	else:             return "Eval('"+integer(min_range,max_range)+"')"
    if random_value==1:      
	if rnd_eval == 0: return ascii_char()
	else:             return "Eval("+ascii_char()+")" 
    elif random_value==2:    
	if rnd_eval == 0: return string()
	else:             return "Eval("+string()+")" 
    elif random_value==3: 
	if rnd_eval == 0: return real()
	else:             return "Eval('"+real()+"')" 
    elif random_value==4: return macro()

def relational_operation(): return choice([">","<",">=","<=","<>","="])

def arithmetic_operation(): return choice(['+','-','*','/'])
def arithmetic_assign():    return choice(['+=','-=','*=','/='])

def var_definition(var,val): return var + " = " + val 

def assign(var,val):
    rnd = randint(0,1)
    if rnd==0: return Utils.generate_random_declarator()+var+" = "+val+"\n"
    else:      return Utils.generate_random_declarator()+var+" = 0\n"+Utils.low_up_string("Assign")+"('"+var+"','"+val.replace('"',"").replace("'","")+"')\n"
	    
def logical_operation(): return choice([Utils.low_up_string("And"),Utils.low_up_string("Or")])

def logical_statement(spaces_min=1,spaces_max=5): return variable()+" "+relational_operation()+" "+value() # Facilita las cosas un formato estándar #

def logical_statements(n_statements,spaces_min=1,spaces_max=5):
    statements = ""
    for i in xrange(n_statements):
	statements += logical_statement(spaces_min,spaces_max) 
	if i<n_statements-1: statements += " " + logical_operation() + " "
    return statements

def assign_by_var_name(var_name): return var_name+" = "+value()

def assign_full(var_name,value):  return var_name+" = "+str(value)

# n_else_if al menos 1 para Switch! #
def block(deep_act,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000): 
    res = ""
    if deep_act>=deep_max: res += simple_block(n_statements_min,n_statements_max)+"\n"
    else:
	block_type = randint(0,7)# 0->simple,1->if,2->for,3->switch,4->for object,5->with,6->while,7->do until #
	if block_type==0:   res += simple_block(n_statements_min,n_statements_max)+"\n"
	elif block_type==1: res += block_if(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
	elif block_type==2: res += block_for(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
	elif block_type==3: res += block_switch(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
	elif block_type==4: res += block_for_object(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
	elif block_type==5: res += block_with(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
	elif block_type==6: res += block_while(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
	elif block_type==7: res += block_do_until(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
    return res
    
def simple_block(n_statements_min=10,n_statements_max=20): 
    n_statements = randint(min(n_statements_min,n_statements_max),max(n_statements_min,n_statements_max))
    variables    = [variable() for i in xrange(n_statements)]
    values       = [value() for i in xrange(n_statements)]
    res = ""
    for i in xrange(n_statements): res += assign(variables[i],values[i])+"\n"
    #res += enum(1,3,5,10) + "\n"
    #elif rnd==2: res += ternary_operation(1,3)
    for i in xrange(n_statements/2):
	""" -3 -> ternary
	    -2 -> enum
	    -1 -> arithmetic assign
	    0  -> f arity 0
	    1  -> f arity 1
	    2  -> f arity 2
	"""
	arity = randint(-1,2)
	if arity==-1:   
	    r,rp  = randint(0,len(variables)-1),randint(0,len(variables)-1)
	    res  += variables[r]+" "+arithmetic_assign()+" "+variables[rp]+"\n"
	elif arity==0:  res  += Utils.low_up_string(choice(Config.FUNCTIONS_ZERO_ARITY)) + "()\n"
	elif arity==1:  
	    r,rf,rp  = randint(0,len(variables)-1),randint(0,len(Config.FUNCTIONS_ONE_ARITY)-1),randint(0,len(variables)-1)
	    res  += variables[r]+" "+arithmetic_assign()+" "+Utils.low_up_string(Config.FUNCTIONS_ONE_ARITY[rf])+"("+variables[rp]+")\n"
	elif arity==2:
	    r,rf,rp,rt = randint(0,len(variables)-1),randint(0,len(Config.FUNCTIONS_TWO_ARITY)-1),randint(0,len(variables)-1),randint(0,len(variables)-1)
	    res  += variables[r]+" "+arithmetic_assign()+" "+Utils.low_up_string(Config.FUNCTIONS_TWO_ARITY[rf])+"("+variables[rp]+","+variables[rt]+")\n"
    return res

def block_do_until(deep_act,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000): 
    # Generalizar bucles do ... until con más de una condición en la guarda, incrementos variables y variabilidad en la actualización de variables (incrementar parte derecha = decrementar parte izquierda) #
    var_one,val_one = variable(),integer()
    var_two,val_two = variable(),integer()
    declarations    = Utils.generate_random_declarator() + var_one + " = " + val_one + "\n" +\
		      Utils.generate_random_declarator() + var_two + " = " + val_two + "\n"
    rel_op          = choice([">","<",">=","<=","<>"])
    res             = Utils.low_up_string(" Do \n") + \
		      block(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,
			    n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,
			    case_values_max)+"\n"
    if   rel_op == ">":   	res        += var_one + " += 1\n"
    elif rel_op == "<":  	res        += var_one + " -= 1\n"
    elif rel_op == ">=":  	res        += var_one + " += 1\n"
    elif rel_op == "<=":  	res        += var_one + " -= 1\n"
    elif rel_op == "<>":  	res        += var_one + " += 1\n"
    elif rel_op == "=": 
	v_max = max(val_one,val_two)
	if v_max == val_one:    res += var_one + " -= 1\n"
	else:                   res += var_two + " -= 1\n"
    res            += Utils.low_up_string(" Until ") + var_one + rel_op + var_two + "\n"
    return declarations+res
	
def block_while(deep_act,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000): 
    # Generalizar bucles while con más de una condición en la guarda, incrementos variables y variabilidad en la actualización de variables (incrementar parte derecha = decrementar parte izquierda) #
    var_one,val_one = variable(),integer()
    var_two,val_two = variable(),integer()
    declarations    = Utils.generate_random_declarator() + var_one + " = " + val_one + "\n" +\
		      Utils.generate_random_declarator() + var_two + " = " + val_two + "\n"
    rel_op          = choice([">","<",">=","<=","="])#relational_operation()
    res             = Utils.low_up_string(" While ")+var_one+rel_op+var_two+"\n"+ \
		      block(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,
			    n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,
			    case_values_max)+"\n"
			    
    if   rel_op == ">":   	res        += var_one + " -= 1\n"
    elif rel_op == "<":  	res        += var_one + " += 1\n"
    elif rel_op == ">=":  	res        += var_one + " -= 1\n"
    elif rel_op == "<=":  	res        += var_one + " += 1\n"
    elif rel_op == "=":   	res        += var_one + " += 1\n"
    elif rel_op == "<>": 
	v_max = max(val_one,val_two)
	if v_max == val_one:    res += var_one + " -= 1\n"
	else:                   res += var_two + " -= 1\n"
    res += Utils.low_up_string("\nWEnd\n")
    return declarations+res 
    
    
def block_if(deep_act,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000): 
    res = Utils.low_up_string("If ")
    declarations = ""
    n_guard_statements = randint(min(n_guard_statements_min,n_guard_statements_max),max(n_guard_statements_min,n_guard_statements_max))
    log_statements = logical_statements(n_guard_statements) + Utils.low_up_string(" Then")+"\n"
    logic_variables = ExtractKeywords.extract_variables(log_statements)
    for i in logic_variables: declarations += Utils.generate_random_declarator()+assign_by_var_name(i)+"\n"
    res += log_statements
    res += block(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)+"\n"
    else_type = randint(0,1) # 0 -> Else if, 1 -> Else #
    if else_type==0: 
	n_else_if = randint(min(n_else_if_min,n_else_if_max),max(n_else_if_min,n_else_if_max))
	for i in xrange(n_else_if):	    
	    log_statements = logical_statements(randint(min(n_guard_statements_min,n_guard_statements_max),max(n_guard_statements_min,n_guard_statements_max)))
	    logic_variables = ExtractKeywords.extract_variables(log_statements)
	    for i in logic_variables: declarations += Utils.generate_random_declarator()+assign_by_var_name(i)+"\n"
	    res += Utils.low_up_string("ElseIf ")+log_statements+Utils.low_up_string(" Then\n")+block(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)+"\n"
    res += Utils.low_up_string("Else ")+"\n"+block(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)+"\n"
    res += Utils.low_up_string("EndIf")+"\n"
    return declarations+res

def block_for(deep_act,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000): 
    a,b = integer(),integer()
    a,b = min(a,b),max(a,b)
    v   = variable()
    declaration = Utils.generate_random_declarator()+assign_by_var_name(v)+"\n\n"
    res = Utils.low_up_string("For ")+assign_full(v,a)+Utils.low_up_string(" To ")+b
    rnd_step = randint(0,1)
    if rnd_step==1:    
	res += Utils.low_up_string(" Step ")+str(randint(1,10))+" \n"
    else:              res += "\n"
    res += block(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,
	         n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,
	         case_values_max)+Utils.low_up_string("\n Next\n")
    return declaration+res

def block_with(deep_act,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000):
    v           = variable()
    declaration = Utils.generate_random_declarator()+v+' = ObjCreate("shell.application") \n'
    res 	= Utils.low_up_string(" With ") + v + "\n" + \
		  block(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,
			n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,
			case_values_max)+Utils.low_up_string("\n EndWith\n")
    return declaration+res
    
def block_for_object(deep_act,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000): 
    v     	= variable()
    v_for 	= variable() 
    declaration = Utils.generate_random_declarator()+v+' = ObjCreate("shell.application") \n'
    res 	= Utils.low_up_string("For ") + v_for+Utils.low_up_string(" In ") + v + "\n" + \
		  block(deep_act+1,n_statements_min,n_statements_max,n_guard_statements_min,
			n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,
			case_values_max)+Utils.low_up_string("\n Next\n")
    return declaration+res
    
def block_switch(deep_act,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000): 
    v = variable()
    declaration = Utils.generate_random_declarator()+assign_by_var_name(v)+"\n"
    n_cases = randint(min(n_else_if_min,n_else_if_max),max(n_else_if_min,n_else_if_max))
    res = Utils.low_up_string("Switch ")+v+"\n" 
    for i in xrange(n_cases):
	a,b = integer(min(case_values_min,case_values_max),max(case_values_min,case_values_max)),integer(min(case_values_min,case_values_max),max(case_values_min,case_values_max))
	a,b = min(a,b),max(a,b)
	res += Utils.low_up_string("Case ")+a+Utils.low_up_string(" To ")+b+"\n"+block(deep_act,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
	res += "\nCase Else\n"+block(deep_act,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)
    res += Utils.low_up_string("\nEndSwitch\n")
    return declaration+res
    
def block_func(arity_min=1,arity_max=4,identifiers_length_min=5,identifiers_length_max=10,n_statements_min=10,n_statements_max=20,n_guard_statements_min=1,n_guard_statements_max=5,n_else_if_min=1,n_else_if_max=5,deep_max=5,case_values_min=-1000,case_values_max=1000):
    id_func,arity = Utils.generate_identifier(identifiers_length_min,identifiers_length_max),randint(min(arity_min,arity_max),max(arity_min,arity_max))
    Config.TDS_FUNCTIONS[id_func]=arity # ¿Sobra?
    res = Utils.low_up_string("Func ")+id_func+"("
    for i in xrange(arity):
	if i<arity-1:  res += variable()+","
	else:          res += variable()
    res += ")\n\n\n"+block(0,n_statements_min,n_statements_max,n_guard_statements_min,n_guard_statements_max,n_else_if_min,n_else_if_max,deep_max,case_values_min,case_values_max)+Utils.low_up_string("\n EndFunc\n")
    Globals.arity_new_functions.append(arity)
    return res

if __name__ == "__main__":
    print block_for(1,deep_max=1)
