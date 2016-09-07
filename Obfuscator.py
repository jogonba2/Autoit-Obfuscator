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

def header():
    print """
                                                                               
    ,----..                                                      .--,-``-.     
   /   /   \      ,---,.     ,---,.   ,---,                     /   /     '.   
  /   .     :   ,'  .'  \  ,'  .' |  '  .' \               ,--,/ ../        ;  
 .   /   ;.  \,---.' .' |,---.'   | /  ;    '.           ,'_ /|\ ``\  .`-    ' 
.   ;   /  ` ;|   |  |: ||   |   .':  :       \     .--. |  | : \___\/   \   : 
;   |  ; \ ; |:   :  :  /:   :  :  :  |   /\   \  ,'_ /| :  . |      \   :   | 
|   :  | ; | ':   |    ; :   |  |-,|  :  ' ;.   : |  ' | |  . .      /  /   /  
.   |  ' ' ' :|   :     \|   :  ;/||  |  ;/  \   \|  | ' |  | |      \  \   \  
'   ;  \; /  ||   |   . ||   |   .''  :  | \  \ ,':  | | :  ' ;  ___ /   :   | 
 \   \  ',  / '   :  '; |'   :  '  |  |  '  '--'  |  ; ' |  | ' /   /\   /   : 
  ;   :    /  |   |  | ; |   |  |  |  :  :        :  | : ;  ; |/ ,,/  ',-    . 
   \   \ .'   |   :   /  |   :  \  |  | ,'        '  :  `--'   \ ''\        ;  
    `---`     |   | ,'   |   | ,'  `--''          :  ,      .-./\   \     .'   
              `----'     `----'                    `--`----'     `--`-,,-'     
									    
-------------------------------------------------------------------------------								    
       """
def footer(): print "\n\n"+"-"*25," Overxfl0w13 ","-"*25,"\n"

def obfuscate(orig_name,dest_name,it,replace_includes,rm_comments_by_tag,rm_comments_by_semicolon, rm_comments_by_hash, \
	      rm_regions,add_regs,hide_func_names,hide_var_names,add_hard_funcs,add_hard_funcs_calls,add_true_guard_statements,add_vars,add_comm, \
	      add_init_blocks,add_end_blocks,add_mid_blocks,add_user_funcs, \
	      add_func_calls,hide_strings_replace,hide_strings_shuffle,hide_strings_flip_two,hide_strings_reverse, hide_strings_split, hide_strings_rotate, hide_strings_hexify, \
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
    
    print "-"*35+" GENERAL "+"-"*35+"\n"
    
    print "\r"+Messages.extracting_code,
    obj  = Utils.extract_code(orig_name)
    print "\r"+Messages.extracting_code+" "+Messages.correct_symbol
    
    if replace_includes:
	print "\r"+Messages.extracting_files,
	Utils.extract_directories_files()
	print "\r"+Messages.extracting_files+" "+Messages.correct_symbol
	print "\r"+Messages.replacing_includes,
	obj  = UnifyIncludes.replace_includes(obj,Globals.directories_files)
	print "\r"+Messages.replacing_includes+" "+Messages.correct_symbol
    
    print "\n\n"
    
    print ("-"*35+" OBFUSCATE "+"-"*35)[:-2]+"\n"
    
    if rm_comments_by_tag:
	print "\r"+Messages.removing_comments_by_tag,
	code = Utils.get_string_from_obj(obj)
	code = RemoveCode.remove_comments_by_tag(code)
	obj  = Utils.get_obj_from_code(code)
	print "\r"+Messages.removing_comments_by_tag+" "+Messages.correct_symbol
	
    if rm_comments_by_semicolon:
	print "\r"+Messages.removing_comments_by_scol,
	obj  = RemoveCode.remove_comments_by_semicolon(obj)
	print "\r"+Messages.removing_comments_by_scol+" "+Messages.correct_symbol
	
    if rm_comments_by_hash:
	print "\r"+Messages.removing_comments_by_hash,
	obj  = RemoveCode.remove_comments_by_hash(obj)
	print "\r"+Messages.removing_comments_by_hash+" "+Messages.correct_symbol
	
    if rm_regions:
	print "\r"+Messages.removing_regions,
	obj  = RemoveCode.remove_region_directive(obj)
	print "\r"+Messages.removing_regions+" "+Messages.correct_symbol
    
    if hide_func_names:
	print "\r"+Messages.hiding_function_names,
	obj  = HideIdentifiers.hide_function_names(obj)	
	print "\r"+Messages.hiding_function_names+" "+Messages.correct_symbol
	
    if add_hard_funcs:
	print "\r"+Messages.adding_hardcoded_functs,
	obj  = AddJunkCode.add_hardcoded_funcs(obj,add_calls=add_hard_funcs_calls,n_funcs_min = hardcoded_n_funcs_min,n_funcs_max = hardcoded_n_funcs_max)
	print "\r"+Messages.adding_hardcoded_functs+" "+Messages.correct_symbol
	
    if hide_var_names:
	print "\r"+Messages.hiding_variable_names,
	obj  = HideIdentifiers.hide_variable_names(obj)
	print "\r"+Messages.hiding_variable_names+" "+Messages.correct_symbol
	
    if add_true_guard_statements:
	print "\r"+Messages.adding_true_guard_sttmnts,
	AddJunkCode.add_true_guard_statements(obj)
	print "\r"+Messages.adding_true_guard_sttmnts," "+Messages.correct_symbol
	
    if hide_strings_replace:
	print "\r"+Messages.adding_code_string_rplce,
	obj  = AddJunkCode.add_hardcoded_string_modifiers(obj,HardcodedPrograms.replace_string)
	print "\r"+Messages.adding_code_string_rplce+" "+Messages.correct_symbol
	
    if hide_strings_flip_two:
	print "\r"+Messages.adding_code_flip_two,
	obj  = AddJunkCode.add_hardcoded_string_modifiers(obj,HardcodedPrograms.flip_two_string)
	print "\r"+Messages.adding_code_flip_two+" "+Messages.correct_symbol
	
    if hide_strings_reverse:
	print "\r"+Messages.adding_code_reverse,
	obj  = AddJunkCode.add_hardcoded_string_modifiers(obj,HardcodedPrograms.reverse_string)
	print "\r"+Messages.adding_code_reverse+" "+Messages.correct_symbol
	
    if hide_strings_rotate:
	print "\r"+Messages.adding_code_rotate,
	obj  = AddJunkCode.add_hardcoded_string_modifiers(obj,HardcodedPrograms.rotate_string)
	print "\r"+Messages.adding_code_rotate+" "+Messages.correct_symbol
    
    if add_directives:
	print "\r"+Messages.adding_directives,
	obj  = AddJunkCode.add_random_directives(obj)
	print "\r"+Messages.adding_directives+" "+Messages.correct_symbol
	
    for i in xrange(max(0,it)):
	try:
	    if add_regs:
		print "\r"+Messages.adding_regions,
		obj  = AddJunkCode.add_regions(obj)
		print "\r"+Messages.adding_regions+" "+Messages.correct_symbol
		
	    if add_vars:
		print "\r"+Messages.adding_variables,
		obj  = AddJunkCode.add_variables(obj)
		print "\r"+Messages.adding_variables+" "+Messages.correct_symbol
		
	    if add_comm:
		print "\r"+Messages.adding_comments,
		obj  = AddJunkCode.add_comments(obj)
		print "\r"+Messages.adding_comments+" "+Messages.correct_symbol
		
	    if add_mid_blocks:
		print "\r"+Messages.adding_mid_blocks,
		obj  = AddJunkCode.add_blocks(obj,mid_prob_block,mid_n_statements_min,mid_n_statements_max,mid_n_guard_statements_min,mid_n_guard_statements_max,mid_n_else_if_min,mid_n_else_if_max,mid_deep_max,mid_case_values_min,mid_case_values_max)
		print "\r"+Messages.adding_mid_blocks+" "+Messages.correct_symbol
		
	    if add_init_blocks:
		print "\r"+Messages.adding_init_blocks,
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
		print "\r"+Messages.adding_init_blocks+" "+Messages.correct_symbol
		
	    if add_end_blocks:
		print "\r"+Messages.adding_end_blocks,
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
		print "\r"+Messages.adding_end_blocks+" "+Messages.correct_symbol
		
	    if add_user_funcs:
		print "\r"+Messages.adding_functions,
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
		print "\r"+Messages.adding_functions+" "+Messages.correct_symbol
							  
	    if add_func_calls:
		print "\r"+Messages.adding_function_calls,
		obj  = AddJunkCode.add_function_calls(obj)
		print "\r"+Messages.adding_function_calls+" "+Messages.correct_symbol
		
	    if hide_strings_rotate:
		print "\r"+Messages.hiding_strings_rotate,
		obj  = HideStrings.hide_strings_rotate(obj)
		print "\r"+Messages.hiding_strings_rotate+" "+Messages.correct_symbol
		
	    if hide_strings_flip_two:
		print "\r"+Messages.hiding_strings_flip_two,
		obj  = HideStrings.hide_strings_flip_two(obj)
		print "\r"+Messages.hiding_strings_flip_two+" "+Messages.correct_symbol
		
	    if hide_strings_replace:
		print "\r"+Messages.hiding_strings_replace,
		obj  = HideStrings.hide_strings_replace(obj)
		print "\r"+Messages.hiding_strings_replace+" "+Messages.correct_symbol
		
	    if hide_strings_shuffle:
		print "\r"+Messages.hiding_strings_shuffle,
		obj  = HideStrings.hide_strings_definition_shuffle(obj)
		print "\r"+Messages.hiding_strings_shuffle+" "+Messages.correct_symbol
		
	    if hide_strings_reverse:
		print "\r"+Messages.hiding_strings_reverse,
		obj  = HideStrings.hide_strings_reverse(obj)
		print "\r"+Messages.hiding_strings_reverse+" "+Messages.correct_symbol
		
	    if hide_strings_hexify:
		print "\r"+Messages.hiding_strings_hexify,
		obj  = HideStrings.hide_strings_hexify(obj)
		print "\r"+Messages.hiding_strings_hexify+" "+Messages.correct_symbol
		
	    if hide_strings_split:
		print "\r"+Messages.hiding_strings_split,
		obj  = HideStrings.hide_strings_split(obj)
		print "\r"+Messages.hiding_strings_split+" "+Messages.correct_symbol
		
	    if hide_numbers:
		print "\r"+Messages.hiding_numbers,
		obj  = HideNumbers.hide_numbers(obj,hide_numbers_deep_max_min,hide_numbers_deep_max_max)
		print "\r"+Messages.hiding_numbers+" "+Messages.correct_symbol
	
	except RuntimeError as re: print "\n\n"+" "+orig_name+" "+Messages.sad_end,Messages.stack_overflow_error+"\n"
	except IOError as ie:      print "\n\n"+" "+orig_name+" "+Messages.sad_end,Messages.file_error+"\n"
	except Exception as e:     print "\n\n"+Messages.unknown_error+"\n\n",e , "\n\n"
    
    print "\n\n"
    
    print ("-"*35+" ADD JUNK "+"-"*35)[:-1]+"\n"
    
    if add_tabs:
	print "\r"+Messages.adding_tabs,
	obj  = HideLines.add_random_tabs(obj)
	print "\r"+Messages.adding_tabs+" "+Messages.correct_symbol
	
    if add_to_eof:
	print "\r"+Messages.adding_to_eof,
	obj  = AddJunkCode.add_to_eof(obj,size=eof_fill_kb)
	print "\r"+Messages.adding_to_eof+" "+Messages.correct_symbol
    
    print "\n\n"
    
    print ("-"*35+" WRITING "+"-"*35)[:-1]+"\n"
    
    print "\r"+Messages.writing_code,
    Utils.write_code(Utils.get_string_from_obj(obj),dest_name)
    print "\r"+Messages.writing_code+" "+Messages.correct_symbol
    
    print "\n\n"
    
    print ("-"*35+" RESULTS "+"-"*35)[:-1]+"\n"
    print "\n\n"+Messages.correct_symbol+" "+orig_name+" "+Messages.happy_end+" "+dest_name	
    
    if add_init_blocks or add_end_blocks or add_mid_blocks or add_func_calls or add_hard_funcs_calls:
	print "\n\n"+Messages.advertisement_symbol+" "+Messages.time_advertisement+"\n\n"
    
def usage(): print "Usage: "+argv[0]+" original_code_file obfuscated_code_file iterations icon\n\n"
    
if __name__ == "__main__":
    
    #######################
    ## Obfuscator params ##
    #######################
    
    orig_name = "./TestScripts/Ind_Server.au3"
    dest_name =  "./TestScripts/ind_server_mod.au3"
    it        = 1
    replace_includes   = False
    rm_comments_by_tag = True #
    rm_comments_by_semicolon = True #
    rm_comments_by_hash      =  True #
    rm_regions = True#
    add_regs   = True#
    hide_func_names = True#
    hide_var_names = True#
    add_hard_funcs = True#
    add_hard_funcs_calls = True#
    add_true_guard_statements = True#
    add_vars = True#
    add_comm = True#
    add_init_blocks = True#
    add_end_blocks  = True#
    add_mid_blocks  = True#
    add_user_funcs  = True#
    add_func_calls  = True#
    hide_strings_replace       = False
    hide_strings_shuffle       = False
    hide_strings_flip_two      = True#
    hide_strings_reverse       = True#
    hide_strings_split         = True#
    hide_strings_rotate        = True#
    hide_strings_hexify        = True#
    hide_numbers         = True#
    add_directives       = False
    add_tabs             = False
    add_to_eof           = False
    
    ########################
    ## Hardcoded params   ##
    ########################
    
    hardcoded_n_funcs_min = 1
    hardcoded_n_funcs_max = 4
    
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
    
    mid_prob_block               = 0.15
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
	      rm_regions,add_regs,hide_func_names,hide_var_names,add_hard_funcs,add_hard_funcs_calls,add_true_guard_statements,add_vars,add_comm, \
	      add_init_blocks,add_end_blocks,add_mid_blocks,add_user_funcs, \
	      add_func_calls,hide_strings_replace,hide_strings_shuffle,hide_strings_flip_two,hide_strings_reverse, hide_strings_split, hide_strings_rotate, hide_strings_hexify, \
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
