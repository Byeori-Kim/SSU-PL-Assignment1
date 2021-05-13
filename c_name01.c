
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <ctype.h>
#include <string.h>
	int charClass;
	char lexeme[100];
	char nextChar;
	int lexLen;
	int token;
	int nextToken;
	FILE* in_fp, * fopen();
	void addChar();
	void getChar();
	void getNonBlank();
	int lex();
	int isReserved();
#define LETTER 0
#define DIGIT 1
#define UNKNOWN 99
#define INT_LIT 10
#define IDENT 11
#define RESERVED_WORD 12
#define ASSIGN_OP 20
#define ADD_OP 21
#define SUB_OP 22
#define MULT_OP 23
#define DIV_OP 24
#define LEFT_PAREN 25
#define RIGHT_PAREN 26
#define BIGGER_OP 27
#define SMALLER_OP 28
#define SEMI_SEP 29
#define LEFT_CURLY_BRAC 30
#define RIGHT_CURLY_BRAC 31
	int main() {
		if ((in_fp = fopen("front01.c", "r")) == NULL) {
			printf("ERROR - cannot open front01.c \n");
		}
		else {
			getChar(); do {
				lex();
			} while (nextToken != EOF);
		}
		return 0;
	}
	int lookup(char ch) {
		switch (ch) {
		case '=':
			addChar();
			nextToken = ASSIGN_OP;
			break;
		case '+':
			addChar();
			nextToken = ADD_OP;
			break;
		case '-':
			addChar();
			nextToken = SUB_OP;
			break;
		case '*':
			addChar();
			nextToken = MULT_OP;
			break;
		case '/':
			addChar();
			nextToken = DIV_OP;
			break;
		case '(':
			addChar();
			nextToken = LEFT_PAREN;
			break;
		case ')':
			addChar();
			nextToken = RIGHT_PAREN;
			break;
		case '>':
			addChar();
			nextToken = BIGGER_OP;
			break;
		case '<':
			addChar();
			nextToken = SMALLER_OP;
			break;
		case ';':addChar();
			nextToken = SEMI_SEP;
			break;
		case '{':
			addChar();
			nextToken = LEFT_CURLY_BRAC;
			break;
		case '}':
			addChar();
			nextToken = RIGHT_CURLY_BRAC;
			break;
		default:
			addChar();
			nextToken = EOF;
			break;
		}
		return nextToken;
	}
	void addChar() {
		if (lexLen <= 98) {
			lexeme[lexLen++] = nextChar;
			lexeme[lexLen] = 0;
		}
		else {
			printf("Error - lexeme is too long \n");
		}
	}
	void getChar() {
		if ((nextChar = getc(in_fp)) != EOF) {
			if (isalpha(nextChar)) {
				charClass = LETTER;
			}
			else if (isdigit(nextChar)) {
				charClass = DIGIT;
			}
			else {
				charClass = UNKNOWN;
			}
		}
		else {
			charClass = EOF;
		}
	}
	void getNonBlank() {
		while (isspace(nextChar)) {
			getChar();
		}
	}
	int isReserved() {
		char reserved_words[32][10] = { "auto", "break", "case", "char", "const", "continue", "default", "do", "int", "long", "register",
		"return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile",
		"while", "double", "else", "enum", "extern", "float", "for", "goto", "if" };
		int i;
		for (i = 0; i < 32; i++) {
			if (strcmp(lexeme, reserved_words[i]) == 0) {
				return 1;
			}
		}
		return 0;
	}
	int lex() {
		lexLen = 0;
		getNonBlank();
		switch (charClass) {
		case LETTER:
			addChar();
			getChar();
			while (charClass == LETTER || charClass == DIGIT) {
				addChar();
				getChar();
			}
			if (isReserved() == 1) {
				nextToken = RESERVED_WORD;
			}
			else {
				nextToken = IDENT;
			}
			break;
		case DIGIT:
			addChar(); getChar();
			while (charClass == DIGIT) {
				addChar();
				getChar();
			}
			nextToken = INT_LIT;
			break;
		case UNKNOWN:
			lookup(nextChar);
			getChar();
			break;
		case EOF:
			nextToken = EOF;
			lexeme[0] = 'E';
			lexeme[1] = 'O';
			lexeme[2] = 'F';
			lexeme[3] = 0;
			break;
		}
		printf("Next token is: %d Next lexeme is %s\n", nextToken, lexeme);
		return nextToken;
	}