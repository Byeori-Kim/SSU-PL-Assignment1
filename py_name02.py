LETTER = 0
DIGIT = 1
UNKNOWN = 99
INT_LIT = 10
IDENT = 11
RESERVED_WORD = 12
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
BIGGER_OP = 27
SMALLER_OP = 28
SEMI_SEP = 29
LEFT_CURLY_BRAC = 30
RIGHT_CURLY_BRAC = 31

charClass = 0
nextChar = 'a'
lexLen = 0
nextToken = 0
lexeme = [ ]

def addChar() :
    if (lexLen <= 98):
		lexeme[lexLen++] = nextChar
		lexeme[lexLen] = 0
	else:
		print(f'Error - lexeme is too long \n')

def lookup(ch) :
    addChar()
    nextToken = {'=' : ASSIGN_OP, '+' : ADD_OP, '-' : SUB_OP, '*' : MULT_OP, '/' : DIV_OP, '(' : LEFT_PAREN, ')' : RIGHT_PAREN, '>': BIGGER_OP, '<' : SMALLER_OP, ';' : SEMI_SEP, '{' : LEFT_CURLY_BRAC, '}' : RIGHT_CURLY_BRAC}.get(ch, EOF)
    return nextToken
