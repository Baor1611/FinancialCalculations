grammar Sample;

program: statement+;

statement: assignment | expression;

assignment: ID '=' expression ';';

expression: expression (ADD | SUB) term | term;

term: term (MUL | DIV) factor | factor;

factor: factor POW atom | atom;

atom: '(' expression ')' | ID | NUMBER;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
POW: '^';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;

WS: [ \t\r\n]+ -> skip;