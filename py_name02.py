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
COLON = 29
LEFT_CURLY_BRAC = 30
RIGHT_CURLY_BRAC = 31
EOF = -1

charClass = 0
nextChar = ''
lexLen = 0
nextToken = 0
data = ""
lexeme = []

lookup_dict = {
    '=': ASSIGN_OP,
    '+': ADD_OP,
    '-': SUB_OP,
    '*': MULT_OP,
    '/': DIV_OP,
    '(': LEFT_PAREN,
    ')': RIGHT_PAREN,
    '>': BIGGER_OP,
    '<': SMALLER_OP,
    '{': LEFT_CURLY_BRAC,
    '}': RIGHT_CURLY_BRAC,
    ':': COLON
}


def addChar():
    global lexLen, lexeme

    if lexLen <= 98:
        lexeme.append(nextChar)
        lexLen += 1
    else:
        print('Error - lexeme is too long: {}\n'.format(lexLen))
        input()


def getChar(option_remove):
    global nextChar, charClass

    if len(tokens) > 0:
        if option_remove==1:
            nextChar = tokens.pop()
        else:
            nextChar = tokens[-1]

        if nextChar.isalpha():
            charClass = LETTER

        elif nextChar.isdigit():
            charClass = DIGIT

        else:
            charClass = UNKNOWN

    else:
        # input()
        nextChar = 'EOF'
        charClass = EOF


def getNonBlank():
    while nextChar.isspace():
        getChar(1)


def lookup(ch):
    addChar()
    code = lookup_dict.get(ch, -1)
    return code


def isReserved():
    reserved_words = {"auto", "break", "case", "char", "const", "continue", "default", "do", "int", "long", "register", "return", "short", "signed", "sizeof",
                      "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while", "double", "else", "enum", "extern", "float", "for", "goto", "if"}
    for re_word in reserved_words:
        if lexeme == re_word:
            return 1
    return 0


def lex():
    global nextToken, nextChar, lexeme, lexLen

    del lexeme[0:]
    lexLen = 0

    getNonBlank()
    if charClass == -1:
        nextToken = -1
        lexeme.append('EOF')

    elif charClass == LETTER:
        addChar()
        getChar(0)
        a = 0
        while charClass == LETTER or charClass == DIGIT:
            a += 1
            getChar(1)
            addChar()
        if isReserved() == 1:
            nextToken = RESERVED_WORD
        else:
            nextToken = IDENT

    elif charClass == DIGIT:
        addChar()
        getChar(0)
        while charClass == DIGIT:
            getChar(1)
            addChar()
        nextToken = INT_LIT

    # elif charClass == UNKNOWN:
    else:
        nextToken = lookup(nextChar)
        # addChar()
        # getChar(1)

    print(f"Next token is: ", nextToken, "Next lexeme is ", ''.join(lexeme))

    return charClass


f = open("./front02.py", "r")
data = f.read()

data = data.replace('\n', ' ')
data = data.replace('\t', ' ')

tokens = list(data)
# print(tokens)
tokens.reverse()

while True:
    getChar(1)
    if lex() == -1:
        getChar(1)
        lex()
        break
f.close()
