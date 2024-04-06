grammar Grammar;

// Reguły leksykalne
INT : 'int' ;
FLOAT : 'float' ;
MATRIX : 'matrix' ;
VOID : 'void' ;
IF : 'if' ;
ELSE : 'else' ;
WHILE : 'while' ;
FOR : 'for' ;
READ : 'read' ;
PRINT : 'print' ;
RETURN : 'return' ;
ID : [a-zA-Z_][a-zA-Z0-9_]* ;
INT_CONSTANT : [0-9]+ ;
FLOAT_CONSTANT : [0-9]+ '.' [0-9]+ ;
MATRIX_CONSTANT : '[' [ \t\r\n]* ( INT_CONSTANT (',' INT_CONSTANT)* )? [ \t\r\n]* ']' ;
ADD : '+' ;
SUB : '-' ;
MUL : '*' ;
DIV : '/' ;
MOD : '%' ;
LT : '<' ;
GT : '>' ;
LTE : '<=' ;
GTE : '>=' ;
EQ : '==' ;
NEQ : '!=' ;
AND : '&&' ;
OR : '||' ;
NOT : '!' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
SEMICOLON : ';' ;
COMMA : ',' ;
ASSIGN : '=' ;
WS : [ \t\r\n]+ -> skip;

// Reguły syntaktyczne
program : statement* ;

statement : variable_declaration
          | assignment
          | print_statement
          | read_statement
          | if_statement
          | while_loop
          | for_loop
          | function_declaration
          | RETURN expression SEMICOLON
          | block ;

variable_declaration : type ID (ASSIGN expression)? SEMICOLON ;

type : INT | FLOAT | MATRIX ;

assignment : ID ASSIGN expression SEMICOLON ;

print_statement : PRINT expression SEMICOLON ;

read_statement : READ ID SEMICOLON ;

if_statement : IF LPAREN expression RPAREN statement (ELSE statement)?;

while_loop : WHILE LPAREN expression RPAREN statement ;

for_loop : FOR LPAREN variable_declaration? SEMICOLON expression SEMICOLON assignment? RPAREN statement ;

function_declaration : type ID LPAREN parameters? RPAREN block ;

parameters : parameter (COMMA parameter)* ;

parameter : type ID ;

block : LBRACE statement* RBRACE ;

expression : additive_expression ;

additive_expression : multiplicative_expression ((ADD | SUB) multiplicative_expression)* ;

multiplicative_expression : unary_expression ((MUL | DIV | MOD) unary_expression)* ;

unary_expression : (ADD | SUB) unary_expression | primary_expression ;

primary_expression : INT_CONSTANT
                    | FLOAT_CONSTANT
                    | MATRIX_CONSTANT
                    | ID
                    | LPAREN expression RPAREN
                    | function_call ;

function_call : ID LPAREN arguments? RPAREN ;

arguments : expression (COMMA expression)* ;
