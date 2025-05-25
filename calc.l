%{
#include "y.tab.h"
#include <stdlib.h>
%}

%%

[0-9]+           { yylval = atoi(yytext); return NUMBER; }
[\t ]+           { /* Ignore whitespaces */ }
[\n]             { return END; }
[+\-*/()]        { return *yytext; }
.                { printf("Invalid character: %s\n", yytext); return 0; }

%%

int yywrap() { return 1; }
