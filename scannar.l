%{
#include <stdio.h>
#include <string.h>

// List of reserved keywords
char *keywords[] = {"int", "float", "if", "else", "while", "return"};

// Function to check if a word is a keyword
int is_keyword(char *word) {
    for (int i = 0; i < 6; i++) {
        if (strcmp(word, keywords[i]) == 0)
            return 1;
    }
    return 0;
}
%}

%%

[a-zA-Z_][a-zA-Z0-9_]* {
    if (is_keyword(yytext))
        printf("Keyword: %s\n", yytext);
    else
        printf("Identifier: %s\n", yytext);
}

[0-9]+                 { printf("Number: %s\n", yytext); }

[=+\-*/]               { printf("Operator: %s\n", yytext); }

[(){};,]               { printf("Special: %s\n", yytext); }

[ \t\n]+               { /* Skip whitespace */ }

.                      { printf("Unknown: %s\n", yytext); }

%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
