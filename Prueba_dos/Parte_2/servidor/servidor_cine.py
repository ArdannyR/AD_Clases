from xmlrpc.server import SimpleXMLRPCServer

peliculas = {} # Diccionario ["id": ..., "titulo": ..., "genero": ...]

def obtener_peliculas():
    respuesta = ""
    if not peliculas:
        return "\nNo hay nada..."
    for key in peliculas:
        respuesta += f"\n{key}. Titulo: {peliculas[key]["titulo"]} - Genero: {peliculas[key]["genero"]}"
    return respuesta

def agregar_pelicula(titulo, genero):
    id = len(peliculas) + 1
    key = str(id)
    peliculas[key] = {"titulo": titulo, "genero": genero}
    respuesta = f"\nPelicula {peliculas[key]["titulo"]} - {peliculas[key]["genero"]} agregada"
    return respuesta

def actualizar_pelicula(id, titulo, genero):
    key = str(id)
    if key in peliculas:
        peliculas[key] = {"titulo": titulo, "genero": genero}
        respuesta = f"\nPelicula {key} actualizada a: {peliculas[key]['titulo']} - {peliculas[key]['genero']}"
        return respuesta
    else:
        respuesta = f"\nPelicula {key} no encontrada"
        return respuesta
    

def eliminar_pelicula(id):
    key = str(id)
    if key in peliculas:
        peliculas.pop(key)
    respuesta = f"\nPelicula {key} eliminada"
    return respuesta 

server = SimpleXMLRPCServer(("0.0.0.0", puerto))
server.register_function(obtener_peliculas, "obtener_peliculas")
server.register_function(agregar_pelicula, "agregar_pelicula")
server.register_function(actualizar_pelicula, "actualizar_pelicula")
server.register_function(eliminar_pelicula, "eliminar_pelicula")

print("Servidor de cine listo...")
server.serve_forever()

