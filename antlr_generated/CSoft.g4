grammar CSoft;


COMMENT: '#' ~[\r\n]* -> skip;
COMMA : ',' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
PRINT : 'print' ;
READ : 'read' ;

prog: statement*  EOF 
    ;

statement: print_statement		#print
	| read_statement  		#read
    | expr              # exprression
 	| ident '=' expr		#assign
    | ID '[' INT ']' '=' expr #elementAssign
    | ident '=' arrayAssign  #arrAssign
    | repeatStm                #repeatStatement
    | ifStm                 #ifStatement
    | function              #funcDecl
    | structDecl            #structDeclaration
    | structFieldAssign     #structFieldAssignment
    | structAssign          #structAssignmet
    | classDecl             #classDeclaration
    | classAssign           #classAssignment
    ;

print_statement : PRINT LPAREN ID RPAREN ;

read_statement : READ LPAREN ID RPAREN ;

arrayAssign: '[' factor (',' factor)* ']';

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


ifStm: IF '(' expr ')' '{' blockIf '}' ;

blockIf: statement* ;

repeatStm: REPEAT repNum '{' blockRepeat '}'  
    ;

repNum: factor 
    ;

blockRepeat: statement* 
    ;

function: funType funName LPAREN parameters? RPAREN '{' blockFun '}' ;

blockFun: statement* ;

classDecl: CLASS className '{' blockClass '}'  ;

blockClass: structVarDecl* method*  ;

method: methodType methodName '{' blockMethod '}'  ;

blockMethod: statement*  ;

methodType: type ;

methodName: ID ;

className: ID ;

methodCall: ID '.' ident '()' ;

classAssign: ident '=' CLASS className ;

parameters : parameter (COMMA parameter)* ;

parameter : ident ;


structDecl: STRUCT structName '{' blockStruct '}' ;

blockStruct: structVarDecl* ;

structVarDecl: ident ;

structAssign: ident '=' STRUCT structName;

structFieldAssign: ID '.' ident '=' expr ;

structFieldAccess: ID '.' ident ;

arrayAccess: ID '[' INT ']';

funcCall: ID '()' 
    ;


ident: (type)? ID;

type: 'float32' | 'double' | 'int32' | 'int64' | 'bool' | 'string';

funType: type 
    ;

funName: ID 
    ;
structName: ID
    ;


IN: 'in';

REPEAT: 'rep';

IF: 'if';

FUNCTION: 'func'
    ;

CLASS: 'class'  ;

STRUCT: 'struct' ;
   

INT:   [0-9]+
    ;

FLOAT: [0-9]+ '.' [0-9]+
    ;

BOOL    : 'true' | 'false';

AddOper: '+' | '-'
    ;

MultOper: '*' | '/' | '%'
    ;

NegOper: '!'
    ;

RelOper: '==' | '!=' | '<' | '>' | '<=' | '>='
    ;

AndOper: '&&'
    ;

OrOper: '||'
    ;

XorOper: '^^'
    ;

ID : [a-zA-Z_][a-zA-Z0-9_]*
   ;

STRING :  '"' [a-zA-Z0-9 \t\n*+-]+ '"';

WS : [ \t\r\n]+ -> skip;