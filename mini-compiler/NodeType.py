from enum import Enum

class NodeType(Enum):
	LEC = 'LEC'
	ESC = 'ESC'
	LISTA_DECLARACIONES = 'LISTA_DECLARACIONES'
	PRINCIPAL = 'PRINCIPAL'
	SCANF = 'SCANF' 
	LPAREN = 'LPAREN'
	RPAREN = 'RPAREN'
	VALUE = 'VALUE'
	SEMICOLON = 'SEMICOLON'

if __name__ == '__main__':
	print("Hola")
	for type in NodeType:
		if type.value == 'LPAREN':
			print(type.name, type.value)

