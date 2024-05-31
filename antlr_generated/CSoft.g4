grammar CSoft;

COMMA : ',' ;
DOT : '.' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
LBRACKET : '[' ;
RBRACKET: ']' ;
PRINT : 'print' ;
READ : 'read' ;
IF: 'if';
STRUCT: 'struct' ;
CLASS: 'class' ;
type: 'double' | 'int' | 'long' | 'bool' | 'string' | 'void';
BOOL    : 'true' | 'false';
REPEAT: 'repeat';
WHILE: 'while' ;
ASSIGN: '=';

INT:   [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;

AddOper: '+' | '-';
MultOper: '*' | '/' | '%';
NegOper: '!';
RelOper: '==' | '!=' | '<' | '>' | '<=' | '>=';
AndOper: '&&';
OrOper: '||';
XorOper: '^';

COMMENT: '#' ~[\r\n]* -> skip;

ID : [a-zA-Z_][a-zA-Z0-9_]*;

STRING :  '"' [a-zA-Z0-9 \t\n*+-]+ '"';

WS : [ \t\r\n]+ -> skip;

prog: statement*  EOF 
    ;

statement: print_statement		    #print
	| read_statement  		        #read
    | expr                          #exprression
 	| assignment	                #assign
    | arrayElementAssign expr       #elementAssign
    | ident ASSIGN arrayAssign      #arrAssign
    | repeatStm                     #repeatStatement
    | ifStm                         #ifStatement
    | whileL                        #whileLoop
    | function                      #funcDecl
    | structDecl                    #structDeclaration
    | structFieldAssign             #structFieldAssignment
    | structAssign                  #structAssignmet
    | classDecl                     #classDeclaration
    | classAssign                   #classAssignment
    ;

ident: (type)? ID;


arrayElementAssign : ID LBRACKET INT RBRACKET ASSIGN;

assignment : ident ASSIGN expr;

print_statement : PRINT LPAREN ID RPAREN ;

read_statement : READ LPAREN ID RPAREN ;

arrayAssign: LBRACKET factor (COMMA factor)* RBRACKET;

expr: condXorStm OrOper condXorStm 
    | condXorStm
    ;

condXorStm: condStmAnd XorOper condStmAnd
    | condStmAnd
    ;

condStmAnd: condStmRel AndOper condStmRel
    | condStmRel
    ;

condStmRel: addExpr RelOper addExpr
    | addExpr
    ;

addExpr: multExpr AddOper multExpr
    | multExpr
    ;

multExpr: negFactor MultOper negFactor
    | negFactor
    ;

negFactor: NegOper factor 
    | factor
    ;


factor: INT
    | FLOAT
    | STRING
    | BOOL
    | ID
    | arrayAccess
    | funcCall
    | structFieldAccess
    | methodCall
    ;


ifStm: IF LPAREN expr RPAREN LBRACE blockIf RBRACE ;

blockIf: statement* ;

whileL: WHILE LPAREN expr RPAREN LBRACE blockWhile RBRACE ;

blockWhile: statement* ;

repeatStm: REPEAT LPAREN repNum RPAREN LBRACE blockRepeat RBRACE  
    ;

repNum: factor 
    ;

blockRepeat: statement* 
    ;

function: funType funName LPAREN (parameters)? RPAREN LBRACE blockFun RBRACE ;

blockFun: statement* ;

classDecl: CLASS className LBRACE blockClass RBRACE  ;

blockClass: structVarDecl* method*  ;

method: methodType methodName LBRACE blockMethod RBRACE  ;

blockMethod: statement*  ;

methodType: type ;

methodName: ID ;

className: ID ;

methodCall: ID DOT ident LPAREN (arguments)? RPAREN  ;

classAssign: ident ASSIGN CLASS className ;

parameters : parameter (COMMA parameter)* ;

parameter : ident ;


structDecl: STRUCT structName LBRACE blockStruct RBRACE ;

blockStruct: structVarDecl* ;

structVarDecl: ident ;

structAssign: ident ASSIGN STRUCT structName;

structFieldAssign: ID DOT ident ASSIGN expr ;

structFieldAccess: ID DOT ident ;

arrayAccess: ID LBRACKET INT RBRACKET;

funcCall: ID LPAREN (arguments)? RPAREN 
    ;

arguments : argument (COMMA argument)* ;

argument : ID;

funType: type 
    ;

funName: ID 
    ;
structName: ID
    ;
 
