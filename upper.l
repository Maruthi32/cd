%{ 
#include <stdio.h> 
%} 
 
%% 
[a-z]    { printf("%c", yytext[0] - 32); } 
[A-Z]    { printf("%c", yytext[0]); }       
\n       { printf("\n"); }                  
.        { printf("%c", yytext[0]); }     
%% 
 
int main() { 
    printf("Enter a string: "); 
    yylex();  // Process input 
    return 0; 
} 
 
int yywrap() { 
    return 1; 
}  
