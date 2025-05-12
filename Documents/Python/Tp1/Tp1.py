
provincias = ['Ciudad Autónoma de Buenos Aires','Buenos Aires','Catamarca','Chaco','Chubut','Córdoba','Corrientes','Entre Ríos','Formosa','Jujuy','La Pampa','La Rioja','Mendoza','Misiones','Neuquén','Río Negro','Salta','San Juan','San Luis','Santa Cruz','Santa Fe','Santiago del Estero','Tierra del Fuego, Antártida e Islas del Atlántico Sur','Tucumán']
cantidad_habitantes = [3120612,17569053,429556,1142963,603120,3978984,1197553,1426426,606041,797955,366022,384607,2014533,1280960,726590,762067,1440672,818234,540905,333473,3556522,1054028,190641,1703186]
genero_femenino = [1666874, 9039102, 218528, 587636, 305364, 2043559, 615293, 728506, 309558, 410753, 185804, 196787, 1034005, 652184, 368638, 388236, 736965, 418550, 275955, 167622, 1833015, 535383, 95169, 876995]
genero_masculino = [1426112, 8410073, 208858, 549406, 294169, 1902135, 580013, 687698, 294653, 386067, 178750, 186290, 966819, 622907, 354755, 369654, 694898, 396048, 263807, 164037, 1702342, 514714, 94438, 823403]
genero_otro = [859, 2685, 31, 44, 79, 632, 270, 259, 67, 271, 6, 51, 478, 77, 277, 111, 219, 279, 110, 48, 644, 171, 178, 447]

print(type(provincias))
print(type(cantidad_habitantes))
print(type(genero_femenino))
print(type(genero_masculino))
print(type(genero_otro))

promedio_habitantes = sum(cantidad_habitantes) / len(cantidad_habitantes)
promedio_femenino = sum(genero_femenino) / len(genero_femenino)
promedio_masculino = sum(genero_masculino) / len(genero_masculino)
promedio_otro = sum(genero_otro) / len(genero_otro)

print("Promedio de habitantes:", promedio_habitantes)
print("Promedio de género femenino:", promedio_femenino)
print("Promedio de género masculino:", promedio_masculino)
print("Promedio de género otro:", promedio_otro)

promedio_habitantes = round(sum(cantidad_habitantes) / len(cantidad_habitantes), 2)
promedio_femenino = round(sum(genero_femenino) / len(genero_femenino), 2)
promedio_masculino = round(sum(genero_masculino) / len(genero_masculino), 2)
promedio_otro = round(sum(genero_otro) / len(genero_otro), 2)

print("Promedio de habitantes por provincia:", promedio_habitantes)
print("Promedio de género femenino por provincia:", promedio_femenino)
print("Promedio de género masculino por provincia:", promedio_masculino)
print("Promedio de género otro por provincia:", promedio_otro)

import statistics

mediana_habitantes = statistics.median(cantidad_habitantes)
print("Mediana de la población por provincia:", mediana_habitantes)

min_habitantes = min(cantidad_habitantes)
max_habitantes = max(cantidad_habitantes)

print("Cantidad mínima de habitantes:", min_habitantes)
print("Cantidad máxima de habitantes:", max_habitantes)

ratios_femenino_vs_otros = []

for fem, masc, otro in zip(genero_femenino, genero_masculino, genero_otro):
    total_otros = masc + otro
    ratio = round(fem / total_otros, 2)
    ratios_femenino_vs_otros.append(ratio)

print("Ratios femenino / (masculino + otro) por provincia:")
print(ratios_femenino_vs_otros)

hay_menos_femeninos = any(ratio < 1 for ratio in ratios_femenino_vs_otros)

if hay_menos_femeninos:
    print("Sí, hay al menos una provincia con menos habitantes femeninos que otros géneros.")
else:
    print("No, en ninguna provincia hay menos habitantes femeninos que otros géneros.")

mayor_ratio = max(ratios_femenino_vs_otros)
menor_ratio = min(ratios_femenino_vs_otros)

print("Mayor ratio femenino / (masculino + otro):", mayor_ratio)
print("Menor ratio femenino / (masculino + otro):", menor_ratio)

len_provincias = len(provincias)
len_habitantes = len(cantidad_habitantes)
len_femenino = len(genero_femenino)
len_masculino = len(genero_masculino)
len_otro = len(genero_otro)

print("Cantidad de provincias:", len_provincias)
print("Cantidad de valores en cantidad_habitantes:", len_habitantes)
print("Cantidad de valores en genero_femenino:", len_femenino)
print("Cantidad de valores en genero_masculino:", len_masculino)
print("Cantidad de valores en genero_otro:", len_otro)

if len_provincias == len_habitantes == len_femenino == len_masculino == len_otro:
    print("Todos los objetos tienen el mismo largo.")
else:
    print("Hay objetos con diferente cantidad de valores.")

def verificar_longitudes(*listas):
    longitudes = [len(lista) for lista in listas]
    iguales = all(l == longitudes[0] for l in longitudes)
    print("Longitudes de las listas:")
    for i, longitud in enumerate(longitudes, 1):
        print(f"Lista {i}: {longitud} elementos")
    print(f"\n¿Todas las listas tienen la misma longitud? {'Sí' if iguales else 'No'}")

# Llamada a la función con tus listas
verificar_longitudes(provincias, cantidad_habitantes, genero_femenino, genero_masculino, genero_otro)

for i in range(len(provincias)):
    print(f"Índice: {i} - Provincia: {provincias[i]}")

for i in range(len(provincias)):
    print(provincias[i])

for provincia in provincias:
    print(provincia.upper())

#print(provincias.upper())

for i in range(len(provincias)):
    print(f"{provincias[i].upper()}: {cantidad_habitantes[i]} habitantes")

def imprimo_habitantes(provincias, cantidad_habitantes):
    for i in range(len(provincias)):
        print(f"{provincias[i].upper()}: {cantidad_habitantes[i]} habitantes")

# Llamada a la función con tus listas
imprimo_habitantes(provincias, cantidad_habitantes)

def imprimo_variables(provincias, valores, texto):
    for i in range(len(provincias)):
        print(f"{texto} {provincias[i].upper()}: {valores[i]}")

# Imprimir la cantidad total de habitantes
imprimo_variables(provincias, cantidad_habitantes, "Cantidad de habitantes en")

# Imprimir la cantidad de mujeres
imprimo_variables(provincias, genero_femenino, "Cantidad de mujeres en")

# Imprimir la cantidad de varones
imprimo_variables(provincias, genero_masculino, "Cantidad de varones en")

# Imprimir la cantidad de personas con otro género
imprimo_variables(provincias, genero_otro, "Cantidad de personas con otro género en")
