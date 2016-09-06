#!/usr/bin/env python
# -*- coding: utf-8 -*-

from System.Kernel import Utils,Config,Messages,Globals
from System.AddCode import AddJunkCode,UnifyIncludes
from System.Hardcoded import HardcodedPrograms
from System.HideCode import HideIdentifiers,HideNumbers,HideStrings,HideLines,HideProgram
from System.RemoveCode import RemoveCode
from System.Reorder import Reorder
from sys import argv
import argparse as ap

def header(): print "\n\n"+"-"*25," OBFAU3 (Autoit Obfuscator) ","-"*25,"\n"
def footer(): print "\n\n"+"-"*25," Overxfl0w13 ","-"*25,"\n"

def obfuscate(orig_name,dest_name,it,replace_includes,rm_comments_by_tag,rm_comments_by_semicolon, rm_comments_by_hash, \
	      rm_regions,add_regs,hide_func_names,hide_var_names,add_hard_funcs,add_true_guard_statements,add_vars,add_comm, \
	      add_init_blocks,add_end_blocks,add_mid_blocks,add_user_funcs, \
	      add_func_calls,hide_strings_replace,hide_strings_shuffle,hide_strings_flip_two,hide_strings_reverse, hide_strings_split, hide_strings_rotate, \
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
    
    if rm_comments_by_hash:
	print "Removing comments with hash #"
	obj  = RemoveCode.remove_comments_by_hash(obj)
	
    if rm_regions:
	print "Removing region directives"
	obj  = RemoveCode.remove_region_directive(obj)
	
    if add_hard_funcs:
	print "Adding hardcoded functions"
	obj  = AddJunkCode.add_hardcoded_funcs(obj,hardcoded_n_funcs_min,hardcoded_n_funcs_max)
	
    if hide_var_names:
	print Messages.hiding_variable_names
	obj  = HideIdentifiers.hide_variable_names(obj)
	
    if hide_func_names:
	print Messages.hiding_function_names
	obj  = HideIdentifiers.hide_function_names(obj)	
    

    
    if add_true_guard_statements:
	print "Adding true guard statements"
	AddJunkCode.add_true_guard_statements(obj)
	
    if hide_strings_replace:
	print "Adding code for hide strings with replace method"
	obj  = AddJunkCode.add_hardcoded_string_modifiers(obj,HardcodedPrograms.replace_string)
    
    if hide_strings_flip_two:
	print "Adding code for hide strings with flip two method"
	obj  = AddJunkCode.add_hardcoded_string_modifiers(obj,HardcodedPrograms.flip_two_string)
	
    if hide_strings_reverse:
	print "Adding code for hide strings with reverse method"
	obj  = AddJunkCode.add_hardcoded_string_modifiers(obj,HardcodedPrograms.reverse_string)
    
    if hide_strings_rotate:
	print "Adding code for hide strings with rotte method"
	obj  = AddJunkCode.add_hardcoded_string_modifiers(obj,HardcodedPrograms.rotate_string)
	
    for i in xrange(max(0,it)):
	try:
	    if add_regs:
		print "Adding new regions"
		obj  = AddJunkCode.add_regions(obj)
		
	    if add_vars:
		print Messages.adding_variables
		obj  = AddJunkCode.add_variables(obj)
		    
	    if add_comm:
		print Messages.adding_comments
		obj  = AddJunkCode.add_comments(obj)
	    
	    if add_mid_blocks:
		print Messages.adding_blocks
		obj  = AddJunkCode.add_blocks(obj,mid_prob_block,mid_n_statements_min,mid_n_statements_max,mid_n_guard_statements_min,mid_n_guard_statements_max,mid_n_else_if_min,mid_n_else_if_max,mid_deep_max,mid_case_values_min,mid_case_values_max)
		
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
	    
	    if hide_strings_rotate:
		print "Hide strings with rotate method..."
		obj  = HideStrings.hide_strings_rotate(obj)
	
	    if hide_strings_flip_two:
		print "Hide strings with two flip method..."
		obj  = HideStrings.hide_strings_flip_two(obj)
	    
	    if hide_strings_replace:
		print "Hide strings with replace method..."
		obj  = HideStrings.hide_strings_replace(obj)
		
	    if hide_strings_shuffle:
		print "Hide string definitions with shuffle method..."
		obj  = HideStrings.hide_strings_definition_shuffle(obj)
	    
	    if hide_strings_reverse:
		print "Hide strings with reverse method..."
		obj  = HideStrings.hide_strings_reverse(obj)
	    
	    if hide_strings_split:
		print "Hide strings with split method..."
		obj  = HideStrings.hide_strings_split(obj)
		
	    if hide_numbers:
		print Messages.hiding_numbers
		obj  = HideNumbers.hide_numbers(obj,hide_numbers_deep_max_min,hide_numbers_deep_max_max)
		
	    if add_directives:
		print Messages.adding_directives
		obj  = AddJunkCode.add_random_directives(obj)
	
	except RuntimeError as re: print "\n\n"+orig_name+Messages.sad_end+"stack overflow because of recursion in block generating, try to reduce deep values and regenerate code :("
	except IOError as ie:      print "\n\n"+orig_name+Messages.sad_end+"file error, probably you have specified an incorrect file name"
	except Exception as e:     print "\n\n An unknown error has occurred, details: \n\n",e , "\n\n"
    
    if add_tabs:
	print Messages.adding_tabs
	obj  = HideLines.add_random_tabs(obj)
    
    if add_to_eof:
	print Messages.adding_to_eof
	obj  = AddJunkCode.add_to_eof(obj,size=eof_fill_kb)
    
    else:
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
    
    orig_name = "./TestScripts/Stub.au3"
    dest_name =  "./TestScripts/Stub_Mod.au3"
    it        = 1
    replace_includes   = False
    rm_comments_by_tag = False
    rm_comments_by_semicolon = False
    rm_comments_by_hash      =  False # Hasta que se repare"
    rm_regions = True#
    add_regs   = True#
    hide_func_names = False#
    hide_var_names = True#
    add_hard_funcs = False#
    add_true_guard_statements = True#
    add_vars = True#
    add_comm = True#
    add_init_blocks = True#
    add_end_blocks  = True#
    add_mid_blocks  = False#
    add_user_funcs  = True#
    add_func_calls  = True
    hide_strings_replace       = False
    hide_strings_shuffle       = False
    hide_strings_flip_two      = True#
    hide_strings_reverse       = True#
    hide_strings_split         = False#
    hide_strings_rotate        = True#
    hide_numbers         = True#
    add_directives       = False
    add_tabs             = False
    add_to_eof           = False
    
    ########################
    ## Hardcoded params   ##
    ########################
    
    hardcoded_n_funcs_min = 1
    hardcoded_n_funcs_max = 5
    
    ########################
    ## Init blocks params ##
    ########################
    
    init_min_blocks          	 = 1
    init_max_blocks          	 = 7
    init_n_statements_min    	 = 1
    init_n_statements_max        = 2
    init_n_guard_statements_min  = 1
    init_n_guard_statements_max  = 5
    init_n_else_if_min		 = 1
    init_n_else_if_max		 = 5
    init_deep_max		 = 2
    init_case_values_min	 = 204
    init_case_values_max	 = 3048

    ########################
    ## End blocks params  ##
    ########################
    
    end_min_blocks          	 = 1
    end_max_blocks          	 = 7
    end_n_statements_min    	 = 1
    end_n_statements_max         = 2
    end_n_guard_statements_min   = 1
    end_n_guard_statements_max   = 5
    end_n_else_if_min		 = 1
    end_n_else_if_max		 = 5
    end_deep_max		 = 2
    end_case_values_min	 	 = 204
    end_case_values_max	 	 = 3048
    
    ########################
    ## Mid blocks params  ##
    ########################
    
    mid_prob_block               = 0.1
    mid_n_statements_min	 = 1
    mid_n_statements_max	 = 2
    mid_n_guard_statements_min	 = 1
    mid_n_guard_statements_max	 = 2
    mid_n_else_if_min		 = 1
    mid_n_else_if_max		 = 2
    mid_deep_max		 = 1
    mid_case_values_min		 = 10
    mid_case_values_max		 = 100
    
    ########################
    ##  Function params   ##
    ########################
    
    func_n_functions_min	 = 1
    func_n_functions_max	 = 10
    func_arity_min 		 = 1
    func_arity_max		 = 5
    func_n_statements_min	 = 1
    func_n_statements_max	 = 8
    func_n_guard_statements_min	 = 1
    func_n_guard_statements_max	 = 2
    func_n_else_if_min		 = 1
    func_n_else_if_max		 = 5
    func_deep_max		 = 2
    func_case_values_min	 = 1078
    func_case_values_max	 = 2039
    
    #########################
    ## Hide numbers params ##
    #########################
    
    hide_numbers_deep_max_min	 = 1
    hide_numbers_deep_max_max 	 = 3
    
    #########################
    ## Hide strings params ##
    #########################
    
    hide_strings_split_chunk_splits = 5
    
    #########################
    ##     EOF params      ##
    #########################
    
    eof_fill_kb = 12
    
    obfuscate(orig_name,dest_name,it,replace_includes,rm_comments_by_tag,rm_comments_by_semicolon, rm_comments_by_hash, \
	      rm_regions,add_regs,hide_func_names,hide_var_names,add_hard_funcs,add_true_guard_statements,add_vars,add_comm, \
	      add_init_blocks,add_end_blocks,add_mid_blocks,add_user_funcs, \
	      add_func_calls,hide_strings_replace,hide_strings_shuffle,hide_strings_flip_two,hide_strings_reverse, hide_strings_split, hide_strings_rotate, \
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
