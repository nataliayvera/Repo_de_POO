class Coleccion(object):
    def __init__ (self,nombre):
        self.nombre = nombre
        self.documentos = {}

    def añadir_documento (self,documento):
        self.documentos[documento.id] = documento

    def eliminar_documento(self, id_documento):
        if id_documento in self.documentos:
            del self.documentos[id_documento]

    def buscar_documento(self, id_documento):
        return self.documentos.get(id_documento, None)
    
    def __str__(self):
        return f"coleccion {self.nombre} con {len(self.documentos)} documentos."

class Database:
    def __init__(self):
        self.colecciones = {}

    def crear_coleccion (self, nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones [nombre_coleccion] = Coleccion(nombre_coleccion)

    def eliminar_coleccion(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]

    def obtener_coleccion(self,nombre_coleccion):
        return self.colecciones.get(nombre_coleccion, None)
    
    def __str__(self):
        return f"Base de datos documental con {len(self.colecciones)} colecciones"
