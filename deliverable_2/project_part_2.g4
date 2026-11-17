grammar project_part_2;

start : ( statement | INDENT statement | NEWLINE )* EOF ;

statement : assignment 
          | if_statement
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
         | array | STRING | FLOAT | INT | BOOL | ID 
         ;

if_statement : IF expression ':' suite 
              ( ELIF expression ':' suite )*
              ( ELSE ':' suite )?
              ;

suite : ( INDENT statement )+ NEWLINE* ;

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