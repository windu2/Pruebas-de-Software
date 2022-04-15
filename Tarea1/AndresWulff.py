# Pruebas de Software: Tarea 1
# Andrés Wulff Reyes
# 201673006-0
# 15 de Abril 2022
from datetime import datetime

def AddString(input, file):
    container.append(input)
    Log(True,file,input)


def CompareStrings(index1, index2, file):
    Log(False, file, container[index1] == container[index2])
    if (container[index1] == container[index2]):
        return True
    else: return False


def Log(operation, file, input):
    if (operation):
        op = " Agregada secuencia"
    else: op = " Resultado comparacion: {result} \n".format(result=input)
    file.write(datetime.now().strftime("%H:%M:%S ") + op)


f = open('logs_andres.txt','a')
container = []
print("Introduzca primera secuencia:")
AddString(input(), f)

print("Introduzca segunda secuencia:")
AddString(input(), f)

compare = CompareStrings(0, 1, f)
print("Las secuencias {comparacion}son iguales".format(comparacion="" if compare else "no "))
f.write("\n")
f.close()