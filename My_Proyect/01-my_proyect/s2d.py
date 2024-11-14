schema= "Nombre,Apellido,Edad,Mail"
row= "Natalia,Vera,25,nataliayvera17@gmail.com"

class Str2Dic (object):
    def __init__(self, schemaStr, separator =","):
        self.schema = schemaStr.split(separator)
        self.separator = separator

    def convert(self, row):
        tmp = row.split(self.separator)
        if len(tmp) == len(self.schema):
            i= 0
            d={}
            while i < len(tmp):
                d[self.schema[i]] = tmp[i]
                i = i + 1
            return d
        
o = Str2Dic(schema)
d= o.convert(row)
print (d)