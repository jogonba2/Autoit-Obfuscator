#!/usr/bin/env python
# -*- coding: utf-8 -*-

general_process           = u" GENERAL "
obfuscate_process         = u" OBFUSCATE "
add_junk_process          = u" ADD JUNK "
end_process               = u" WRITING "
results_process           = u" RESULTS "

extracting_code    	  = u"Extracting code ..."
extracting_files          = u"Extracting include files from project ..."

removing_comments_by_tag  = u"Removing comments by #comments-start , #cs ..."
removing_comments_by_hash = u"Removing comments with hash # ..."
removing_comments_by_scol = u"Removing comments with semicolon ..."
removing_regions          = u"Removing region directives ..."

adding_variables   	  = u"Adding variables ..."
adding_true_guard_sttmnts = u"Adding true guard statements ..."
adding_hardcoded_functs   = u"Adding hardcoded functions ..."
adding_comments   	  = u"Adding comments ..."
adding_code_string_shffle = u"Adding code for hide strings with shuffle method ..."
adding_code_string_rplce  = u"Adding code for hide strings with replace method ..."
adding_code_flip_two      = u"Adding code for hide strings with flip two method ..."
adding_code_reverse       = u"Adding code for hide strings with reverse method ..."
adding_code_rotate        = u"Adding code for hide strings with rotate method ..."
adding_mid_blocks      	  = u"Adding blocks at random positions ..."
adding_functions          = u"Adding functions (this may take a few minutes) ..."
adding_regions            = u"Adding regions ..."
adding_function_calls     = u"Adding function calls ..."
adding_init_blocks        = u"Adding blocks at init ..."
adding_end_blocks         = u"Adding blocks at end ..."
adding_directives         = u"Adding directives ..."
adding_tabs               = u"Adding tabs ..."
adding_to_eof             = u"Adding to eof ..."

replacing_includes        = u"Replacing includes ..."

writing_code              = u"Writing obfuscated text ..."

happy_end                 = u" obfuscated correctly in "
sad_end                   = u" not obfuscated, reason is: "
end_application           = u"Press a key to close the obfuscator ..."

hiding_function_params    = u"Hiding function params ..."
hiding_variable_names     = u"Hiding variable names ..."
hiding_function_names     = u"Hiding function names ..."
hiding_numbers            = u"Hiding numbers (this may take a few minutes) ..."
hiding_strings_replace    = u"Hiding strings with replace method ..."
hiding_strings_flip_two   = u"Hiding strings with two flip method ..."
hiding_strings_reverse    = u"Hiding strings with reverse method ..."
hiding_strings_rotate     = u"Hiding strings with rotate method ..."
hiding_strings_hexify     = u"Hiding strings with hexify method ..."
hiding_strings_shuffle    = u"Hiding string definitions with shuffle method ..."
hiding_strings_split      = u"Hiding strings with split method ..."


stack_overflow_error      = u"stack overflow because of recursion in block generating, try to reduce deep values and regenerate code."
file_error                = u"file error, probably you have specified an incorrect file name."
unknown_error             = u"An unknown error has occurred, details: "
config_file_error         = u"Config.ini has not been found or is not well formed. "
config_parse_error        = u"Config.ini is not well formed check variable definitions"

time_advertisement        = u"It's probably that obfuscated code takes to run due to added new blocks."


advertisement_symbol      = u"[?]"
error_symbol              = u"[X]"
correct_symbol            = u"[C]"
