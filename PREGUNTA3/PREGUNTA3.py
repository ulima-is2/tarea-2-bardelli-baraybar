import sys
import sqlite3

conn = sqlite3.connect('tarea2')

class Entrada:
    def __init__(self, cine_id, pelicula_id, funcion, cantidad):
        self.cine_id = cine_id
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad

class Pelicula:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

class CineFactory:

    def obtener_cine(self,tipo_cine):
        if tipo_cine == '1':
            return CinePlaneta()
        else:
            return CineStark()

class Cine:

    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, cine_id, id_pelicula_elegida, funcion_elegida, cantidad):
        # entrada = Entrada(cine_id,id_pelicula_elegida, funcion_elegida, cantidad)
        c = conn.cursor()
        c.execute('INSERT INTO entrada VALUES ('+ cine_id +',' + id_pelicula_elegida + ','+ funcion_elegida +','+ cantidad + ')')
        conn.commit()
        c = conn.cursor()
        return c.execute('SELECT * FROM entrada').arraysize


class CinePlaneta(Cine):
    def __init__(self):
        peliculaIT = Pelicula(1, 'IT')
        peliculaHF = Pelicula(2, 'La Hora Final')
        peliculaD = Pelicula(3, 'Desparecido')
        peliculaDeep = Pelicula(4, 'Deep El Pulpo')

        peliculaIT.funciones = ['19:00', '20.30', '22:00']
        peliculaHF.funciones = ['21:00']
        peliculaD.funciones = ['20:00', '23:00']
        peliculaDeep.funciones = ['16:00']

        self.lista_peliculas = [peliculaIT, peliculaHF, peliculaD, peliculaDeep]
        self.entradas = []


class CineStark(Cine):
    def __init__(self):
        peliculaD = Pelicula(1, 'Desparecido')
        peliculaDeep = Pelicula(2, 'Deep El Pulpo')

        peliculaD.funciones = ['21:00', '23:00']
        peliculaDeep.funciones = ['16:00', '20:00']

        self.lista_peliculas = [peliculaD, peliculaDeep]
        self.entradas = []


def main():
    terminado = False
    cineFactory = CineFactory()
    while not terminado:
        print('Ingrese la opción que desea realizar')
        print('(1) Listar cines')
        print('(2) Listar cartelera')
        print('(3) Comprar entrada')
        print('(0) Salir')
        opcion = input('Opción: ')

        if opcion == '1':
            print('********************')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')

        elif opcion == '2':
            print('********************')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')

            cine = input('Primero elija un cine:')

            cine = cineFactory.obtener_cine(cine)

            peliculas = cine.listar_peliculas()
            print('********************')
            for pelicula in peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            print('********************')


        elif opcion == '3':
            print('********************')
            print('COMPRAR ENTRADA')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')
            cine_id = input('Primero elija un cine:')

            cine = cineFactory.obtener_cine(cine_id)

            peliculas = cine.listar_peliculas()
            for pelicula in peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            pelicula_elegida = input('Elija pelicula:')
            #pelicula = obtener_pelicula(id_pelicula)
            print('Ahora elija la función (debe ingresar el formato hh:mm): ')
            for funcion in cine.listar_funciones(pelicula_elegida):
                print('Función: {}'.format(funcion))
            funcion_elegida = input('Funcion: ')
            cantidad_entradas = input('Ingrese cantidad de entradas: ')
            codigo_entrada = cine.guardar_entrada(cine_id, pelicula_elegida, funcion_elegida, cantidad_entradas)
            print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))
        elif opcion == '0':
            terminado = True
            c = conn.cursor()
            for row in c.execute('SELECT * FROM entrada'):
                print(row)
            conn.close()
        else:
            print(opcion)



if __name__ == '__main__':
    main()
