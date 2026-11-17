grammar project_part_1;

start : ( statement | NEWLINE )* EOF ;

statement : assigenemnt 
          | ifStatement
          ;

assignement : ID ( '=' | '+=' | '-=' | '*=' | '/=' ) expression ;

expression : array
           | expression ( '*' | '/' | '%' ) expression
           | expression ( '+' | '-' ) expression
           | STRING | FLOAT | INT | BOOL | ID
           ;

array : '[' (expression ( ',' expression )* )? ']';

BOOL : 'True' | 'False' ;

ID : [a-zA-Z_] [a-zA-Z0-9_]* ;

STRING : '"' .*? '"' | '\'' .*? '\'' ;

FLOAT : '-'? [0-9]+ '.' [0-9]+ ;

INT : '-'? [0-9]+ ;

NEWLINE : [\r\n]+ ;

WS : [ \t]+ -> skip ;

// Key Words
IF : 'if';
ELSE : 'else';
ELIF : 'elif';

comOp : '<'
    | '<='
    | '>'
    | '>='
    | '=='
    | '!=' 
    ;
    
// indentations
INDENTATION : '<INDENT>';
DEDENTATION : '<DEDENT>';
    
ifStatement : IF expression ':' suite 
            (ELIF expression ':' suite)*
            (ELSE ':' suite)
            ;

suite : NEWLINE INDENTATION NEWLINE
        (statement NEWLINE*)+
        DEDENTATION
        ;