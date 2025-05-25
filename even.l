%{
#include <stdio.h>
#include <stdlib.h>  // For atoi()
%}

%%

[0-9]+    {
             int num = atoi(yytext);
             if (num % 2 == 0)
                 printf("%d is Even\n", num);
             else
                 printf("%d is Odd\n", num);
          }

.|\n      ;   // Ignore all other characters and newlines

%%

int main() {
    yylex();
    return 0;
}
