#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('../')
from Kernel import Utils,Config,Globals,StringModifiers
from Kernel import ExtractKeywords as ex
from random import shuffle,randint

"""
Local $s = StringToASCIIArray("tTes") -> esto en realidad es Test
Local $tpr = $s
Local $i[14] = [3,0,1,2] -> Permutación de los valores
For $p=0 To 14-1
    $s[$i[$p] = $tpr[$i[$p]] -> Se regenera
Next
$s = StringFromASCIIArray($s) 
-> Falta generar codigo para cifrar -> C.decrypt(C.encrypt($s)) 
"""

def hide_strings_split(obj):
    for i in xrange(len(obj)):
	v = ex.extract_string(obj[i])
	aux = obj[i].strip()
	if len(aux)>0 and aux[0]!="#" and not "RegExp" in aux:
	    for j in xrange(len(v)):
		v[j]   = v[j][1:-1] # !Comillas! -> puede bugear esto, probar a dejarlas 
		if len(v[j])>2:
		    obj[i] = obj[i].replace('"'+v[j]+'"',StringModifiers.split_string(v[j]))
		    #obj[i] = obj[i].replace("'"+v[j]+"'",StringModifiers.split_string(v[j]))
		#print v[j]
		#print StringModifiers.split_string(v[j])
		#raw_input()
		#obj[i] = obj[i].replace('"'+v[j]+'"',StringModifiers.split_string(v[j]))
		#obj[i] = obj[i].replace("'"+v[j]+"'",Globals.string_flip_two_function+'("'+StringModifiers.flip_two_modifier(v[j])+'") ') #
    return obj
    
def hide_strings_flip_two(obj):
    for i in xrange(len(obj)):
	v = ex.extract_string(obj[i])
	aux = obj[i].strip()
	if len(aux)>0 and aux[0]!="#" and not "RegExp" in aux:
	    for j in xrange(len(v)):
		v[j] = v[j][1:-1]
		if len(v[j])>2:
		    obj[i] = obj[i].replace('"'+v[j]+'"',Globals.string_flip_two_function+'("'+StringModifiers.flip_two_modifier(v[j])+'") ')
		    #obj[i] = obj[i].replace("'"+v[j]+"'",Globals.string_flip_two_function+'("'+StringModifiers.flip_two_modifier(v[j])+'") ') #
    return obj

def hide_strings_replace(obj):
    for i in xrange(len(obj)):
	v = ex.extract_string(obj[i])
	if not "#include" in obj[i] and not "RegExp" in obj[i]:
	    for j in xrange(len(v)):
		v[j] = v[j][1:-1]
		if len(v[j].strip())>0 and len(obj[i])<Globals.max_size_len_autoit-(len(obj[i])+(1.0/2)*len(obj[i]))+4+len(Config.JUNK_SYMBOLS[0]):
		    aux  = Utils.add_random_char_between_string(v[j],Config.JUNK_SYMBOLS[0])
		    obj[i] = obj[i].replace('"'+v[j]+'"',Globals.string_replace_function+"('"+aux+"','"+Config.JUNK_SYMBOLS[0]+"')")
    return obj
	    
def hide_strings_definition_shuffle(obj):
    for i in xrange(len(obj)):
	v = ex.extract_string_definition(obj[i])
	if not v: continue
	else:     
	    v = list(v[0])
	    aux = v[0].strip().lower()
	    if not '(' in aux and aux.find('if')!=0 and aux.find('elseif')!=0 and aux.find('func')!=0:
		indexes,shuffled = range(len(v[1])),""
		shuffle(indexes)
		for index in indexes: shuffled += v[1][index]
		v[0] = v[0].strip()
		if " " in v[0]: var_name = v[0][v[0].rfind(" ")+1:]
		else: var_name = v[0]
		var_aux_name   = Utils.generate_identifier(50,150)
		var_ind_name   = Utils.generate_identifier(50,150)
		var_cnt_name   = Utils.generate_identifier(30,75)
		obj[i] = v[0]+" = StringToASCIIArray(\""+shuffled+"\")\n Local $"+var_aux_name+" = "+var_name+"\n Local $"+var_ind_name+"["+str(len(indexes))+"] = "+str(indexes)+"\n For $"+var_cnt_name+" = 0 To "+str(len(indexes))+"-1\n\t"+var_name+"[$"+var_ind_name+"[$"+var_cnt_name+"]] = $"+var_aux_name+"[$"+var_cnt_name+"]\nNext\n"+var_name+" = StringFromASCIIArray("+var_name+")\n"	    
    return obj

def hide_strings_reverse(obj):
    for i in xrange(len(obj)):
	v = ex.extract_string(obj[i])
	aux = obj[i].strip()
	if len(aux)>0 and aux[0]!="#" and not "RegExp" in aux:
	    for j in xrange(len(v)):
		v[j] = v[j][1:-1]
		if '"' not in v[j] and "'" not in v[j] and len(v[j])>0:
		    obj[i] = obj[i].replace('"'+v[j]+'"',Globals.string_reverse_function+'("'+v[j][::-1]+'") ')
		    obj[i] = obj[i].replace("'"+v[j]+"'",Globals.string_reverse_function+'("'+v[j][::-1]+'") ') #
    return obj
    
if __name__ == "__main__":
    obj = Utils.extract_code("test.au3")
    obj = hide_strings_definition(obj)
    Utils.write_code(Utils.get_string_from_obj(obj),"testmod.au3")
    #print generate_graph(obj)
