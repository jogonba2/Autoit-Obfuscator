#!/usr/bin/env python
# -*- coding: utf-8 -*-

from System.Kernel import Utils,Config,Messages,Globals
from System.AddCode import AddJunkCode,UnifyIncludes
from System.Hardcoded import HardcodedPrograms
from System.HideCode import HideIdentifiers,HideNumbers,HideStrings,HideLines
from System.RemoveCode import RemoveCode
from System.Reorder import Reorder
from sys import argv
import argparse as ap

def header(): print "\n\n"+"*"*25," AutoIt Obfuscation ","*"*25,"\n"
def footer(): print "\n\n***************************** Overxfl0w13 *****************************\n"

def obfuscate(orig_name,dest_name,it,replace_includes,rm_comments_by_tag,rm_comments_by_semicolon, \
	      rm_regions,add_regs,hide_func_names,hide_var_names,add_hard_funcs,add_vars,add_comm, \
	      add_init_blocks,add_end_blocks,add_mid_blocks,add_user_funcs, \
	      add_func_calls,hide_strings_replace,hide_strings_shuffle,hide_strings_cipher,\
	      hide_numbers,add_directives,add_tabs,add_to_eof,hardcoded_n_funcs_min,\
	      hardcoded_n_funcs_max,init_min_blocks,init_max_blocks,init_n_statements_min,init_n_statements_max,\
	      init_n_guard_statements_min,init_n_guard_statements_max,init_n_else_if_min,init_n_else_if_max,\
	      init_deep_max,init_case_values_min,init_case_values_max,end_min_blocks,end_max_blocks,\
	      end_n_statements_min,end_n_statements_max,end_n_guard_statements_min,end_n_guard_statements_max,\
	      end_n_else_if_min,end_n_else_if_max,end_deep_max,end_case_values_min,end_case_values_max,\
	      mid_prob_block,mid_n_statements_min,mid_n_statements_max,mid_n_guard_statements_min,\
	      mid_n_guard_statements_max,mid_n_else_if_min,mid_n_else_if_max,mid_deep_max,mid_case_values_min,\
	      mid_case_values_max,func_n_functions_min,func_n_functions_max,func_arity_min,func_arity_max,\
	      func_n_statements_min,func_n_statements_max,func_n_guard_statements_min,func_n_guard_statements_max,\
	      func_n_else_if_min,func_n_else_if_max,func_deep_max,func_case_values_min,func_case_values_max,\
	      hide_numbers_deep_max_min,hide_numbers_deep_max_max,eof_fill_kb):
		  
    header()
    
    print Messages.extracting_code
    obj  = Utils.extract_code(orig_name)
    
    if replace_includes:
	print "Extracting files from directories..."
	Utils.extract_directories_files()
	print "Replacing includes.."
	obj  = UnifyIncludes.replace_includes(obj,Globals.directories_files)
	
    if rm_comments_by_tag:
	print Messages.removing_comments
	code = Utils.get_string_from_obj(obj)
	code = RemoveCode.remove_comments_by_tag(code)
	obj  = Utils.get_obj_from_code(code)
	
    if rm_comments_by_semicolon:
	print "Removing comments with semicolon"
	obj  = RemoveCode.remove_comments_by_semicolon(obj)
	
    if rm_regions:
	print "Removing region directives"
	obj  = RemoveCode.remove_region_directive(obj)
	
    if hide_func_names:
	print Messages.hiding_function_names
	obj  = HideIdentifiers.hide_function_names(obj)	
	
    for i in xrange(max(0,it)):
	try:
	    if add_regs:
		print "Adding new regions"
		obj  = AddJunkCode.add_regions(obj)
		
	    if add_hard_funcs:
		print "Adding hardcoded functions"
		obj  = AddJunkCode.add_hardcoded_funcs(obj,hardcoded_n_funcs_min,hardcoded_n_funcs_max)
		    
	    if hide_var_names:
		print Messages.hiding_variable_names
		obj  = HideIdentifiers.hide_variable_names(obj)
		
	    if add_vars:
		print Messages.adding_variables
		obj  = AddJunkCode.add_variables(obj)
		    
	    if add_comm:
		print Messages.adding_comments
		obj  = AddJunkCode.add_comments(obj)
		    
	    if add_init_blocks:
		print "Adding blocks at init"
		obj  = AddJunkCode.add_blocks_to_init(obj,min_blocks_init=init_min_blocks,
							  max_blocks_init=init_max_blocks,
							  n_statements_min=init_n_statements_min,
							  n_statements_max=init_n_statements_max,
							  n_guard_statements_min=init_n_guard_statements_min,
							  n_guard_statements_max=init_n_guard_statements_max,
							  n_else_if_min=init_n_else_if_min,
							  n_else_if_max=init_n_else_if_max,
							  deep_max=init_deep_max,
							  case_values_min=init_case_values_min,
							  case_values_max=init_case_values_max)
		
	    if add_end_blocks:
		print "Adding blocks at end"
		obj  = AddJunkCode.add_blocks_to_end(obj,min_blocks_end=end_min_blocks,
							 max_blocks_end=end_max_blocks,
							 n_statements_min=end_n_statements_min,
							 n_statements_max=end_n_statements_max,
							 n_guard_statements_min=end_n_guard_statements_min,
							 n_guard_statements_max=end_n_guard_statements_max,
							 n_else_if_min=end_n_else_if_min,
							 n_else_if_max=end_n_else_if_max,
							 deep_max=end_deep_max,
							 case_values_min=end_case_values_min,
							 case_values_max=end_case_values_max)
		
	    if add_mid_blocks:
		print Messages.adding_blocks
		obj  = AddJunkCode.add_blocks(obj,mid_prob_block,mid_n_statements_min,mid_n_statements_max,mid_n_guard_statements_min,mid_n_guard_statements_max,mid_n_else_if_min,mid_n_else_if_max,mid_deep_max,mid_case_values_min,mid_case_values_max)
		
	    if add_user_funcs:
		print Messages.adding_functions
		obj  = AddJunkCode.add_user_functions(obj,n_functions_min=func_n_functions_min,
							  n_functions_max=func_n_functions_max,
							  arity_min=func_arity_min,
							  arity_max=func_arity_max,
							  n_statements_min=func_n_statements_min,
							  n_statements_max=func_n_statements_max,
							  n_guard_statements_min=func_n_guard_statements_min,
							  n_guard_statements_max=func_n_guard_statements_max,
							  n_else_if_min=func_n_else_if_min,
							  n_else_if_max=func_n_else_if_max,
							  deep_max=func_deep_max,
							  case_values_min=func_case_values_min,
							  case_values_max=func_case_values_max)
							  
	    if add_func_calls:
		print Messages.adding_function_calls
		obj  = AddJunkCode.add_function_calls(obj)
	       
	    if hide_strings_cipher:
		print Message.NOT_IMPLEMENTED
	    
	    if hide_strings_replace:
		print "Ocultando strings con metodo replace"
		obj  = HideStrings.hide_strings_string_replace(obj)
		
	    if hide_strings_shuffle:
		print "Ocultando definiciones de strings con metodo shuffle"
		obj  = HideStrings.hide_strings_definition_shuffle(obj)
	       
	    if hide_numbers:
		print Messages.hiding_numbers
		obj  = HideNumbers.hide_numbers(obj,hide_numbers_deep_max_min,hide_numbers_deep_max_max)
		
	    if add_directives:
		print Messages.adding_directives
		obj  = AddJunkCode.add_random_directives(obj)
	
	except RuntimeError as re: print "\n\n"+orig_name+Messages.sad_end+"stack overflow because of recursion in block generating, try to reduce deep values and regenerate code :("
	except IOError as ie:      print "\n\n"+orig_name+Messages.sad_end+"file error, probably you have specified an incorrect file name"
	except Exception as e:     print "\n\n An unknown error has occurred! \n\n"
    
    if add_tabs:
	print Messages.adding_tabs
	obj  = HideLines.add_random_tabs(obj)
    
    if add_to_eof:
	print Messages.adding_to_eof
	obj  = AddJunkCode.add_to_eof(obj,size=eof_fill_kb)
    
    print Messages.writing_code
    Utils.write_code(Utils.get_string_from_obj(obj),dest_name)
    print "\n\n! "+orig_name+Messages.happy_end+dest_name+" :)"	
    print "\n? it's probably that obfuscated code takes to run or even not work, then readjusts parameters and generates a new obfuscated code or simply generate it."
    footer()
    
def usage(): print "Usage: "+argv[0]+" original_code_file obfuscated_code_file iterations icon\n\n"
    
if __name__ == "__main__":
    
    #######################
    ## Obfuscator params ##
    #######################
    
    orig_name = "./TestScripts/Gen.au3"
    dest_name =  "./TestScripts/gen_mod.au3"
    it        = 1
    replace_includes   = 0
    rm_comments_by_tag = 1
    rm_comments_by_semicolon = 0
    rm_regions = 1
    add_regs   = 1
    hide_func_names = 1
    hide_var_names = 1
    add_hard_funcs = 1
    add_vars = 1
    add_comm = 1
    add_init_blocks = 1
    add_end_blocks  = 1
    add_mid_blocks  = 1
    add_user_funcs  = 1
    add_func_calls  = 1
    hide_strings_replace = 0
    hide_strings_shuffle = 0
    hide_strings_cipher  = 0
    hide_numbers         = 1
    add_directives       = 1
    add_tabs             = 0
    add_to_eof           = 0
    
    ########################
    ## Hardcoded params   ##
    ########################
    
    hardcoded_n_funcs_min = 1
    hardcoded_n_funcs_max = 3
    
    ########################
    ## Init blocks params ##
    ########################
    
    init_min_blocks          	 = 2
    init_max_blocks          	 = 4
    init_n_statements_min    	 = 1
    init_n_statements_max        = 2 
    init_n_guard_statements_min  = 1
    init_n_guard_statements_max  = 2
    init_n_else_if_min		 = 2
    init_n_else_if_max		 = 3
    init_deep_max		 = 2
    init_case_values_min	 = 204
    init_case_values_max	 = 3048

    ########################
    ## End blocks params  ##
    ########################
    
    end_min_blocks          	 = 2
    end_max_blocks          	 = 6
    end_n_statements_min    	 = 1
    end_n_statements_max         = 2 
    end_n_guard_statements_min   = 1
    end_n_guard_statements_max   = 2
    end_n_else_if_min		 = 2
    end_n_else_if_max		 = 3
    end_deep_max		 = 2
    end_case_values_min	 	 = 204
    end_case_values_max	 	 = 3048
    
    ########################
    ## Mid blocks params  ##
    ########################
    
    mid_prob_block               = 0.85
    mid_n_statements_min	 = 1
    mid_n_statements_max	 = 5
    mid_n_guard_statements_min	 = 2
    mid_n_guard_statements_max	 = 3
    mid_n_else_if_min		 = 2
    mid_n_else_if_max		 = 3
    mid_deep_max		 = 3
    mid_case_values_min		 = 204
    mid_case_values_max		 = 3048
    
    ########################
    ##  Function params   ##
    ########################
    
    func_n_functions_min	 = 1
    func_n_functions_max	 = 3
    func_arity_min 		 = 2
    func_arity_max		 = 4
    func_n_statements_min	 = 3
    func_n_statements_max	 = 4
    func_n_guard_statements_min	 = 2
    func_n_guard_statements_max	 = 4
    func_n_else_if_min		 = 1
    func_n_else_if_max		 = 5
    func_deep_max		 = 2
    func_case_values_min	 = 1078
    func_case_values_max	 = 2039
    
    #########################
    ## Hide numbers params ##
    #########################
    
    hide_numbers_deep_max_min	 = 1
    hide_numbers_deep_max_max 	 = 5
    
    #########################
    ##     EOF params      ##
    #########################
    
    eof_fill_kb = 12

    obfuscate(orig_name,dest_name,it,replace_includes,rm_comments_by_tag,rm_comments_by_semicolon, \
	      rm_regions,add_regs,hide_func_names,hide_var_names,add_hard_funcs,add_vars,add_comm, \
	      add_init_blocks,add_end_blocks,add_mid_blocks,add_user_funcs, \
	      add_func_calls,hide_strings_replace,hide_strings_shuffle,hide_strings_cipher,\
	      hide_numbers,add_directives,add_tabs,add_to_eof,hardcoded_n_funcs_min,\
	      hardcoded_n_funcs_max,init_min_blocks,init_max_blocks,init_n_statements_min,init_n_statements_max,\
	      init_n_guard_statements_min,init_n_guard_statements_max,init_n_else_if_min,init_n_else_if_max,\
	      init_deep_max,init_case_values_min,init_case_values_max,end_min_blocks,end_max_blocks,\
	      end_n_statements_min,end_n_statements_max,end_n_guard_statements_min,end_n_guard_statements_max,\
	      end_n_else_if_min,end_n_else_if_max,end_deep_max,end_case_values_min,end_case_values_max,\
	      mid_prob_block,mid_n_statements_min,mid_n_statements_max,mid_n_guard_statements_min,\
	      mid_n_guard_statements_max,mid_n_else_if_min,mid_n_else_if_max,mid_deep_max,mid_case_values_min,\
	      mid_case_values_max,func_n_functions_min,func_n_functions_max,func_arity_min,func_arity_max,\
	      func_n_statements_min,func_n_statements_max,func_n_guard_statements_min,func_n_guard_statements_max,\
	      func_n_else_if_min,func_n_else_if_max,func_deep_max,func_case_values_min,func_case_values_max,\
	      hide_numbers_deep_max_min,hide_numbers_deep_max_max,eof_fill_kb)
