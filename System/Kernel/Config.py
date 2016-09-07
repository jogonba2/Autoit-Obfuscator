#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('./System')
from string import ascii_letters,digits,punctuation,whitespace,ascii_uppercase,ascii_lowercase
from Kernel import Utils
from random import shuffle
import base64

####################### DIRECTIVES #######################
PRAGMA_DIRECTIVES = ["Out","ExecLevel","UPX","AutoItExecuteAllowed","Console","Compression",\
		     "Compatibility","x64","inputboxres","Comments","CompanyName","FileDescription",\
		     "FileVersion","InternalName","LegalCopyright","LegalTrademarks","OriginalFilename",\
		     "ProductName","ProductVersion"]
		     
PRAGMA_VALID_VALUES = [Utils.generate_random_string(ext="exe"),\
		       ["none","asInvoker","highestAvailable"],["true","false"],\
		       ["true","false"],["true","false"],['1','3','5','7','9'],["vista","win7","win8","win81","win10"],\
		       ["true","false"],["true","false"],Utils.generate_random_string(15,30,""),\
		       Utils.generate_random_string(10,15,""),Utils.generate_random_string(15,50,""),\
		       Utils.generate_random_string(5,10,""),Utils.generate_random_string(20,30,""),\
		       Utils.generate_random_string(50,75,""),Utils.generate_random_string(50,75,""),\
		       Utils.generate_random_string(15,30,""),Utils.generate_random_string(10,20,""),\
		       Utils.generate_random_string(10,20,"")]

##########################################################

####################### AUTOIT DEFINITIONS #######################

INCLUDES                   = ['AVIConstants.au3', 'Array.au3', 'BorderConstants.au3', 'ButtonConstants.au3', 'Clipboard.au3', 'Color.au3', 'ColorConstants.au3', 'ComboConstants.au3', 'Constants.au3', 'Crypt.au3', 'Date.au3', 'DateTimeConstants.au3', 'Debug.au3', 'DirConstants.au3', 'EditConstants.au3', 'EventLog.au3', 'Excel.au3', 'FTPEx.au3', 'File.au3', 'FileConstants.au3', 'FontConstants.au3', 'FrameConstants.au3', 'GDIPlus.au3', 'GDIPlusConstants.au3', 'GUIConstants.au3', 'GUIConstantsEx.au3', 'GuiAVI.au3', 'GuiButton.au3', 'GuiComboBox.au3', 'GuiComboBoxEx.au3', 'GuiDateTimePicker.au3', 'GuiEdit.au3', 'GuiHeader.au3', 'GuiIPAddress.au3', 'GuiImageList.au3', 'GuiListBox.au3', 'GuiListView.au3', 'GuiMenu.au3', 'GuiMonthCal.au3', 'GuiReBar.au3', 'GuiRichEdit.au3', 'GuiScrollBars.au3', 'GuiSlider.au3', 'GuiStatusBar.au3', 'GuiTab.au3', 'GuiToolTip.au3', 'GuiToolbar.au3', 'GuiTreeView.au3', 'HeaderConstants.au3', 'IE.au3', 'IPAddressConstants.au3', 'ImageListConstants.au3', 'Inet.au3', 'ListBoxConstants.au3', 'ListViewConstants.au3', 'Math.au3', 'Memory.au3', 'MemoryConstants.au3', 'MenuConstants.au3', 'Misc.au3', 'NamedPipes.au3', 'NetShare.au3', 'Process.au3', 'ProcessConstants.au3', 'ProgressConstants.au3', 'RebarConstants.au3', 'RichEditConstants.au3', 'SQLite.au3', 'SQLite.dll.au3', 'ScreenCapture.au3', 'ScrollBarConstants.au3', 'Security.au3', 'SecurityConstants.au3', 'SendMessage.au3', 'SliderConstants.au3', 'Sound.au3', 'StaticConstants.au3', 'StatusBarConstants.au3', 'String.au3', 'StructureConstants.au3', 'TabConstants.au3', 'Timers.au3', 'ToolTipConstants.au3', 'ToolbarConstants.au3', 'TreeViewConstants.au3', 'UDFGlobalID.au3', 'UpDownConstants.au3', 'Visa.au3', 'WinAPI.au3', 'WinAPIError.au3', 'WinNet.au3', 'WindowsConstants.au3', 'Word.au3']
shuffle(INCLUDES)
MACROS                     = ["@TAB","@AutoItPID","@AutoItX64","@Compiled","@DesktopHeight","@DesktopWidth","@DesktopRefresh","@error","@HOUR","@MDAY","@MIN","@MON","@MSEC","@NumParams","@ScriptLineNumber","@TrayIconFlashing","@TrayIconVisible","@WDAY","@YDAY","@YEAR"]
MACRO_EXECUTE              = [] # Poner macros que realicen alguna acción #
FUNCTIONS_ZERO_ARITY       = ["ClipGet","MemGetStats","TrayGetMsg"]
FUNCTIONS_ONE_ARITY        = ["WinGetTitle","WinGetText","Execute","ConsoleWrite","BitNOT","StringUpper","StringIsAlNum","StringIsAlpha","StringIsASCII","Hex","Abs","ACos","ASin","ATan","BinaryLen","Ceiling","Cos","Dec","Floor","IsArray","IsBinary","IsBool","IsDeclared","IsFloat","IsInt","IsKeyword","IsNumber","Round"]
FUNCTIONS_TWO_ARITY        = ["BitAND","BitOR","BitRotate","BitShift","BitXOR","PixelGetColor"]

##############################################################
############################################################################
COMMENT_TYPES  = ["; *","#cs\n*\n#ce","#comments-start\n*\n#comments-end"]
VARIABLE_TYPES = ["Local *","Global *","Dim *"]#+["*"]
############################################################################

###############################################################
COMMENT_VOCABULARY   = ascii_uppercase+ascii_lowercase+digits
VARIABLE_VOCABULARY  = ascii_uppercase+ascii_lowercase+digits
NON_SENSE_VOCABULARY = [0x20,0x09]
###############################################################

################## STRING MODIFIERS ##################
JUNK_SYMBOLS = ['ç']
##############################################

## Registrar en la TDS las variables, sus tipos y dimensiones ##
TDS_FUNCTIONS = {}
TDS_VARIABLES = {}


MATH_FUNCTIONS              = [Utils.sum,Utils.sub,Utils.dot]
INVERSE_MATH_FUNCTIONS      = [Utils.sub,Utils.sum,Utils.dot]
AUTOIT_FUNCTIONS  	    = ["+","-","*","/"]
AUTOIT_INVERSE_FUNCTIONS    = ["-","+","/","*"]
BRACKETS                    = [0,0,0,0]
ARITY                       = [2,2,2,2]
#################################################################
