import ply.yacc as yacc
from lexer import tokens
import sys
from NodeType import *
start = 'principal'

list_args = []
list_local_declarations = []
list_statement_list = []
list_param_list = []
var_decl = None
#########################################
list_declaration_list = []
list_args = []
#########################################
str_trace = ''
prompt_pos = ''
token_error = ''
line_error = ''
mensaje = ''

calls_to_lista_declaraciones = 0

class Node:
     def __init__(self,type,children=None,leaf=None, lineno = None):
          self.type = type #Puede tener el token
          if children:
               self.children = children
          else:
               self.children = [ ]
          self.leaf = leaf #Tiene el valor del Lexema
          self.lineno = lineno
class MessageError:
     def __init__(self, message, line_error_content, promt_pos):
          self.message = message
          self.line_error_content = line_error_content
          self.prompt_pos
VERBOSE = 1
masInfo = True

def inOrder(arbol, linear_tree):
     if arbol != None:
          if arbol.children != []:
               inOrder(arbol.children[0], linear_tree)
          linear_tree.append(arbol.leaf)
          if arbol.children != []:
               inOrder(arbol.children[1], linear_tree)
     return linear_tree
                    
def p_principal(p):
	'principal : lista_declaraciones'
	new_declaration_list = []
	if masInfo:
		print("principal: ", p[1])
	list_declaration_list.reverse()
	nodeDeclarationList = Node(NodeType.LISTA_DECLARACIONES, list_declaration_list, None, 100)		
	p[0] = Node(NodeType.PRINCIPAL, [nodeDeclarationList], None, 100 )

def p_lista_declaraciones_1(p):
	'lista_declaraciones : lec lista_declaraciones'
	if masInfo:
		print("lista_declaraciones_1: ", p[1])
	global list_declaration_list
	if(p[1] != None):
		list_declaration_list.append(p[1])

	print("list declaration list 1: ", list_declaration_list)

def p_lista_declaraciones_2(p):
	'lista_declaraciones : esc lista_declaraciones'

	if masInfo:
		print("lista_declaraciones_2: ", p[1])
	global list_declaration_list

	list_declaration_list.append(p[1])

	print("list declaration list 2: ", list_declaration_list)
def p_lista_declaraciones_3(p):
	'lista_declaraciones : declaracion lista_declaraciones'
	global list_declaration_list
	list_declaration_list.append(p[1])
def p_lista_declaraciones_empty(p):
	'lista_declaraciones : empty'




def p_lec(p):
	'lec : SCANF LPAREN VALUE COMMA VARIABLE RPAREN SEMICOLON' 
	if masInfo:
		print("p_lec: ", p[1], p[2], p[3], p[4], p[5]) 
	p[0] = Node(NodeType.LEC, [
		Node(NodeType.SCANF, None, None, 100), 
		Node(NodeType.LPAREN, None, None, 100), 
		Node(NodeType.VALUE, None, None, 100), 
		Node(NodeType.COMMA, None, None, 100), 
		Node(NodeType.VARIABLE, None, None, 100), 
		Node(NodeType.RPAREN, None, None, 100), 
		Node(NodeType.SEMICOLON, None, None, 100), 
		], None, 100)
def p_esc(p):
	'esc : PRINTF LPAREN VALUE args RPAREN SEMICOLON'
	if masInfo:
		print('p_esc: ', p[1], p[2], p[3], p[4], p[5], p[6])

	if list_args != []:
		p[0] = Node(NodeType.ESC, [
			Node(NodeType.PRINTF, None, None, 100),
			Node(NodeType.LPAREN, None, None, 100),
			Node(NodeType.VALUE, None, None, 100),
			Node(NodeType.ARGS, list_args.copy(), None, 100),
			Node(NodeType.RPAREN, None, None, 100),
		])	
	else:
		p[0] = Node(NodeType.ESC, [
			Node(NodeType.PRINTF, None, None, 100),
			Node(NodeType.LPAREN, None, None, 100),
			Node(NodeType.VALUE, None, None, 100),
			Node(NodeType.RPAREN, None, None, 100),
		])	
	list_args.clear()
	return
def p_declaracion(p):
	'declaracion : tipo_dato VARIABLE args SEMICOLON'	
	if(masInfo):
		print('declaracion: ', p[1], p[2], list_args, p[4])
	if(list_args == []):
		p[0] = Node(NodeType.DECLARACION, [
			p[1], 
			Node(NodeType.VARIABLE, None, None, 100),
			Node(NodeType.SEMICOLON, None, None, 100)
			], None, 100);
	else:
		p[0] = Node(NodeType.DECLARACION, [
			p[1], 
			Node(NodeType.VARIABLE, None, None, 100),
			Node(NodeType.ARGS, list_args, None, 100),
			Node(NodeType.SEMICOLON, None, None, 100)
			], None, 100);
	


def p_args(p):
	'''args : COMMA VARIABLE args
	| empty'''
	global list_args
	if p[1] != None:
		list_args.append(Node(NodeType.VARIABLE, None, None, 100))
def p_tipo_dato(p):
	'''tipo_dato : NUMBER 
	| DOUBLE 
	| TEXT'''
	if(masInfo):
		print('tipo_dato: ', p[1])
	for dataType in NodeType:
		if(dataType.value == str(p[1])):
			print("Entre")
			p[0] = Node(dataType, None, p[1], 100)


def p_empty(p):
        'empty :'
        pass

def imprimeAST(arbol):
	global endentacion
	endentacion += 2
	if arbol != None:
		imprimeEspacios()
		print(arbol.leaf, arbol.type)

          #if arbol.type == "compound_stmt":
		for i in range(len(arbol.children)):
			for node in arbol.children[i]:
				imprimeAST(node)
         # elif arbol.children:
         #      for child in range(len(arbol.children)):
         #           if arbol.children[child] != []:
         #                imprimeAST(arbol.children[child])                        
		endentacion -= 2

def traverseTree(tree):
	global endentacion
	print(tree.type)
	if tree.children == None:
		return
	for i in range(len(tree.children)):
		endentacion += 2
		imprimeEspacios()
		traverseTree(tree.children[i])
		endentacion -=2


def imprimeEspacios():
    print(" "*endentacion, end="")

parser = None
endentacion = 0

programa = ''
posicion = 0
progLong = 0

def globales(prog, pos, progL):
     global programa, posicion, progLong
     programa = prog
     posicion = pos
     progLong = progL

def parser(imprime = True, sourceCode = ""):
     #global programa
     global parser
     #programa = programa.translate({ord('$'): None})
     print("SourceCode: ", sourceCode)
     parser = yacc.yacc()
     arbol = parser.parse(sourceCode)
     if imprime:
	     traverseTree(arbol)
     return arbol
     

if __name__ == '__main__':
	sourceCode = """ 
	scanf(1, x);
	printf(888888);
	double foo;
	"""
	parser(True, sourceCode = sourceCode)