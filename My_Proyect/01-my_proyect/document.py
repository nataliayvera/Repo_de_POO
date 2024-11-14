
"""Trabajo Practico"""

#Crear clase documento 

class Documento(object): 
    def __init__(self, id, contenido=None):
        self.id = id
        self.contenido =contenido if contenido is not None else {}

    def obtener_valor(self, clave):
        return self.contenido.get(clave, None)
    
    def modificar_valor(self,clave,valor):
        self.contenido[clave] = valor

    def __str__(self):
        return f"Documento(id={self.id}, contenido={self.contenido})"
    
class Coleccion(object):
    def __init__ (self,nombre):
        self.nombre = nombre
        self.documentos = {}

    def añadir_documento(self,documento):
        self.documentos[documento.id] = documento

    def eliminar_documento(self, id_documento):
        if id_documento in self.documentos:
            del self.documentos[id_documento]

    def buscar_documento(self, id_documento):
        return self.documentos.get(id_documento, None)

# Prueba de la clase Documento y Coleccion
c = Coleccion('libros')
l1 = Documento(1,{'Titulo' : 'Python para todos','Autor': 'Harry Styles'})
l2= Documento (2,{'titulo':'Fundamentos del lenguaje', 'Autor': 'Leonel Vera'})
c.añadir_documento(l1)
c.añadir_documento(l2)


# Modificando el contenido del primer documento
libro = c.buscar_documento(1)
print(libro)  
libro.modificar_valor('Autor', 'Nuevo Autor')
print(libro) 


# Eliminar el documento
c.eliminar_documento(libro.id)
libro = c.buscar_documento(1)
print(libro.obtener_valor('Titulo'), libro.obtener_valor('Autor'))
