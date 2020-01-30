grammar Slp;

SEMI : ';';
EQ : '=';
LPAREN : '(';
RPAREN : ')';
COMMA : ',';

PLUS : '+';
MINUS : '-';
MUL : '*';
DIV : '/';

PRINT :'print';

fragment
    ALPHA : [a-z] | [A-Z] ;
fragment
    DIGIT : [0-9];

WS : [ \r\n\t] -> skip;

ID : ALPHA+ (ALPHA | DIGIT)*;
NUM : DIGIT+;

stm : ID EQ exp # assign_stm|
    stm SEMI stm # compound_stm|
    PRINT LPAREN exp_list RPAREN # print_stm;


exp : ID # id
    | NUM # num
    | exp op exp # bin_op
    | LPAREN  stm COMMA exp RPAREN # eseq;

exp_list : exp COMMA exp_list # exp_list_not_final
    | exp # exp_list_final;
op : PLUS | MINUS | MUL | DIV;