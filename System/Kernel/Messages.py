#!/usr/bin/env python
# -*- coding: utf-8 -*-

general_process           = " GENERAL "
obfuscate_process         = " OBFUSCATE "
add_junk_process          = " ADD JUNK "
end_process               = " WRITING "
results_process           = " RESULTS "

extracting_code    	  = "Extracting code ..."
extracting_files          = "Extracting include files from project ..."

removing_comments_by_tag  = "Removing comments by #comments-start , #cs ..."
removing_comments_by_hash = "Removing comments with hash # ..."
removing_comments_by_scol = "Removing comments with semicolon ..."
removing_regions          = "Removing region directives ..."

adding_variables   	  = "Adding variables ..."
adding_true_guard_sttmnts = "Adding true guard statements ..."
adding_hardcoded_functs   = "Adding hardcoded functions ..."
adding_comments   	  = "Adding comments ..."
adding_code_string_rplce  = "Adding code for hide strings with replace method ..."
adding_code_flip_two      = "Adding code for hide strings with flip two method ..."
adding_code_reverse       = "Adding code for hide strings with reverse method ..."
adding_code_rotate        = "Adding code for hide strings with rotate method ..."
adding_mid_blocks      	  = "Adding blocks at random positions ..."
adding_functions          = "Adding functions (this may take a few minutes) ..."
adding_regions            = "Adding regions ..."
adding_function_calls     = "Adding function calls ..."
adding_init_blocks        = "Adding blocks at init ..."
adding_end_blocks         = "Adding blocks at end ..."
adding_directives         = "Adding directives ..."
adding_tabs               = "Adding tabs ..."
adding_to_eof             = "Adding to eof ..."

replacing_includes        = "Replacing includes ..."

writing_code              = "Writing obfuscated text ..."

happy_end                 = " obfuscated correctly in "
sad_end                   = " not obfuscated, reason is: "



hiding_variable_names     = "Hiding variable names ..."
hiding_function_names     = "Hiding function names ..."
hiding_numbers            = "Hiding numbers (this may take a few minutes) ..."
hiding_strings_replace    = "Hiding strings with replace method ..."
hiding_strings_flip_two   = "Hiding strings with two flip method ..."
hiding_strings_reverse    = "Hiding strings with reverse method ..."
hiding_strings_rotate     = "Hiding strings with rotate method ..."
hiding_strings_hexify     = "Hiding strings with hexify method ..."
hiding_strings_shuffle    = "Hiding string definitions with shuffle method ..."
hiding_strings_split      = "Hiding strings with split method ..."


stack_overflow_error      = "stack overflow because of recursion in block generating, try to reduce deep values and regenerate code."
file_error                = "file error, probably you have specified an incorrect file name."
unknown_error             = "An unknown error has occurred, details: "

time_advertisement        = "It's probably that obfuscated code takes to run due to added new blocks."


advertisement_symbol      = "[?]"
error_symbol              = "[X]"
correct_symbol            = "[C]"
