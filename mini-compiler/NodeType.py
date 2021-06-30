from enum import Enum

class NodeType(Enum):
	LEC = 'LEC'
	ESC = 'ESC'
	ARGS = 'ARGS'
	LISTA_DECLARACIONES = 'LISTA_DECLARACIONES'
	DECLARACION = 'DECLARACION'
	PRINCIPAL = 'PRINCIPAL'
	SCANF = 'SCANF' 
	PRINTF = 'PRINTF'
	LPAREN = 'LPAREN'
	RPAREN = 'RPAREN'
	VALUE = 'VALUE'
	SEMICOLON = 'SEMICOLON'
	VARIABLE = 'VARIABLE'
	COMMA = 'COMMA'

	# Tipo de Dato
	NUMBER_DATA_TYPE = 'number'
	DOUBLE_DATA_TYPE = 'double'
	TEXT_DATA_TYPE = 'text'

if __name__ == '__main__':
	print("Hola: ", NodeType)
	for type in NodeType.DATA_TYPE:
		#if type.value == 'LPAREN':
		print(type.name, type.value)

