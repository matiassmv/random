import matplotlib.pyplot as plt

def pedir_coordenadas():
    vectores = input("Ingrese 2 vectores separados por espacio: ")
    vectores = vectores.replace("(", "")
    vectores = vectores.replace(")", "")
    vectores = vectores.split(" ")
    u_aux = [vectores[0]]
    v_aux = [vectores[1]]
    u_aux = u_aux[0].split(",")
    v_aux = v_aux[0].split(",")
    u = []
    v = []
    for elem in u_aux:
        elem = u.append(int(elem))
    for elem in v_aux:
        elem = v.append(int(elem))
    return u, v

def juntar_xyz(u, v):
    x, y, z = [], [], []
    i = 0
    x.append(u[0])
    if len(u) > 1:
        y.append(u[1])
    if len(u) > 2:
        z.append(u[2])
    x.append(v[0])
    if len(v) > 1:
        y.append(v[1])
    if len(v) > 2:
        z.append(v[2])
    return x, y, z

def transformacion(a, b, c):
    t = [a, b, c]
    return t

def verificar_transformacion(u, v):
    verf = False
    suma_uv = []
    for i in range(len(u)):
        suma = u[i] + v[i]
        suma_uv.append(suma)

    return verf

def mostrar_grafico(coord_x, coord_y):
    x = [0]*len(coord_x)
    y = [0]*len(coord_y)
    l = min(-1, min(coord_x)-1)
    r = max(1, max(coord_x)+1)
    b = min(-1, min(coord_y)-1)
    t = max(1, max(coord_y)+1)

    plt.xlim([l, r])
    plt.ylim([b, t])
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.quiver(x, y, coord_x, coord_y,  angles='xy', scale_units='xy', scale=1)
    plt.show()

if __name__ == "__main__":
    u, v = pedir_coordenadas()
    x, y, z = juntar_xyz(u, v)
    verificar_transformacion(u, v)
