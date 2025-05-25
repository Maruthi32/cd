%{
#include <stdio.h>
#include <stdlib.h>

int yylex(void);
void yyerror(const char *s);
%}

%token NUMBER END

%left '+' '-'
%left '*' '/'

%%

input:
      expr END { printf("Result: %d\n", $1); }
    ;

expr:
      expr '+' expr { $$ = $1 + $3; }
    | expr '-' expr { $$ = $1 - $3; }
    | expr '*' expr { $$ = $1 * $3; }
    | expr '/' expr { 
          if ($3 == 0) {
              yyerror("Division by zero");
              exit(1);
          }
          $$ = $1 / $3;
      }
    | '(' expr ')'   { $$ = $2; }
    | NUMBER         { $$ = $1; }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    printf("Enter an arithmetic expression:\n");
    while (1)
        yyparse();
    return 0;
}
