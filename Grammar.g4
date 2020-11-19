// Grammar.g4
grammar Grammar;

WHITESPACE: [ \r\n\t]+ -> skip;

// Rules
start : select1 EOF
    | insert1 EOF;

insert1 : 'INSERT INTO'  table_name '(' columns_list ')' 'VALUES' '(' values_list ')';

columns_list : column ( ',' column)*;

values_list : value ( ',' value)*;

select1 : 'SELECT' set_list 'FROM' from_list 'WHERE' condition;

set_list : pair ( ',' pair )* ;

pair : function '(' attribute ')' ;

function : 'AVG' | 'MEDIAN' ;

from_list : relation;

condition : attribute '=' IDENTIFIER ;

column : IDENTIFIER;

value : IDENTIFIER;

table_name : IDENTIFIER;

attribute : IDENTIFIER ;

relation : IDENTIFIER ;

IDENTIFIER :  (NUM_LETTER|'_'|('\\"'))+;

//STRING_LITERAL :  (NUM_LETTER|'_'|('\\"'))*;

fragment
NUM_LETTER : ('a'..'z'|'A'..'Z'|'0'..'9');


