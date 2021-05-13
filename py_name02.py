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
data = ""
lexeme = [0 for i in range(100)]

def addChar():
    if lexLen <= 98:
        lexLen = lexLen + 1
        lexeme[lexLen] = nextChar
        lexeme[lexLen] = 0
    else:
        print(f'Error - lexeme is too long \n')

def getChar(nextChar):
    if nextChar != 'EOF':
        if nextChar.isalpha:
            charClass = LETTER
        elif nextChar.isdigit:
            charClass = DIGIT
        else :
            charClass = UNKNOWN
    else :
        charClass = 'EOF'

def getNonBlank():
    while nextChar.isspace:
        getChar()

def lookup(ch):
    addChar()
    nextToken = {'=': ASSIGN_OP, '+': ADD_OP, '-': SUB_OP, '*': MULT_OP, '/': DIV_OP, '(': LEFT_PAREN, ')': RIGHT_PAREN, '>': BIGGER_OP, '<': SMALLER_OP, ';': SEMI_SEP, '{': LEFT_CURLY_BRAC, '}': RIGHT_CURLY_BRAC}.get(ch, 'EOF')
    return nextToken

def isReserved():
    reserved_words = { "auto", "break", "case", "char", "const", "continue", "default", "do", "int", "long", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while", "double", "else", "enum", "extern", "float", "for", "goto", "if" }
    for re_word in reserved_words:
        if lexeme == re_word:
            return 1
    return 0

def lex():
    lexLen = 0
    getNonBlank()
    if charClass == LETTER:
        addChar()
        getChar()
        while charClass == LETTER or charClass == DIGIT:
            addChar()
            getChar()
        if isReserved() == 1:
            nextToken = RESERVED_WORD
        else :
            nextToken = IDENT
    elif charClass ==  DIGIT:
        addChar();
        getChar();
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = INT_LIT;
    elif charClass == UNKNOWN:
        lookup(nextChar);
        getChar();
    elif charClass == 'EOF':
        nextToken = 'EOF'
        lexeme[0] = 'E'
        lexeme[1] = 'O'
        lexeme[2] = 'F'
        lexeme[3] = 0
    print(f"Next token is: ", nextToken, "Next lexeme is ", lexeme, "\n")
    return nextToken

f = open("C:/Users/user/source/repos/PL_Assignment1/front02.py", "r")
data = f.read()
print(data)
tokens = data.split(" ")

for token in tokens:
    getChar(token)
    lex()
f.close()

#뭐가문제인지 알겠니
# 95번줄 data=f.read 에서 괄호를 안쳐서 그냥 함수 그 자체를 넣어버린거야  ?????
