import sqlite3

connection =sqlite3.connect('cine.db')
cursor = connection.cursor()

cursor.execute('create table Cine (id real, nombre text)')
cursor.execute('create table Pelicula (id real, nombre text)')
cursor.execute('create table PeliculaxCine (id_cine real, id_pelicula real)')
cursor.execute('create table Funcion (id real, hora text)')
cursor.execute('create table FuncionxPeliculaxCine(id_cine real, id_pelicula real, id_funcion real)')
cursor.execute('create table Entrada (id real, id_pelicula real, id_funcion real, cantidad real)')

cursor.execute("insert into Cine values (1,'CinePlaneta')")
cursor.execute("insert into Cine values (2,'CineStark')")

cursor.execute("insert into Pelicula values (1, 'IT')")
cursor.execute("insert into Pelicula values (2, 'La Hora Final')")
cursor.execute("insert into Pelicula values (3, 'Desparecido')")
cursor.execute("insert into Pelicula values (4, 'Deep El Pulpo')")

cursor.execute("insert into PeliculaxCine values(1,1)")
cursor.execute("insert into PeliculaxCine values(1,2)")
cursor.execute("insert into PeliculaxCine values(1,3)")
cursor.execute("insert into PeliculaxCine values(1,4)")
cursor.execute("insert into PeliculaxCine values(2,3)")
cursor.execute("insert into PeliculaxCine values(2,4)")


connection.commit()


