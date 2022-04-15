from datetime import datetime

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
f.write(current_time + " Secuencia 1 ingresada"+"\n")


secuen_2 = input("Ingrese la 2da secuencia de caracteres a comparar: ")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
f.write(current_time + " Secuencia 2 ingresada"+"\n")



now = datetime.now()
current_time = now.strftime("%H:%M:%S")
f.write(current_time + " Comparando"+"\n")

if(secuen_2 != secuen_1):
	print("Ambas secuencias no son iguales")
	f.write("Resultado: Ambas secuencias no son iguales")
else:
	print("Ambas secuencias son iguales")
	f.write("Resultado: Ambas secuencias son iguales")


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
f.write(current_time + " Fin de ejecucion" + "\n"+"\n")


#cierre de documento
f.close()

			





