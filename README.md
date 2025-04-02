Brainrot Compiler
The brainrot compiler compiles a custom file with a .skbd at the end. The language used in this compiler is
unique because it uses gen-z slang as a substitute for Python keywords and converts it into C language.

How to Run the Compiler
To run the compiler, type python3 skbd.py (filename).skdb in a terminal. Make sure that every file is in the same folder.
After entering the command, it should output:
"""
SK.bd Compiler
Compiling completed.
"""
If there is an error about python3 not being found, type python skdb.py (filename).skbd

Syntax Rules
As for the syntax rules, it follows the standard syntax of Python except for the keywords.
Here is the list of the keywords that was replaced with gen-z slang:
LIGMA      ->  LABEL
SKEDADDLE  ->  GOTO
TUAH       ->  PRINT
HAWK       ->  INPUT
LETEMCOOK  ->  LET
GOON       ->  IF
BUSS       ->  ENDIF
EDGE       ->  ELSE
EDGING     ->  ELSEIF
VIBING     ->  WHILE
RUNITBACK  ->  REPEAT
GGS        ->  ENDWHILE
SHIP       ->  AND
LOWKEY     ->  OR
AINT       ->  NOT
GRINDING   ->  FOR

Sample Usage
As for the sample usage, we provided two programs that highlights specific functionalities of the compiler:
1. test_code_1.skbd  -  Basic I/O operations, if-else statements, arithmetic operations, assignment
2. test_code_2.skbd  -  Goto, looping, logical operators
