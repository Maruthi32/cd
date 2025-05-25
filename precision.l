 
%{ 
#include <stdio.h> 
%} 
 
%% 
[0-9]+\.[0-9]+  { printf("Real Precision Number: %s\n", yytext); } 
(e.g., 12.34) 
[0-9]+          { printf("Integer Number: %s\n", yytext); }      
.|\n            { } // Ignore other characters 
%% 
 
int main() { 
    printf("Enter numbers: "); 
    yylex();  // Process input 
    return 0; 
} 
 
int yywrap() { 
    return 1; 
} 
