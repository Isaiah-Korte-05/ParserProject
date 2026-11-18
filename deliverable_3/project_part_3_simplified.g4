grammar project_part_3;

start : ( INDENT? statement | NEWLINE )* EOF ;

statement : assignment 
          | if_statement
          | while_loop
          | for_loop
          ;

assignment : ID assignment_operator expression ;

assignment_operator : '=' | '+=' | '-=' | '*=' | '/=' ;

expression : '(' expression ')' 
           | function_call
           | ( '*' | '/' | '%' | '+' | '-' ) expression
           | expression ( '*' | '/' | '%' | '+' | '-' ) expression
           | expression comparison_operator expression
           | NOT expression
           | expression AND expression
           | expression OR expression
           | array
           | STRING | FLOAT | INT | BOOL | ID
           ;

comparison_operator : '<' | '<=' | '>' | '>=' | '==' | '!=' ;

function_call : ID '(' ( expression ( ',' expression )* )? ')' ;

if_statement : IF expression ':' suite 
              ( INDENT? ELIF expression ':' suite )*
              ( INDENT? ELSE ':' suite )?
              ;

while_loop : WHILE expression ':' suite ;

for_loop : FOR ID IN expression ':' suite ;

suite : ( INDENT? statement )+ NEWLINE* ;

IF : 'if' ;
ELIF : 'elif' ;
ELSE : 'else' ;
WHILE : 'while' ;
FOR : 'for' ;
IN : 'in' ;

AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;

array : '[' (expression ( ',' expression )* )? ']' ;

BOOL : 'True' | 'False' ;
ID : [a-zA-Z_] [a-zA-Z0-9_]* ;
STRING : '"' .*? '"' | '\'' .*? '\'' ;
FLOAT : '-'? [0-9]+ '.' [0-9]+ ;
INT : '-'? [0-9]+ ;

SINGLE_LINE_COMMENT : '#' ~[\r\n]* -> skip ;
MULTI_LINE_COMMENT : ( '\'\'\'' .*? '\'\'\'' | '"""' .*? '"""' ) -> skip ;

INDENT : NEWLINE [ \t]+ ;
NEWLINE : ( '\r'? '\n' )+ ;
WS : [ \t]+ -> skip ;
