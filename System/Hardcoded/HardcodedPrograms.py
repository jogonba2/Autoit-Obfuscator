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

def base_91_encode(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($sStr)

    Local $aB91 = StringSplit('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~"', '', 2)
    Local $sEncoded, $b, $n, $v, $aStr = StringToASCIIArray($sStr)

    For $i = 0 To UBound($aStr) - 1
        $b = BitOR($b, BitShift($aStr[$i], ($n * - 1)))
        $n += 8
        If $n > 13 Then
            $v = BitAND($b, 8191)
            $s = 13 + ($v <= 88)
            If $v <= 88 Then $v = BitAND($b, 16383)
            $b = BitShift($b, $s)
            $n -= $s
            $sEncoded &= $aB91[Mod($v, 91)] & $aB91[$v / 91]
        EndIf
    Next

    If $n Then
        $sEncoded &= $aB91[Mod($b, 91)]
        If $n > 7 Or $b > 90 Then $sEncoded &= $aB91[$b / 91]
    EndIf

    Return $sEncoded

EndFunc \n\n"""

def base_91_decode(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($sStr)

    Local $sB91 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~"'
    Local $sDecoded, $n, $c, $b, $v = -1, $aStr = StringSplit($sStr, '', 2)

    For $i = 0 To UBound($aStr) - 1
        $c = StringInStr($sB91, $aStr[$i], 1) - 1
        If $v < 0 Then
            $v = $c
        Else
            $v += $c * 91
            $b = BitOR($b, BitShift($v, ($n * - 1)))
            $n += 13 + (BitAND($v, 8191) <= 88)
            Do
                $sDecoded &= Chr(BitAND($b, 255))
                $b = BitShift($b, 8)
                $n -= 8
            Until Not ($n > 7)
            $v = -1
        EndIf
    Next

    If ($v + 1) Then $sDecoded &= Chr(BitAND(BitOR($b, BitShift($v, ($n * - 1))), 255))

    Return $sDecoded

EndFunc \n\n"""

def base_128_encode(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($sStr)

    Local $aB128 = StringSplit('!#$%()*,.0123456789:;=@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎ', '', 2)
    Local $sEncoded, $ls, $r, $rs = 7, $aStr = StringToASCIIArray($sStr & ' ')

    For $i = 0 To UBound($aStr) - 1
        If $ls > 7 Then
            $i -= 1
            $ls = 0
            $rs = 7
        EndIf
        $nc = BitOR(BitAND(BitShift($aStr[$i], ($ls * -1)), 0x7f), $r)
        $r = BitAND(BitShift($aStr[$i], $rs), 0x7f)
        $rs -= 1
        $ls += 1
        $sEncoded &= $aB128[$nc]
    Next

    Return $sEncoded

EndFunc \n\n"""

def base_128_decode(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($sStr)

    Local $sB128 = '!#$%()*,.0123456789:;=@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎ'
    Local $sDecoded, $r, $rs = 8, $ls = 7, $aStr = StringSplit($sStr, '', 2)

    For $i = 0 To UBound($aStr) - 1
        $nc = StringInStr($sB128, $aStr[$i], 1) - 1
        If $rs > 7 Then
            $rs = 1
            $ls = 7
            $r = $nc
            ContinueLoop
        EndIf
        $r1 = $nc
        $nc = BitOR(BitAND(BitShift($nc, ($ls * -1)), 0xFF), $r)
        $r = BitShift($r1, $rs)
        $rs += 1
        $ls -= 1
        $sDecoded &= Chr($nc)
    Next

    Return $sDecoded

EndFunc \n\n"""

### String modifiers ###

def reverse_string(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.string_reverse_function = identifier
    return """Func """+identifier+"""($sText )
		Local $Result , $i , $sParams
		$sParams = StringLen($sText)
		For $i = 0 To $sParams
		   $Result = $Result & StringMid($sText, $sParams - $i, 1)
		Next
		Return $Result
	      EndFunc
	   """

def decode_xor(length_min=5,length_max=10): pass


def replace_string(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.string_replace_function = identifier
    return """Func """+identifier+"""($sText,$symbol)
		$Result = StringReplace($sText,$symbol,'')
		Return $Result
	      EndFunc
	   """
	   
def flip_two_string(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.string_flip_two_function = identifier
    return """Func """+identifier+"""($sText)
		Local $Result , $i , $sParams
		$Result  = ""
		$i       = 1
		While $i < StringLen($sText)
		    $Result &= StringMid($sText,$i+1,1) & StringMid($sText,$i,1)
		    $i = $i+2
		WEnd
		If Mod(StringLen($sText),2)<>0 Then
		    $Result &= StringRight($sText,1)
		EndIf
		Return $Result
	      EndFunc
	   """

HARDCODED_STRING_MODIFIERS = [flip_two_string,replace_string,reverse_string]

HARDCODED_PROGRAMS = [hex_to_string,string_repeat,string_to_hex,string_shuffle,
		      log_change_base,is_prime,string_dump,random_autoit,name_count]
