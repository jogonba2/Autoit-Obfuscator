#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('../')
from Kernel import GenerateJunkCode
from Kernel import Utils
from Kernel import Config
from GenerateCode import Grammar as g
from random import sample,randint,choice

def pragma_directive(directive,parameter): return "#pragma compile("+directive+","+parameter+")\n"

def random_pragma_directives(n_directives_min=5,n_directives_max=19):
    res = ""
    n_directives_min,n_directives_max = max(n_directives_min,0),min(19,n_directives_max)
    n_directives                      = randint(min(n_directives_min,n_directives_max),max(n_directives_min,n_directives_max))
    pos_directives                    = sample(range(19),n_directives)
    for i in xrange(n_directives):
	if type(Config.PRAGMA_VALID_VALUES[pos_directives[i]])==list: res += pragma_directive(Config.PRAGMA_DIRECTIVES[pos_directives[i]],choice(Config.PRAGMA_VALID_VALUES[pos_directives[i]]))
	else: res += pragma_directive(Config.PRAGMA_DIRECTIVES[pos_directives[i]],Config.PRAGMA_VALID_VALUES[pos_directives[i]])
    return res

def on_autoit_start_register(func_name=Utils.generate_random_string(ext="")): return "#OnAutoItStartRegister "+'"'+func_name+'"\n'

def no_tray_icon(): return "#NoTrayIcon\n"

def include_once(): return "#include-once\n"

def include(script_au3=choice(Config.INCLUDES)): return "#include <"+script_au3+">\n"

def random_includes(n_includes_min=10,n_includes_max=20):
    res = ""
    n_includes_min,n_includes_max     = max(n_includes_min,0),min(len(Config.INCLUDES),n_includes_max)
    n_includes                        = randint(min(n_includes_min,n_includes_max),max(n_includes_min,n_includes_max))
    pos_includes                      = sample(range(len(Config.INCLUDES)),n_includes)
    for i in xrange(n_includes): res += include(Config.INCLUDES[pos_includes[i]])
    return res
    

if __name__ == "__main__":
    #print on_autoit_start_register("hola")
    print random_includes()
