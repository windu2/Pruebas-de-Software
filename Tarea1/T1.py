from datetime import datetime

#clase Pila
class Pila:
	def __init__(self,secuen):
		self.pila = secuen.split()

	def size(self):
		return len(self.pila)

	def pop(self):
		last = self.pila[-1]
		del self.pila[-1]
		return last

	def empty(self):
		if len(self.pila) == 0:
			return True
		return False

#Funcion que compara 2 pilas
def compare(pila1, pila2):

	if pila1.size() != pila1.size():
		return print("Ambas secuencias no son iguales")
	
	#las comparo si son del mismo largo
	while not pila1.empty():
		if pila2.pop() != pila1.pop():
			return print("Ambas secuencias no son iguales")

	return print("Ambas secuencias son iguales")

###########################################################################

#############PROGRAMA########################
#Se tomara como caracter todo lo que pueda escribirse con el teclado

print("Comparador de caracteres")
print("")

#Archivo de logs
f = open('logs.txt','a')


#inputs
secuen_1 = input("Ingrese la 1era secuencia de caracteres a comparar: ")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#print(current_time," secuencia 1 ingresada")
f.write(current_time + " secuencia 1 ingresada"+"\n")


secuen_2 = input("Ingrese la 2da secuencia de caracteres a comparar: ")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
f.write(current_time + " secuencia 2 ingresada"+"\n")


#las guardo en una pila

pila1 = Pila(secuen_1)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
f.write(current_time + " secuencia 1 guardada en pila"+"\n")

pila2 = Pila(secuen_2)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
f.write(current_time + " secuencia 2 guardada en pila"+"\n")


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
f.write(current_time + " comparando"+"\n")

compare(pila1, pila2)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
f.write(current_time + " fin de ejecucion" + "\n"+"\n")


#cierre de documento
f.close()

			





