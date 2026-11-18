grammar project_part_3;

start : ( INDENT? statement | NEWLINE )* EOF ;

statement : assignment 
          | if_statement
          | while_loop
          | for_loop
          ;

assignment : ID assignment_operator expression ;

assignment_operator : '=' | '+=' | '-=' | '*=' | '/=' ;

expression : or_expression ;

or_expression : and_expression ( OR and_expression )* ;

and_expression : not_expression ( AND not_expression )* ;

not_expression : NOT not_expression | comparison_expression ;

comparison_expression : arithmetic ( comparison_operator arithmetic )? ;

arithmetic : first ( ( '+' | '-' ) first )* ;

first : second ( ( '*' | '/' | '%' ) second )* ;

second : ( '+' | '-' ) second | data_type ;

comparison_operator : '<' | '<=' | '>' | '>=' | '==' | '!=' ;

data_type : '(' expression ')'
          | function_call
          | array | STRING | FLOAT | INT | BOOL | ID 
          ;

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
