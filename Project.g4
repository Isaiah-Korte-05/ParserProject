grammar Project;

start : ( statement | NEWLINE )* EOF ;

statement : ID '=' expression ;

expression : STRING | INT | FLOAT | BOOL | ID ;

BOOL : 'True' | 'False' ;

ID : [a-zA-Z_] [a-zA-Z0-9_]* ;

STRING : '"' .*? '"' | '\'' .*? '\'' ;

FLOAT : '-'? [0-9]+ '.' [0-9]+ ;

INT : '-'? [0-9]+ ;

NEWLINE : [\r\n]+ ;

WS : [ \t]+ -> skip ;