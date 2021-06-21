import ply.lex as lex

tokens = (

	#Reserved words
	'ELSE',
	'IF',
	'NUMBER',
	'DOUBLE',
	'TEXT',
	'WHILE',
	'FOR',
	'SCANF',
	'PRINTF',
	
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'LESS',
	'LESSEQUAL',
	'GREATER',
	'GREATEREQUAL',
	'EQUAL',
	'DISTINCT',
	'ASSIGN',
	'AND',
	'OR',
	'SEMICOLON',
	'QUOTE',
	'COLON',
	'COMMA',
	'LPAREN',
	'RPAREN',
	'LBRACKET',
	'RBRACKET',
	'LBRACE',
	'RBRACE',

	# Variable tokens	
	'VALUE',
	'VARIABLE', 

)

t_PLUS 	 = r'\+'
t_MINUS	 = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_LESS 	 = r'<'
t_GREATER = r'>'
t_SEMICOLON = r';'
t_COLON = r':'
t_QUOTE = r'\''
t_COMMA	 = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'{'
t_RBRACE = r'}'

def t_ELSE(t):
	r'else'
	return t
def t_PRINTF(t):
	r'printf'
	return t
def t_SCANF(t):
	r'scanf'
	return t
def t_TEXT(t):
	r'text'
	return t
def t_NUMBER(t): 
	r'number'
	return t
def t_DOUBLE(t):
	r'double'
	return t
def t_IF(t):
	r'if'
	return t
def t_FOR(t):
	r'for'
	return t
	
def t_VALUE(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_VARIABLE(t):
	r'\w+(_\d\w)*'
	return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_EQUAL(t):
	r'=='
	return t

def t_DISTINCT(t):
	r'!='
	return t
def t_AND(t):
	r'&&'
	return t
def t_OR(t):
	r'\|\|'
	return t
def t_WHILE(t):
	r'while'
	return t
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
	r'/\*(.|\n)*?\*/'
	t.lexer.lineno += t.value.count('\n')

def t_error(t):
	print("Lexical error: ", str(t.value[0]))
	t.lexer.skip(1)

def test(data):
	global lexer
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print(tok)

lexer = lex.lex()