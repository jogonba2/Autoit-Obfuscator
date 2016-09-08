#!/usr/bin/env python
# -*- coding: utf-8 -*-

general_process           = " GENERAL "
obfuscate_process         = " OFUSCAR "
add_junk_process          = " AÑADIR BASURA "
end_process               = " ESCRIBIENDO "
results_process           = " RESULTADOS "

extracting_code    	  = "Extrayendo código ..."
extracting_files          = "Extrayendo archivos incluídos del proyecto ..."

removing_comments_by_tag  = "Eliminando comentarios por #comments-start , #cs ..."
removing_comments_by_hash = "Eliminando comentarios con hash # ..."
removing_comments_by_scol = "Eliminando comentarios con punto y coma ..."
removing_regions          = "Eliminando directivas region ..."

adding_variables   	  = "Añadiendo variables ..."
adding_true_guard_sttmnts = "Añadiendo sentencias true guard ..."
adding_hardcoded_functs   = "Añadiendo funciones codificadas ..."
adding_comments   	  = "Añadiendo comentarios ..."
adding_code_string_rplce  = "Añadiendo código para ocultar cadenas de texto con el método de reemplazo ..."
adding_code_flip_two      = "Añadiendo código para ocultar cadenas de texto con el método flip two ..."
adding_code_reverse       = "Añadiendo código para ocultar cadenas de texto con el método inverso ..."
adding_code_rotate        = "Añadiendo código para ocultar cadenas de texto con el método de rotación ..."
adding_mid_blocks      	  = "Añadiendo bloques en posiciones aleatorias ..."
adding_functions          = "Añadiendo funciones (puede tardar unos minutos) ..."
adding_regions            = "Añadiendo regiones ..."
adding_function_calls     = "Añadiendo bloques de función ..."
adding_init_blocks        = "Añadiendo bloques al inicio ..."
adding_end_blocks         = "Añadiendo bloques al final ..."
adding_directives         = "Añadiendo directivas ..."
adding_tabs               = "Añadiendo tabulaciones ..."
adding_to_eof             = "Añadiendo al final del archivo ..."

replacing_includes        = "Reemplazando archivos incluidos ..."

writing_code              = "Escribiendo texto ofuscado ..."

happy_end                 = " ofuscado correctamente en "
sad_end                   = " no ofuscado; motivo: "



hiding_variable_names     = "Ocultado nombre de las variables ..."
hiding_function_names     = "Ocultado nombre de las funciones ..."
hiding_numbers            = "Ocultando números (puede tardar unos minutos) ..."
hiding_strings_replace    = "Ocultando cadenas de texto con el método de reemplazo ..."
hiding_strings_flip_two   = "Ocultando cadenas de texto con el método flip two ..."
hiding_strings_reverse    = "Ocultando cadenas de texto con el método inverso ..."
hiding_strings_rotate     = "Ocultando cadenas de texto con el método de rotación ..."
hiding_strings_hexify     = "Ocultando cadenas de texto con el método hexify ..."
hiding_strings_shuffle    = "Ocultando definición de cadenas de texto con el método shuffle ..."
hiding_strings_split      = "Ocultando cadenas de texto con el método split ..."


stack_overflow_error      = "stack overflow por recursión en generación de bloques, pruebe a reducir el valor deep y regenerar el código."
file_error                = "error de archivo, probablemente has escrito mal el nombre del archivo."
unknown_error             = "Ha ocurrido un error desconocido; detalles: "

time_advertisement        = "Es probable que el código tarde en ejeceutarse debido a los nuevos bloques añadidos."


advertisement_symbol      = "[?]"
error_symbol              = "[X]"
correct_symbol            = "[C]"
