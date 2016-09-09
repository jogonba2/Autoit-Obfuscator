#!/usr/bin/env python
# -*- coding: utf-8 -*-

general_process           = u" GENERAL "
obfuscate_process         = u" OFUSCAR "
add_junk_process          = u" AÑADIR BASURA "
end_process               = u" ESCRIBIENDO "
results_process           = u" RESULTADOS "
compilation_process       = u" COMPILACIÓN "

extracting_code    	  = u"Extrayendo código ..."
extracting_files          = u"Extrayendo archivos incluídos del proyecto ..."

removing_comments_by_tag  = u"Eliminando comentarios por #comments-start , #cs ..."
removing_comments_by_hash = u"Eliminando comentarios con hash # ..."
removing_comments_by_scol = u"Eliminando comentarios con punto y coma ..."
removing_regions          = u"Eliminando directivas region ..."

adding_variables   	  = u"Añadiendo variables ..."
adding_true_guard_sttmnts = u"Añadiendo sentencias true guard ..."
adding_hardcoded_functs   = u"Añadiendo funciones codificadas ..."
adding_comments   	  = u"Añadiendo comentarios ..."
adding_code_string_shffle = u"Añadiendo código para ocultar cadenas de texto con el método de barajado ..."
adding_code_string_rplce  = u"Añadiendo código para ocultar cadenas de texto con el método de reemplazo ..."
adding_code_flip_two      = u"Añadiendo código para ocultar cadenas de texto con el método flip two ..."
adding_code_reverse       = u"Añadiendo código para ocultar cadenas de texto con el método reverso ..." #
adding_code_rotate        = u"Añadiendo código para ocultar cadenas de texto con el método de rotación ..."
adding_mid_blocks      	  = u"Añadiendo bloques en posiciones aleatorias ..."
adding_functions          = u"Añadiendo funciones (puede tardar unos minutos) ..."
adding_regions            = u"Añadiendo regiones ..."
adding_function_calls     = u"Añadiendo bloques de función ..."
adding_init_blocks        = u"Añadiendo bloques al inicio ..."
adding_end_blocks         = u"Añadiendo bloques al final ..."
adding_directives         = u"Añadiendo directivas ..."
adding_tabs               = u"Añadiendo tabulaciones ..."
adding_to_eof             = u"Añadiendo al final del archivo ..."

replacing_includes        = u"Reemplazando archivos incluidos ..."

writing_code              = u"Escribiendo texto ofuscado ..."

happy_end                 = u" ofuscado correctamente en "
sad_end                   = u" no ofuscado; motivo: "
end_application           = u"Presione una tecla para cerrar el ofuscador ..."

hiding_function_params    = u"Ocultado nombres de los parámetros de las funciones ..."
hiding_variable_names     = u"Ocultado nombre de las variables ..."
hiding_function_names     = u"Ocultado nombre de las funciones ..."
hiding_numbers            = u"Ocultando números (puede tardar unos minutos) ..."
hiding_strings_replace    = u"Ocultando cadenas de texto con el método de reemplazo ..."
hiding_strings_flip_two   = u"Ocultando cadenas de texto con el método flip two ..."
hiding_strings_reverse    = u"Ocultando cadenas de texto con el método reverso ..."
hiding_strings_rotate     = u"Ocultando cadenas de texto con el método de rotación ..."
hiding_strings_hexify     = u"Ocultando cadenas de texto con el método hexify ..."
hiding_strings_shuffle    = u"Ocultando definición de cadenas de texto con el método shuffle ..."
hiding_strings_split      = u"Ocultando cadenas de texto con el método split ..."

compiling                 = u"Compilando ... "
stack_overflow_error      = u"stack overflow por recursión en generación de bloques, pruebe a reducir el valor deep y regenerar el código."
file_error                = u"error de archivo, probablemente has escrito mal el nombre del archivo."
unknown_error             = u"Ha ocurrido un error desconocido; detalles: "
config_file_error         = u"No se ha encontrado o no está bien formado el fichero config.ini. "
config_parse_error        = u"El fichero config.ini no está bien formado, comprueba las definiciones de variables. "

time_advertisement        = u"Es probable que el código tarde en ejeceutarse debido a los nuevos bloques añadidos."


advertisement_symbol      = u"[?]"
error_symbol              = u"[X]"
correct_symbol            = u"[C]"
