from lexer import *
from emit import *
from parser import *
import sys


def main():
    print("SK.bd Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(source)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program()  # Start the parser.
    emitter.writeFile()  # Write the output to file.
    print("Compiling completed.")


main()
