grammar Grammar;

// Reguły leksykalne
INT : 'int' ;
FLOAT : 'float' ;
MATRIX : 'matrix' ;
BOOL : 'bool' ;
TRUE : 'true' ;
FALSE : 'false' ;
VOID : 'void' ;
IF : 'if' ;
ELSE : 'else' ;
WHILE : 'while' ;
FOR : 'for' ;
READ : 'read' ;
PRINT : 'print' ;
RETURN : 'return' ;
INT_CONSTANT : [0-9]+ ;
FLOAT_CONSTANT : [0-9]+ '.' [0-9]+ ;
ID : [a-zA-Z_][a-zA-Z0-9_]* ;
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
XOR : '^' ;
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
          | block
          | function_call ;

variable_declaration : type ID (ASSIGN expression)? SEMICOLON ;

type : INT | FLOAT | MATRIX | BOOL;

assignment : ID ASSIGN expression SEMICOLON ;

print_statement : PRINT LPAREN (ID | INT_CONSTANT | FLOAT_CONSTANT) RPAREN SEMICOLON ;

read_statement : READ ID SEMICOLON ;

if_statement : IF LPAREN boolean_expression RPAREN statement (ELSE statement)?;

while_loop : WHILE LPAREN boolean_expression RPAREN statement ;

for_loop : FOR LPAREN variable_declaration? SEMICOLON additive_expression SEMICOLON assignment? RPAREN statement ;

function_declaration : type ID LPAREN parameters? RPAREN block ;

parameters : parameter (COMMA parameter)* ;

parameter : type ID ;

block : LBRACE statement* RBRACE ;

expression : boolean_expression | additive_expression ;

boolean_expression : NOT? (primary_boolean_expression ((AND | OR | XOR) boolean_expression)*) ;

primary_boolean_expression : bool | (additive_expression (LT | GT | LTE | GTE | EQ | NEQ) additive_expression) ;

additive_expression : multiplicative_expression ((ADD | SUB) multiplicative_expression)* ;

multiplicative_expression : unary_expression ((MUL | DIV | MOD) unary_expression)* ;

unary_expression : (ADD | SUB) unary_expression | primary_expression ;

primary_expression : INT_CONSTANT
                    | FLOAT_CONSTANT
                    | ID
                    | LPAREN expression RPAREN
                    | function_call ;

bool : TRUE | FALSE | ID;

function_call : ID LPAREN arguments? RPAREN ;

arguments : expression (COMMA expression)* ;

// Error handling for lexer
lexerError
    : . {emitErrorMessage("Lexer error at line " + getLine() + ", column " + getCharPositionInLine() + ": " + getText());} // Emit an error message with row and column information
    ;

parserError
    : . {emitErrorMessage("Parser error at line " + getLine() + ", column " + getCharPositionInLine() + ": " + getText());} // Emit an error message with row and column information
    ;