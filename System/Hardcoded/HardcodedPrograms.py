#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('../')
from Kernel import Utils,ExtractKeywords,Config,Globals
from random import randint,choice,uniform
from string import lowercase,uppercase,letters
from re import findall


def hex_to_string(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($sHex)
	If Not (StringLeft($sHex, 2) == "0x") Then $sHex = "0x" & $sHex
	Return BinaryToString($sHex)
EndFunc \n\n"""

def string_repeat(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(2)
    return """Func """+identifier+"""($sString, $iRepeatCount)
	; Casting Int() takes care of String/Int, Numbers.
	$iRepeatCount = Int($iRepeatCount)
	; Zero is a valid repeat integer.
	If StringLen($sString) < 1 Or $iRepeatCount < 0 Then Return SetError(1, 0, "")
	Local $sResult = ""
	While $iRepeatCount > 1
		If BitAND($iRepeatCount, 1) Then $sResult &= $sString
		$sString &= $sString
		$iRepeatCount = BitShift($iRepeatCount, 1)
	WEnd
	Return $sString & $sResult
EndFunc  \n\n ;==>_StringRepeat """

def string_to_hex(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($sString)
	Return Hex(StringToBinary($sString))
EndFunc   ;==>_StringToHex \n\n
"""

def string_shuffle(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($sString)
    For $i = StringLen($sString) - 1 To 0 Step -1
        $sString = StringRegExpReplace($sString, "(?s)(.{" & Random(0, $i, 1) & "})(.)(.*)", "$1$3$2")
    Next
    Return $sString
EndFunc \n\n
"""

def log_change_base(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(2)
    return """Func """+identifier+"""($Number, $Base)
    return Log($Number) / Log($Base)
EndFunc \n\n """


def is_prime(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($iNum) ; Alexander Alvonellos
    If($iNum < 2) Then Return False
    If($iNum = 2) Then Return True
    If(BitAnd($iNum, 1) = 0) Then Return False
    For $i = 3 To Sqrt($iNum) Step 2
        If(Mod($iNum, $i) = 0) Then Return False
    Next
    Return True
EndFunc \n\n
"""

def string_dump(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(2)
    return """Func """+identifier+"""($sString, $iLength)

    Local $sStringAsc, $sStringDec, $sStringHex, $sChar, $iIndex, $iPos = 1
    For $iIndex = 1 To StringLen($sString)
        $sChar = StringMid($sString, $iIndex, 1)
        If Asc($sChar) >= 32 Then
            $sStringAsc = $sStringAsc & "  " & $sChar & " "
        Else
            $sStringAsc = $sStringAsc & "  . "
        EndIf
        $sStringHex = $sStringHex & " " & Hex(Asc(StringMid($sString, $iIndex, 1)), 2) & " "
        $sStringDec = $sStringDec & StringRight("00" & Asc(StringMid($sString, $iIndex, 1)), 3) & " "
    Next
    While $iPos < StringLen($sString)
        ConsoleWrite(StringStripWS(StringMid($sStringAsc, ($iPos * 4) - 3, $iLength * 4), 2) & @LF)
        ConsoleWrite(StringStripWS(StringMid($sStringHex, ($iPos * 4) - 3, $iLength * 4), 2) & @LF)
        ConsoleWrite(StringStripWS(StringMid($sStringDec, ($iPos * 4) - 3, $iLength * 4), 2) & @LF & @LF)
        $iPos += $iLength
    WEnd

EndFunc \n\n"""

def random_autoit(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(2)
    return """Func """+identifier+"""($nNum1 = 0, $nNum2 = 0, $iFlag = 0)
    If Not IsNumber($nNum1) Then Return SetError(1, 0, 0) ; Invalid 1st parameter
    Switch @NumParams
        Case 0
            Return Random()
        Case 1
            If $nNum1 < 0 Then Return -Random(-$nNum1)
            Return Random($nNum1)
        Case Else
            If Not IsNumber($nNum1) Or ($iFlag <> 0 And $iFlag <> 1) Then Return SetError(2, 0, 0) ; Invalid 2nd or 3rd parameter
            If $nNum1 = $nNum2 Then Return $nNum1
            If $nNum2 > $nNum1 Then Return Random($nNum1, $nNum2, $iFlag)
            Return Random($nNum2, $nNum1, $iFlag)
    EndSwitch
EndFunc \n\n"""

def name_count(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($sData)
    $sData = StringStripWS(StringLower($sData), 8)
    Local $aStringSplit = StringSplit($sData, ''), $iReturn = 0
    For $i = 1 To $aStringSplit[0]
        For $j = 97 To 122
            If $aStringSplit[$i] == Chr($j) Then
                $iReturn += ($j - 96)
                ExitLoop
            EndIf
        Next
    Next
    Return $iReturn
EndFunc \n\n"""

HARDCODED_PROGRAMS = [hex_to_string,string_repeat,string_to_hex,string_shuffle,
		      log_change_base,is_prime,string_dump,random_autoit,name_count]
