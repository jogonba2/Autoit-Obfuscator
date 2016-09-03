#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import match,findall,compile,search
## ARREGLAR --> OCURRENCIAS EXACTAS DE LAS PALABRAS CON REGEXP ##

## IF ##
def is_if(line): return 1 if "If" in line else 0
def is_else_if(line): return 1 if "ElseIf" in line else 0
def is_else(line): return 1 if "Else" in line else 0
def is_end_if(line): return 1 if "EndIf" in line else 0
########

## SELECT && SWITCH ##
def is_select(line): return 1 if "Select" in line else 0
def is_case(line): return 1 if "Case" in line else 0
def is_case_else(line): return 1 if match(".*Case.*Else",line) else 0
def is_end_select(line): return 1 if "EndSelect" in line else 0
def is_switch(line): return 1 if "Switch" in line else 0
def is_end_switch(line): return 1 if "EndSwitch" in line else 0
######################

## FOR LOOPS ##
def is_for_to(line): return 1 if match(".*For.*To.*",line) else 0
def is_for_in(line): return 1 if match(".*For.*In.*",line) else 0
def is_next(line): return 1 if "Next" in line else 0
###############

## WHILE LOOPS ##
def is_while(line): return 1 if "While" in line else 0
def is_end_while(line): return 1 if "WEnd" in line else 0
#################

## DO WHILE LOOPS ##
def is_do_while(line): return 1 if "Do" in line else 0
def is_until(line): return 1 if "Until" in line else 0
####################

## WITH ##
def is_with(line): return 1 if "With" in line else 0
def is_end_with(line): return 1 if "EndWith" in line else 0
##########

## FUNC ##
def is_func(line): return 1 if "Func" in line else 0
def is_end_func(line): return 1 if "EndFunc" in line else 0
##########

## COMMENTS ##
def extract_comments_by_semicolon(line): return findall(r";[^\n]*","",line)
def extract_comments_by_comments_tag(line): return findall(r"#comments-start.*#comments-end[^\n]*","",line)
def extract_comments_by_c_tag(line): return findall(r"#cs.*#ce[^\n]*","",line)
##############

## VARIABLES ##
def extract_variables(line): return findall("(\$\w*)",line)
    
def extract_variables_from_obj(obj):
    identifiers = set()
    for line in obj: identifiers = identifiers.union(set(extract_variables(line)))
    return identifiers
#################

## FUNC NAMES ##
def extract_func_names(line): return findall(".*Func (\w*).*",line)
def extract_func_names_from_obj(obj): 
    identifiers = set()
    for line in obj: identifiers = identifiers.union(set(extract_func_names(line)))
    return identifiers
################

## STRING DEFINITIONS ##
def extract_string_definition(line): return findall("(.*\$\w*)\s*=\s*[\"\'](.*)[\"\']",line)
def extract_string(line): return findall("[\"\'][^\"\']*[\"\']",line)
########################

## VALUES ##
def extract_integer(line): return findall("\s+([-]?\d+)+",line)
def extract_float(line):   return findall(" ([-]?\d+\.\d+) ",line)
def extract_relational_operators(line): return findall("(<=|>=|=|<>|>|<)",line)
############

## FILES INCLUDED ##
def extract_includes(line):
    p = compile('#include ["<][aA-zZ]+[0-9]*\.au3[">]')
    if p.search(line) is not None:
        return p.search(line).group().replace("#include ", "").replace('"', "").replace("<","").replace(">","")
####################
