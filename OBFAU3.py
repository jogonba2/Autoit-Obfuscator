#!/usr/bin/env python
# -*- coding: utf-8 -*-

from System.Kernel import Utils,Config,Globals
from System.AddCode import AddJunkCode,UnifyIncludes
from System.Hardcoded import HardcodedPrograms
from System.HideCode import HideIdentifiers,HideNumbers,HideStrings,HideLines,HideProgram
from System.RemoveCode import RemoveCode
from System.Reorder import Reorder
from sys import argv
import argparse as ap
import ConfigParser 
import Languages.English as Messages

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

def obfuscate(orig_name,dest_name,it,replace_includes,rm_comments_by_tag,rm_comments_by_semicolon, rm_comments_by_hash, \
	      rm_regions,add_regs,hide_func_names,hide_var_names,hide_func_params,add_hard_funcs,add_hard_funcs_calls,add_true_guard_statements,add_vars,add_comm, \
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

    try:
	print "-"*35+Messages.general_process+"-"*35+"\n"
	
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
	
	print ("-"*35+Messages.obfuscate_process+"-"*35)[:-2]+"\n"
	
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

	if hide_func_params:
	    print "\r"+Messages.hiding_function_params,
	    obj  = HideIdentifiers.hide_function_parameters(obj)
	    print "\r"+Messages.hiding_function_params+" "+Messages.correct_symbol
	    
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
	
	if hide_strings_shuffle:
	    print "\r"+Messages.adding_code_string_shffle,
	    obj  = AddJunkCode.add_hardcoded_string_modifiers(obj,HardcodedPrograms.shuffle_string)
	    print "\r"+Messages.adding_code_string_shffle," "+Messages.correct_symbol
	    
	if add_directives:
	    print "\r"+Messages.adding_directives,
	    obj  = AddJunkCode.add_random_directives(obj)
	    print "\r"+Messages.adding_directives+" "+Messages.correct_symbol
    except:
	raw_input(Messages.unknown_error)
	
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
	
	except RuntimeError as re: raw_input("\n\n"+" "+orig_name+" "+Messages.sad_end+" "+Messages.stack_overflow_error+"\n")
	except IOError as ie:      raw_input("\n\n"+" "+orig_name+" "+Messages.sad_end+" "+Messages.file_error+"\n")
	except Exception as e:     raw_input("\n\n"+Messages.unknown_error+"\n\n"+" "+ e +"\n\n")
    
    print "\n\n"
    
    try:
	print ("-"*35+Messages.add_junk_process+"-"*35)[:-1]+"\n"
	
	if add_tabs:
	    print "\r"+Messages.adding_tabs,
	    obj  = HideLines.add_random_tabs(obj)
	    print "\r"+Messages.adding_tabs+" "+Messages.correct_symbol
	    
	if add_to_eof:
	    print "\r"+Messages.adding_to_eof,
	    obj  = AddJunkCode.add_to_eof(obj,size=eof_fill_kb)
	    print "\r"+Messages.adding_to_eof+" "+Messages.correct_symbol
	
	print "\n\n"
	
	print ("-"*35+Messages.end_process+"-"*35)[:-1]+"\n"
	
	print "\r"+Messages.writing_code,
	Utils.write_code(Utils.get_string_from_obj(obj),dest_name)
	print "\r"+Messages.writing_code+" "+Messages.correct_symbol
	
    except:
	raw_input(Messages.unknown_error)
	
    print "\n\n"
    
    print ("-"*35+Messages.results_process+"-"*35)[:-1]+"\n"
    print "\n\n"+Messages.correct_symbol+" "+orig_name+" "+Messages.happy_end+" "+dest_name	
    
    if add_init_blocks or add_end_blocks or add_mid_blocks or add_func_calls or add_hard_funcs_calls:
	print "\n\n"+Messages.advertisement_symbol+" "+Messages.time_advertisement+"\n\n"
    

def set_language(language):
    pass
    
if __name__ == "__main__":
    
    #######################
    ## Obfuscator params ##
    #######################
    
    header()
    
    config = ConfigParser.RawConfigParser()
    try:
	config.read("config.ini")
	version   = config.get("ApplicationInfo","Version")
	language  = config.get("ApplicationInfo","Language")
    
	## Set language ##
	if language=="Spanish": import Languages.Spanish as Messages
	elif language=="English": import Languages.English as Messages
	elif language=="Portuguese": import Languages.Portuguese as Messages
	else: import Languages.English as Messages
	##################
	
	orig_name = config.get("ProjectFiles","ScriptToObfuscate") #"./TestScripts/Stub.au3"
	dest_name = config.get("ProjectFiles","ScriptObfuscated")  #"./TestScripts/stub_mod.au3"
	it        = config.getint("General","Iterations") # 1
	replace_includes   = config.getboolean("ProjectFiles","ReplaceIncludes") # False X
	rm_comments_by_tag = config.getboolean("RemoveCode","CommentsByTag") #True # X
	rm_comments_by_semicolon = config.getboolean("RemoveCode","CommentsBySemicolon") #True # X
	rm_comments_by_hash      =  config.getboolean("RemoveCode","CommentsByHash") #True # X
	rm_regions = config.getboolean("RemoveCode","Regions") #True# X
	add_regs   = config.getboolean("AddCode","Regions") #True# X
	hide_func_names = config.getboolean("HideCode","FunctionNames") #True# X
	hide_var_names    = config.getboolean("HideCode","VarNames") #True# X
	hide_func_params = config.getboolean("HideCode","FunctionParams")
	add_hard_funcs = config.getboolean("AddCode","HardcodedFunctions") #False#X
	add_hard_funcs_calls = config.getboolean("AddCode","HardcodedFunctionsCalls") #False# X
	add_true_guard_statements = config.getboolean("AddCode","TrueGuardStatements") #False# X
	add_vars = config.getboolean("AddCode","Variables") #True# X
	add_comm = config.getboolean("AddCode","Comments") # True# X
	add_init_blocks = config.getboolean("AddCode","InitBlocks") #True#
	add_end_blocks  = config.getboolean("AddCode","EndBlocks") #False#
	add_mid_blocks  = config.getboolean("AddCode","MidBlocks") #False#
	add_user_funcs  = config.getboolean("AddCode","UserFuncs") #True#
	add_func_calls  = config.getboolean("AddCode","UserFuncsCalls") #False#
	hide_strings_replace       = config.getboolean("HideCode","StringsReplace") #"False
	hide_strings_shuffle       = config.getboolean("HideCode","StringsShuffle") #False
	hide_strings_flip_two      = config.getboolean("HideCode","StringsFlipTwo") #False#
	hide_strings_reverse       = config.getboolean("HideCode","StringsReverse") #False#
	hide_strings_split         = config.getboolean("HideCode","StringsSplit") #False#
	hide_strings_rotate        = config.getboolean("HideCode","StringsRotate") #True#
	hide_strings_hexify        = config.getboolean("HideCode","StringsHexify") #True#
	hide_numbers         = config.getboolean("HideCode","Numbers") #True#
	add_directives       = config.getboolean("AddCode","Directives") # False
	add_tabs             = config.getboolean("AddJunk","Tabs") #False
	add_to_eof           = config.getboolean("AddJunk","EOF") #
	
	########################
	## Hardcoded params   ##
	########################
	
	hardcoded_n_funcs_min = config.getint("HardcodedFunctionsParams","NFuncsMin")
	hardcoded_n_funcs_max = config.getint("HardcodedFunctionsParams","NFuncsMax")
	
	########################
	## Init blocks params ##
	########################
	
	init_min_blocks          	 = config.getint("InitBlocksParams","MinBlocks")
	init_max_blocks          	 = config.getint("InitBlocksParams","MaxBlocks")
	init_n_statements_min    	 = config.getint("InitBlocksParams","NStatementsMin")
	init_n_statements_max        = config.getint("InitBlocksParams","NStatementsMax")
	init_n_guard_statements_min  = config.getint("InitBlocksParams","NGuardStatementsMin")
	init_n_guard_statements_max  = config.getint("InitBlocksParams","NGuardStatementsMax")
	init_n_else_if_min		 = config.getint("InitBlocksParams","NElseIfMin")
	init_n_else_if_max		 = config.getint("InitBlocksParams","NElseIfMax")
	init_deep_max		 = config.getint("InitBlocksParams","DeepMax")
	init_case_values_min	 = config.getint("InitBlocksParams","CaseValuesMin")
	init_case_values_max	 = config.getint("InitBlocksParams","CaseValuesMax")

	########################
	## End blocks params  ##
	########################
	
	end_min_blocks          	 = config.getint("EndBlocksParams","MinBlocks")
	end_max_blocks          	 = config.getint("EndBlocksParams","MaxBlocks")
	end_n_statements_min    	 = config.getint("EndBlocksParams","NStatementsMin")
	end_n_statements_max         = config.getint("EndBlocksParams","NStatementsMax")
	end_n_guard_statements_min   = config.getint("EndBlocksParams","NGuardStatementsMin")
	end_n_guard_statements_max   = config.getint("EndBlocksParams","NGuardStatementsMax")
	end_n_else_if_min		 = config.getint("EndBlocksParams","NElseIfMin")
	end_n_else_if_max		 = config.getint("EndBlocksParams","NElseIfMax")
	end_deep_max		 = config.getint("EndBlocksParams","DeepMax")
	end_case_values_min	 	 = config.getint("EndBlocksParams","CaseValuesMin")
	end_case_values_max	 	 = config.getint("EndBlocksParams","CaseValuesMax")
	
	########################
	## Mid blocks params  ##
	########################
	
	mid_prob_block         	 = config.getfloat("MidBlocksParams","ProbBlocks")
	mid_n_statements_min    	 = config.getint("MidBlocksParams","NStatementsMin")
	mid_n_statements_max         = config.getint("MidBlocksParams","NStatementsMax")
	mid_n_guard_statements_min   = config.getint("MidBlocksParams","NGuardStatementsMin")
	mid_n_guard_statements_max   = config.getint("MidBlocksParams","NGuardStatementsMax")
	mid_n_else_if_min		 = config.getint("MidBlocksParams","NElseIfMin")
	mid_n_else_if_max		 = config.getint("MidBlocksParams","NElseIfMax")
	mid_deep_max		 = config.getint("MidBlocksParams","DeepMax")
	mid_case_values_min	 	 = config.getint("MidBlocksParams","CaseValuesMin")
	mid_case_values_max	 	 = config.getint("MidBlocksParams","CaseValuesMax")
	
	########################
	##  Function params   ##
	########################
	
	func_n_functions_min         = config.getint("FunctionsParams","NFunctionsMin")
	func_n_functions_max         = config.getint("FunctionsParams","NFunctionsMax")
	func_arity_min        	 = config.getint("FunctionsParams","ArityMin")
	func_arity_max     	         = config.getint("FunctionsParams","ArityMax")
	
	func_n_statements_min    	 = config.getint("FunctionsParams","NStatementsMin")
	func_n_statements_max         = config.getint("FunctionsParams","NStatementsMax")
	func_n_guard_statements_min   = config.getint("FunctionsParams","NGuardStatementsMin")
	func_n_guard_statements_max   = config.getint("FunctionsParams","NGuardStatementsMax")
	func_n_else_if_min		 = config.getint("FunctionsParams","NElseIfMin")
	func_n_else_if_max		 = config.getint("FunctionsParams","NElseIfMax")
	func_deep_max		 = config.getint("FunctionsParams","DeepMax")
	func_case_values_min	 	 = config.getint("FunctionsParams","CaseValuesMin")
	func_case_values_max	 	 = config.getint("FunctionsParams","CaseValuesMax")
	
	
	#########################
	## Hide numbers params ##
	#########################
	
	hide_numbers_deep_max_min	 = config.getint("HideCodeParams","NumbersDeepMin")
	hide_numbers_deep_max_max 	 = config.getint("HideCodeParams","NumbersDeepMax")
	
	#########################
	## Hide strings params ##
	#########################
	
	hide_strings_split_chunk_splits = config.getint("HideCodeParams","StringsChunkSplits")
	
	#########################
	##     EOF params      ##
	#########################
	
	eof_fill_kb = config.getint("AddJunkParams","FillKBEOF")
    
    except:
	raw_input(Messages.config_file_error+" "+Messages.error_symbol)
	exit()	
	
    obfuscate(orig_name,dest_name,it,replace_includes,rm_comments_by_tag,rm_comments_by_semicolon, rm_comments_by_hash, \
	      rm_regions,add_regs,hide_func_names,hide_var_names,hide_func_params,add_hard_funcs,add_hard_funcs_calls,add_true_guard_statements,add_vars,add_comm, \
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

    raw_input(Messages.end_application)
