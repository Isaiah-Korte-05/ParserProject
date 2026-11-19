grammar project_part_2;

start : ( statement | INDENT statement | NEWLINE )* EOF ;

statement : assignment 
          | if_statement
          ;

assignment : ID assignment_operator expression ;

assignment_operator 
    : '=' 
    | '+=' 
    | '-=' 
    | '*=' 
    | '/=' 
    ;

comparison_operator 
    : '<' 
    | '<=' 
    | '>' 
    | '>=' 
    | '==' 
    | '!=' 
    ;

data_type
    : array 
    | STRING 
    | FLOAT 
    | INT 
    | BOOL 
    | ID 
    ;

expression 
    : '(' expression ')'

    |  '-' expression
    | '+' expression

    | NOT expression
    | left=expression AND right=expression
    | left=expression OR right=expression
    | left=expression compOp=comparison_operator right=expression

    | left=expression mulOp=('*' | '/' | '%') right=expression
    | left=expression addOp=('+' | '-') right=expression

    | data_type
    ;

if_statement 
    : IF expression ':' block 
    ( ELIF expression ':' block )*
    ( ELSE ':' block )?
    ;

block : ( INDENT statement )+ NEWLINE* ;

IF : 'if';
ELIF : 'elif';
ELSE : 'else';

AND : 'and';
OR : 'or';
NOT : 'not';

array : '[' (expression ( ',' expression )* )? ']';

BOOL : 'True' | 'False' ;
ID : [a-zA-Z_] [a-zA-Z0-9_]* ;
STRING : '"' .*? '"' | '\'' .*? '\'' ;
FLOAT : '-'? [0-9]+ '.' [0-9]+ ;
INT : '-'? [0-9]+ ;

INDENT : NEWLINE [ \t]+ ;
NEWLINE : ( '\r'? '\n' )+ ;
WS : [ \t]+ -> skip ;