%{
#include <stdio.h>
#include <stdlib.h>
void yyerror(const char *s);
int yylex(void);
%}

/* Declare token types */
%token NUMBER END

/* Define operator precedence and associativity */
%left '+' '-'
%left '*' '/'

%%

input:
      expr END { printf("Valid arithmetic expression\n"); return 0; }
    ;

expr:
      expr '+' expr
    | expr '-' expr
    | expr '*' expr
    | expr '/' expr
    | '(' expr ')'
    | NUMBER
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    printf("Enter an arithmetic expression:\n");
    return yyparse();
}
