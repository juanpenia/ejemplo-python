# 10. Dada una lista con nombres de imágenes:
# 
# imagenes = ['im1','im2','im3']
# 
# Generar una estructura que asocie 3 coordenadas ingresadas por teclado(x1, y1),(x2, y2)y(x3, y3), 
# con cada elemento de la lista (en el mismo orden en que son ingresadas). 
# Además verifique, mientras se van ingresando las coordenadas, que no hayan repetidas para una misma imagen;
# en dicho caso deberá volver a ingresarla

def main():
    imagenes = ['im1', 'im2', 'im3']
    lista = []
    for x in range(3):
        lista.append([imagenes[x]]) 
        for i in range(3):
            aux = []
            while True:
                for j in range(2):
                
                    a = "Coordenada " + (("X(" + str(i + 1) + ")") if j == 0 else ("Y(" + str(i + 1) + ")")) + ": "
                    coord = int(input(a))
                    aux.append(coord)
            
                    t = tuple(aux)
                
                if(t in lista[x]):
                    print("Las coordenadas estan repetidas.")
                    aux = []
                else:
                    break

            lista[x].append(t)
           
        print(lista)
main()