grammar Grammar;

// Reguły leksykalne
INT : 'int' ;
FLOAT : 'float' ;
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
ASSIGN : ASSIGN ;
WS : [ \t\r\n]+ -> skip;

// Reguły syntaktyczne
program : statement* ;

statement : variable_declaration
          | assignment
          | print_statement
          | read_statement
          | if_statement
          | while_loop
          | function_declaration
          | return_statement
          | block
          | function_call ;

variable_declaration : type ID (ASSIGN expression)? SEMICOLON ;

type : INT | FLOAT | BOOL;

assignment : ID ASSIGN expression SEMICOLON ;

print_statement : PRINT LPAREN (ID | INT_CONSTANT | FLOAT_CONSTANT) RPAREN SEMICOLON ;

read_statement : READ LPAREN ID RPAREN SEMICOLON ;

if_statement : IF LPAREN expression RPAREN if_block (ELSE block)?;

if_block: block;

while_loop : WHILE LPAREN expression RPAREN while_block ;

while_block: block;

function_declaration : type ID LPAREN parameters? RPAREN function_block ;

function_block : block;

parameters : parameter (COMMA parameter)* ;

parameter : type ID ;

block : LBRACE statement* RBRACE ;

return_statement : RETURN expression SEMICOLON ;

primary_expression : INT_CONSTANT
                    | FLOAT_CONSTANT
                    | ID
                    | LPAREN expression RPAREN
                    | function_call ;

unary_expression : primary_expression | (ADD | SUB | NOT ) primary_expression ;

multiplicative_expression : unary_expression | multiplicative_expression (MUL | DIV | MOD) unary_expression;

additive_expression : multiplicative_expression | additive_expression (ADD | SUB) multiplicative_expression;

relational_expression : additive_expression | relational_expression (LT | GT | LTE | GTE) additive_expression;

equality_expression : relational_expression | equality_expression (EQ | NEQ) relational_expression;

logical_and_expression : equality_expression | logical_and_expression AND equality_expression;

logical_or_expression : logical_and_expression | logical_or_expression OR logical_and_expression;

expression : logical_or_expression;

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