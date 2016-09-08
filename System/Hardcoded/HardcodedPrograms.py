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
EndFunc  \n\n"""

def string_to_hex(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($sString)
	Return Hex(StringToBinary($sString))
EndFunc   \n\n
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
    Globals.arity_new_functions.append(3)
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

def copyright_year(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(2)
    return """Func """+identifier+"""($iStartYear, $sDelimeter = "-") ; Return a String representation.
    If Number($iStartYear) <> @YEAR Then
        Return String($iStartYear & " " & $sDelimeter & " " & @YEAR)
    EndIf
    Return String($iStartYear)
EndFunc 
"""

def func_time(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(0)
    return """Func """+identifier+"""()
	Local $AMPM, $hour
    If @HOUR > 12 Then
        $hour = @HOUR - 12
        $AMPM = "PM"
    ElseIf @HOUR = 0 Then
        $hour = 12
        $AMPM = "AM"
    Else
        $hour = @HOUR
        $AMPM = "AM"
    EndIf
    Return $hour & ":" & @MIN & $AMPM
EndFunc
"""

def string_equal_split(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(2)
    return """Func """+identifier+"""($sString, $iNumChars)
	If IsString($sString) = 0 Or $sString == '' Then
		Return SetError(1, 0, 0)
	EndIf

	If IsInt($iNumChars) = 0 Or $iNumChars < 1 Then
		Return SetError(2, 0, 0)
	EndIf

	Local $aReturn = StringRegExp(_StringRepeat('0', 5) & $sString, '(?s).{1,' & $iNumChars & '}', 3)
	$aReturn[0] = UBound($aReturn, 1) - 1
	Return $aReturn
EndFunc 
"""

def string_is_num(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($sString)
    Return StringRegExp($sString, "^([0-9]*(\.[0-9]+){1}|[0-9]+(\.[0-9]*){0,1})$") = 1
EndFunc
"""

 ##
def autoit_win_get_text(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(0)
    return """Func """+identifier+"""()
    Local Const $hWnd = WinGetHandle(AutoItWinGetTitle()) ; Get the handle of the AutoIt Hidden Window by finding out the title of the AutoIt Hidden Window.
    Return ControlGetText($hWnd, '', ControlGetHandle($hWnd, '', 'Edit1'))
EndFunc  
"""

def is_beta(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(0)
    return """Func """+identifier+"""()
       Return Mod(StringSplit(@AutoItVersion, '.')[3], 2) == 1
EndFunc 
"""

def is_default(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($sDefault)
    Return StringRegExp($sDefault, "(?-i)\s|Default|-1|0")
EndFunc 
"""

def script_name(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(0)
    return """Func """+identifier+"""()
	Return StringLeft(@ScriptName, StringInStr(@ScriptName, '.', 2, -1) - 1)
EndFunc
"""

def string_get_chr_count(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(2)
    return """Func """+identifier+"""($sStr, $sChr, $iCase = 0)
	If $iCase <> 0 Then
		$iCase = 1
	EndIf
	StringReplace($sStr, $sChr, $sChr, 0, $iCase)
	Return @extended
EndFunc  
"""

###### NEW ######

def rgb_2_bgr(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($iColor)
    Return BitAND(BitShift(String(Binary($iColor)), 8), 0xFFFFFF)
EndFunc"""


def toggle_show_or_hide(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($iControlID)
    Local $aState[2] = [0,1]
    GUICtrlSetState($iControlID, $aState[Number(BitAND(GUICtrlGetState($iControlID), $aState[0]) = $aState[0])])
EndFunc  
"""

def are_icons_equal(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(2)
    return """Func """+identifier+"""($hicon1, $hicon2)
   Local $aRtn = DllCall("shlwapi.dll", "BOOL", 548, "handle", $hicon1, "handle", $hicon2)
   If @error Then
     Return SetError(@error)
   EndIf
   Return $aRtn[0]
EndFunc
"""

def calc_contrast_colour(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(2)
    return """Func """+identifier+"""($iColour, $iTolerance = 30)
    Switch $iTolerance
        Case 0 To 255
            $iTolerance = Int($iTolerance)
        Case Else
            $iTolerance = 30
    EndSwitch

    If (Abs(BitAND($iColour, 0xFF) - 0x80) <= $iTolerance And _
        Abs(BitAND(BitShift($iColour, 8), 0xFF) - 0x80) <= $iTolerance And _
        Abs(BitAND(BitShift($iColour, 16), 0xFF) - 0x80) <= $iTolerance) _
        Then Return BitAND((0x7F7F7F + $iColour), 0xFFFFFF)

    Return BitXOR($iColour, 0xFFFFFF)
EndFunc
"""

def image_size(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($ImgFullPath)
    Local $hWnd, $hGuiSwitch, $aCtrlSize, $aRetSize[2] = [0, 0]

    $hWnd = GUICreate($ImgFullPath, 0, 0, 0, 0, BitOR(0x80000000, 0x20000000), BitOR(0x00000080, 0x00000020))
    $hGuiSwitch = GUISwitch($hWnd)
    $aCtrlSize = ControlGetPos($hWnd, "", GUICtrlCreatePic($ImgFullPath, 0, 0, 0, 0))
    GUIDelete($hWnd)
    GUISwitch($hGuiSwitch)

    If IsArray($aCtrlSize) Then
        $aRetSize[0] = $aCtrlSize[2]; Width
        $aRetSize[1] = $aCtrlSize[3]; Height
        Return SetError(0, 0, $aRetSize)
    EndIf
    Return SetError(1, 0, $aRetSize)
EndFunc
"""

def switch_color(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($iColor)
    Local $iMask
    $iMask = BitXOR(BitAND($iColor, 0xFF) , ($iColor / 0x10000))
    Return BitXOR($iColor, ($iMask * 0x10001))
EndFunc 
"""

def bin_to_int(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($bin)
    Local $aArr = StringSplit($bin, "", 2)
    Local $dec = 0
    For $i = UBound($aArr) - 1 To 0 Step -1
        If $aArr[$i] = "1" Then
            $dec = BitXOR($dec, BitShift(1, -(UBound($aArr) - 1 - $i)))
        EndIf
    Next
    Return $dec
EndFunc
"""

def int_to_bin(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($iInt)
    Local $b = ""
    For $i = 1 To 32
        $b = BitAND($iInt, 1) & $b
        $iInt = BitShift($iInt, 1)
    Next
    Return $b
EndFunc
"""

def bytes_to_bits(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($bBinary)

    Local $byte, $bits="", $i, $j, $s
	#forceref $j
    For $i = 1 To BinaryLen($bBinary)
        $byte = BinaryMid($bBinary, $i, 1)
        For $j = 1 To 8
            $bits &= BitAND($byte, 1)
            $byte = BitShift($byte, 1)
        Next
    Next
    $s = StringSplit($bits, "")
    $bits = ""
    For $i = $s[0] To 1 Step -1
        $bits &= $s[$i]
    Next
    Return $bits
EndFunc
"""

def bits_to_bytes(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($sBits)
    Local $bBytes = Binary(''), $iLen = StringLen($sBits)
    Local $iCnt = 0, $iVal = 0
    For $i = 1 To $iLen
        $iCnt += 1
        $iVal = BitShift($iVal, -1)
        If "1" = StringMid($sBits, $i, 1) Then
            $iVal = BitOR($iVal, 1)
        EndIf
        If $iCnt = 8 Then
            $iCnt = 0
            $bBytes &= BinaryMid($iVal, 1, 1)
            $iVal = 0
        EndIf
    Next
    If $iCnt Then $bBytes &= BinaryMid(Binary(BitShift($iVal, -8+$iCnt)), 1, 1)
    Return $bBytes
EndFunc
"""

def generate(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(3)
    return """Func """+identifier+"""($iSize = 7, $iMin = 1, $iMax = 36)
	Local $aArray[$iSize], $sReturn = ''
	$aArray[0] = Random($iMin, $iMax, 1)
	For $i = 0 To $iSize - 1
		While 1
			$sReturn = Random($iMin, $iMax, 1)
			For $j = 0 To $i - 1
				If $aArray[$j] = $sReturn Then
					ContinueLoop 2
				EndIf
			Next
			ExitLoop
		WEnd
		$aArray[$i] = $sReturn
	Next
	Return $aArray
EndFunc
"""

def it_fibo(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(3)
    return """Func """+identifier+"""($n_0,$n_1,$N)
   Local $first = $n_0
   Local $second = $n_1
   Local $next = $first + $second
   Local $febo = 0
   For $i = 1 To $N-3
      $first = $second
      $second = $next
      $next = $first + $second
   Next
   if $n==0 Then
      $febo = 0
   ElseIf $n==1 Then
      $febo = $n_0
   ElseIf $n==2 Then
      $febo = $n_1
   Else
      $febo = $next
   EndIf
   Return $febo
EndFunc
"""

def miles_to_km(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($iLength)
    Return $iLength * 1.609
EndFunc 
"""

def km_to_miles(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($iLength)
    Return $iLength * 0.6214
EndFunc 
"""

def random_char_gen(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($iLength)
    Local $sReturn
    Local $aChars[62] = [ _
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', _
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', _
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    For $i = 0 To $iLength
        $sReturn &= $aChars[Random(0, 61)]
    Next
    Return $sReturn
EndFunc
"""

def check_idle(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(2)
    return """Func """+identifier+"""(ByRef $last_active, $start = 0)
    Local $struct = DllStructCreate("uint;dword");
    DllStructSetData($struct, 1, DllStructGetSize($struct));
    If $start Then
        DllCall("user32.dll", "int", "GetLastInputInfo", "ptr", DllStructGetPtr($struct))
        $last_active = DllStructGetData($struct, 2)
        Return $last_active
    Else
        DllCall("user32.dll", "int", "GetLastInputInfo", "ptr", DllStructGetPtr($struct))
        If $last_active <> DllStructGetData($struct, 2) Then
            Local $save = $last_active
            $last_active = DllStructGetData($struct, 2)
            Return $last_active - $save
        EndIf
    EndIf
EndFunc
"""

def m_sec(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(0)
    return """Func """+identifier+"""()
    Local $stSystemTime = DllStructCreate('ushort;ushort;ushort;ushort;ushort;ushort;ushort;ushort')
    DllCall('kernel32.dll', 'none', 'GetSystemTime', 'ptr', DllStructGetPtr($stSystemTime))
    Local $sMilliSeconds = StringFormat('%03d', DllStructGetData($stSystemTime, 8))
    $stSystemTime = 0
    Return $sMilliSeconds
EndFunc
"""

def get_todays_date(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($iReturnTime = 1)
    Local $aMDay[8] = [7, "Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"], _
            $aMonth[13] = [12, "Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"], $aTime[2] = ["", ' ' & @HOUR & ':' & @MIN & ':' & '00']
    Return $aMDay[@WDAY] & ', ' & @MDAY & ' ' & $aMonth[@MON] & ' ' & @YEAR & $aTime[$iReturnTime]
EndFunc
"""

def return_card(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($nJoker = 0)
    Local $nNumbers, $azSplits, $nRandom, $nReturn, $sFace, $sFaces, $nRandom2
    $nNumbers = "Two,Three,Four,Five,Six,Seven,Eight,Nine,Ten,Jack,King,Queen,Ace"
    If $nJoker Then
        $nNumbers &= ",Joker"
    EndIf
    $azSplits = StringSplit($nNumbers, ",")
    $sReturn = $azSplits[Random(1, $azSplits[0], 1)]
    $sFaces = StringSplit("Spades|Clubs|Hearts|Diamonds", "|")
    $nRandom2 = Random(1, $sFaces[0] - 1)
    $sFace = $sFaces[Round($nRandom2)]
    If $sReturn = "Joker" Then
        Return $sReturn
    Else
        Return $sReturn & " Of " &$sFace
    EndIf
EndFunc
 """

def get_time_online(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($iTimeZone)
	Local $aTimeZone[7] = ['utc', 'est', 'cst', 'mst', 'pst', 'akst', 'hast']

	Local $sRead = BinaryToString(InetRead('http://www.timeapi.org/' & $aTimeZone[$iTimeZone] & '/now?format=\Y/\m/\d%20\H:\M:\S'))

	If @error Then
		Return SetError(1, 0, @YEAR & '/' & @MON & '/' & @MDAY & ' ' & @HOUR & ':' & @MIN & ':' & @SEC)
	EndIf

	Return $sRead
EndFunc
 """
 
def string_to_ip_array(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($sString)
    Local $avArray = StringRegExp($sString, '([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', 3)
    Local $avRetArr[1], $iUbound

    For $i = 0 To UBound($avArray)-1
        If _IsValidIP($avArray[$i]) Then
            $iUbound = UBound($avRetArr)
            ReDim $avRetArr[$iUbound+1]
            $avRetArr[$iUbound] = $avArray[$i]
        EndIf
    Next
    If $iUbound = 0 Then Return SetError(1, 0, 0)

    $avRetArr[0] = $iUbound
    Return $avRetArr
EndFunc
 """

def string_to_struct(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($string)

	Local $iLen = StringLen($string)
	Local $Struct = DllStructCreate("char[" & String($iLen + 2) & "]")
	DllStructSetData($Struct, 1, $string)
	DllStructSetData($Struct, 1, 0, $iLen + 1)
	DllStructSetData($Struct, 1, 0, $iLen + 2)

	Return $Struct
EndFunc
 """

def is_file(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($sFilePath)
	Return Int(FileExists($sFilePath) And StringInStr(FileGetAttrib($sFilePath), 'D', Default, 1) = 0)
EndFunc
"""

def get_time_online(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($iTimeZone)
	Local $aTimeZone[7] = ['utc', 'est', 'cst', 'mst', 'pst', 'akst', 'hast']

	Local $sRead = BinaryToString(InetRead('http://www.timeapi.org/' & $aTimeZone[$iTimeZone] & '/now?format=\Y/\m/\d%20\H:\M:\S'))

	If @error Then
		Return SetError(1, 0, @YEAR & '/' & @MON & '/' & @MDAY & ' ' & @HOUR & ':' & @MIN & ':' & @SEC)
	EndIf

	Return $sRead
EndFunc
 """
 
def ini_read_file(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""$sFilePath)
    Local $aReturn[1][3] = [[0, 3]], $aSectionArray, $aSectionNameArray, $iCount = 0
    $aSectionNameArray = IniReadSectionNames($sFilePath)
    If @error Then
        Return SetError(1, 0, $aReturn)
    EndIf
    For $A = 1 To $aSectionNameArray[0]
        $aSectionArray = IniReadSection($sFilePath, $aSectionNameArray[$A])
        If @error Then
            ContinueLoop
        EndIf
        For $B = 1 To $aSectionArray[0][0]
            $aReturn[0][0] += 1
            $iCount += 1
            If $aReturn[0][0] <= $iCount + 1 Then
                ReDim $aReturn[$aReturn[0][0] * 2][$aReturn[0][1]]
            EndIf
            $aReturn[$iCount][0] = $aSectionArray[$B][0]
            $aReturn[$iCount][1] = $aSectionArray[$B][1]
            $aReturn[$iCount][2] = $aSectionNameArray[$A]
        Next
    Next
    ReDim $aReturn[$aReturn[0][0] + 1][$aReturn[0][1]] ; Remove empty entries.
    Return $aReturn
EndFunc
"""

def random_text(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($iLength = 10)
    Local $sData = '', $sRandom = ''
    For $i = 1 To $iLength
        $sRandom = Random(55, 116, 1)
        $sData &= Chr($sRandom + 6 * ($sRandom > 90) - 7 * ($sRandom < 65))
    Next
    Return $sData
EndFunc
"""

def is_maximized(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""($hWnd)
    Return BitAND(WinGetState($hWnd), 32) = 32
EndFunc
"""

def ternary(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(3)
    return """Func """+identifier+"""($iValue, $vTrue, $vFalse)
    Local $aArray[2] = [$vFalse, $vTrue]
    Return $aArray[Number(Number($iValue) > 0)]
EndFunc
"""

def get_last_error_message(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(0)
    return """Func """+identifier+"""()
    Local $ret, $s
    Local $p = DllStructCreate("char[4096]")
    Local Const $FORMAT_MESSAGE_FROM_SYSTEM = 0x00001000
    If @error Then Return ""
    $ret = DllCall("Kernel32.dll", "int", "GetLastError")
    $ret = DllCall("kernel32.dll", "int", "FormatMessage", _
            "int", $FORMAT_MESSAGE_FROM_SYSTEM, _
            "ptr", 0, _
            "int", $ret[0], _
            "int", 0, _
            "ptr", DllStructGetPtr($p), _
            "int", 4096, _
            "ptr", 0)
    $s = DllStructGetData($p, 1)
    Return $s
EndFunc
"""

def os_arch(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(0)
    return """Func """+identifier+"""()
    Return StringRegExpReplace(@OSArch, "(?i)x86|\D+", "") ; Thanks to wraithdu.
EndFunc
"""

def os_version_ex(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.defined_new_functions.append(identifier)
    Globals.arity_new_functions.append(1)
    return """Func """+identifier+"""()
    Return StringLeft(FileGetVersion(@SystemDir & "\WinVer.exe"), 3)
EndFunc
"""

### String modifiers ###

def shuffle_string(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.string_shuffle_function = identifier
    return """Func """+identifier+"""($string,$shifts_string)
    Local $s   = StringToASCIIArray($string) 
    Local $tpr = $s
    Local $i = StringSplit($shifts_string,Chr(44))
    For $p=0 To UBound($s)-1
	$s[$i[$p+1]] = $tpr[$p] 
    Next
    Return StringFromASCIIArray($s) 
EndFunc


"""

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
	   
def rotate_string(length_min=10,length_max=15):
    identifier = Utils.generate_identifier(length_min,length_max)
    Globals.string_rotate_function = identifier
    return """Func """+identifier+"""($sString,$sShift)
    Return StringMid($sString,StringLen($sString)-$sShift+1) & StringMid($sString,1,StringLen($sString)-$sShift)
EndFunc
"""

HARDCODED_STRING_MODIFIERS = [shuffle_string,rotate_string,flip_two_string,replace_string,reverse_string]

HARDCODED_PROGRAMS = [hex_to_string,string_repeat,string_to_hex,string_shuffle,
		      log_change_base,is_prime,string_dump,random_autoit,name_count,
		      base_91_encode, base_91_decode, base_128_encode, base_128_decode,
		      copyright_year, func_time, string_equal_split, string_is_num,
		      autoit_win_get_text, is_beta, is_default, script_name, 
		      string_get_chr_count,rgb_2_bgr,toggle_show_or_hide,are_icons_equal,calc_contrast_colour,
		      image_size,switch_color,bin_to_int,int_to_bin,bytes_to_bits,bits_to_bytes,generate,it_fibo,
		      miles_to_km,km_to_miles,random_char_gen,check_idle,m_sec,get_todays_date,return_card,
		      get_time_online,string_to_ip_array,string_to_struct,is_file,get_time_online,ini_read_file,
		      random_text,is_maximized,ternary,get_last_error_message,os_arch,os_version_ex]



