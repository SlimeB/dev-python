import shelve

fruta = shelve.open("fruit")
#      v-"llave"  v-"resultado"
fruta["mango"] = "dulce"
fruta["kiwi"] = "acido"
"""
las shelves funcionan parecido que un diccionario, pero a diferencia de estas
la llave soloo puede ser un string
"""

fruta.close()