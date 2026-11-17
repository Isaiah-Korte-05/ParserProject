grammar project_part_1;

start : ( statement | NEWLINE )* EOF ;

statement : assignment 
          | ifStatement
          ;

assignment : ID ( '=' | '+=' | '-=' | '*=' | '/=' ) expression ;

// this is to make sure no multiple tree can be made
expression : orExp;

orExp : andExp (OR andExp)*;

andExp : notExp (AND notExp)*;

notExp : NOT notExp
       | compExpression
       ;

compExpression : arithmetic (compOP arithmetic)? ;

arithmetic : first (('+' | '-') first)*;

first : second (('*' | '/' | '%') second)*;

second : ('+' | '-') second
       | dataType
       ;

compOP : '<' | '<=' | '>' | '>=' | '==' | '!=';

dataType : '(' expression ')'
         | array | STRING | FLOAT | INT | BOOL | ID 
         ;

ifStatement : IF expression ':' suite 
            (ELIF expression ':' suite)*
            (ELSE ':' suite)?
            ;

suite : NEWLINE INDENTATION 
        (NEWLINE | statement NEWLINE*)+
        DEDENTATION
        ;

// Key Words / Lexer Rule
IF : 'if';
ELIF : 'elif';
ELSE : 'else';

AND : 'and';
OR : 'or';
NOT : 'not';

INDENTATION : '<INDENT>';
DEDENTATION : '<DEDENT>';

array : '[' (expression ( ',' expression )* )? ']';

BOOL : 'True' | 'False' ;
ID : [a-zA-Z_] [a-zA-Z0-9_]* ;
STRING : '"' .*? '"' | '\'' .*? '\'' ;
FLOAT : [0-9]+ '.' [0-9]+ ;
INT : [0-9]+ ;
NEWLINE : '\r'? '\n' ;
WS : [ \t]+ -> skip ;
