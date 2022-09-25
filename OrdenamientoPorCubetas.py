
def cubetas(datos):
    cubetas = []
    k = 0
    
    for i in range(len(datos)):
        cubetas.append([])

    for j in datos:
        index = (10 // j)
        cubetas[index].append(j)

    
    for i in range(len(datos)):
        cubetas[i] = sorted(cubetas[i])
   
    for i in range(len(datos)):
        for j in range(len(cubetas[i])):
            datos[k] = cubetas[i][j]
            k += 1

    return datos

datos = [70, 12, 11, 78, 90, 33, 4, 51, 57, 10, 41, 22, 19, 88, 97, 13, 31, 40]
print("La matriz ordenada en orden descendente es")
print(cubetas(datos))