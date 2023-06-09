import matplotlib.pyplot as plt

def pedir_coordenadas():
    vectores = input("Ingrese vectores separados por espacio: ")
    vectores = vectores.split(" ")
    x = []
    y = []
    for elem in vectores:
        elem = elem.split(",")
        x.append(int(elem[0]))
        y.append(int(elem[1]))
    return x, y

def verificar_transformacion(coord_x, coord_y, T):
    suma_x = sum(coord_x)
    suma_y = sum(coord_y)
    
    for elem in coord_x:
        suma_x = suma_x + elem
        

    return 
    
def mostrar_grafico(coord_x, coord_y):
    x = [0]*len(coord_x)
    y = [0]*len(coord_y)
    l = min(-1, min(coord_x)-1)
    r = max(1, max(coord_x)+1)
    d = min(-1, min(coord_y)-1)
    u = max(1, max(coord_y)+1)

    plt.xlim([l, r])
    plt.ylim([d, u])
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.quiver(x, y, coord_x, coord_y,  angles='xy', scale_units='xy', scale=1)
    plt.show()

if __name__ == "__main__":
    coord_x, coord_y = pedir_coordenadas()
    transformacion = ["x","y",">","2x","2y"]
    verificar_transformacion(coord_x, coord_y, transformacion)
