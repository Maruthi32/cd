%{
#include <stdio.h>
%}

%%

0[0-7]+              { printf("Octal Number: %s\n", yytext); }

0[xX][0-9a-fA-F]+     { printf("Hexadecimal Number: %s\n", yytext); }

[0-9]+               { printf("Decimal Number: %s\n", yytext); }

.|\n                 ;   // Ignore all other characters and newlines

%%

int main() {
    yylex();
    return 0;
}
