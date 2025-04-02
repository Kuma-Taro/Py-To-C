import enum
import sys


class Lexer:
    def __init__(self, input):
        self.source = input + '\n'  # Source code to lex
        self.curChar = ''  # Current character
        self.curPos = -1  # Current position
        self.nextChar()  # Initialize first character

    def nextChar(self):
        self.curPos += 1
        self.curChar = '\0' if self.curPos >= len(self.source) else self.source[self.curPos]

    def peek(self):
        return '\0' if self.curPos + 1 >= len(self.source) else self.source[self.curPos + 1]

    def abort(self, message):
        sys.exit("Lexing error. " + message)

    def skipWhitespace(self):
        while self.curChar in (' ', '\t', '\r'):
            self.nextChar()

    def skipComment(self):
        if self.curChar == '#':
            while self.curChar != '\n':
                self.nextChar()

    def getToken(self):
        self.skipWhitespace()
        self.skipComment()
        token = None

        # Multi-character operators
        if self.curChar == '+' and self.peek() == '+':
            self.nextChar()
            token = Token('++', TokenType.INC)
        elif self.curChar == '-' and self.peek() == '-':
            self.nextChar()
            token = Token('--', TokenType.DEC)
        elif self.curChar == '&' and self.peek() == '&':
            self.nextChar()
            token = Token('&&', TokenType.AND)
        elif self.curChar == '|' and self.peek() == '|':
            self.nextChar()
            token = Token('||', TokenType.OR)
        elif self.curChar == '=' and self.peek() == '=':
            self.nextChar()
            token = Token('==', TokenType.EQEQ)
        elif self.curChar == '!' and self.peek() == '=':
            self.nextChar()
            token = Token('!=', TokenType.NOTEQ)
        elif self.curChar == '<' and self.peek() == '=':
            self.nextChar()
            token = Token('<=', TokenType.LTEQ)
        elif self.curChar == '>' and self.peek() == '=':
            self.nextChar()
            token = Token('>=', TokenType.GTEQ)

        # Single-character operators
        elif self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)
        elif self.curChar == '=':
            token = Token(self.curChar, TokenType.EQ)
        elif self.curChar == '>':
            token = Token(self.curChar, TokenType.GT)
        elif self.curChar == '<':
            token = Token(self.curChar, TokenType.LT)
        elif self.curChar == '!':
            token = Token(self.curChar, TokenType.NOT)

        # String literals
        elif self.curChar == '\"':
            self.nextChar()
            startPos = self.curPos
            while self.curChar != '\"':
                if self.curChar in ('\r', '\n', '\t', '\\', '%'):
                    self.abort("Illegal character in string.")
                self.nextChar()
            token = Token(self.source[startPos:self.curPos], TokenType.STRING)

        # Numbers
        elif self.curChar.isdigit():
            startPos = self.curPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek() == '.':
                self.nextChar()
                if not self.peek().isdigit():
                    self.abort("Illegal character in number.")
                while self.peek().isdigit():
                    self.nextChar()
            token = Token(self.source[startPos:self.curPos + 1], TokenType.NUMBER)

        # Identifiers and keywords (now with underscore support)
        elif self.curChar.isalpha() or self.curChar == '_':
            startPos = self.curPos
            while self.peek().isalnum() or self.peek() == '_':
                self.nextChar()
            tokText = self.source[startPos:self.curPos + 1]
            keyword = Token.checkIfKeyword(tokText)
            token = Token(tokText, keyword if keyword else TokenType.IDENT)

        # Newlines
        elif self.curChar == '\n':
            token = Token(self.curChar, TokenType.NEWLINE)

        # EOF
        elif self.curChar == '\0':
            token = Token('', TokenType.EOF)

        else:
            self.abort("Unknown token: " + self.curChar)

        self.nextChar()
        return token


class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind

    @staticmethod
    def checkIfKeyword(tokenText):
        for kind in TokenType:
            if kind.name == tokenText and kind.value >= 100 and kind.value < 200:
                return kind
        return None


class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3

    # Keywords
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    ELSE = 112
    ELSEIF = 113
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    FOR = 114
    TO = 115
    STEP = 116
    NEXT = 117

    # Logical operators
    AND = 118
    OR = 119
    NOT = 120

    # Operators
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211
    INC = 212
    DEC = 213