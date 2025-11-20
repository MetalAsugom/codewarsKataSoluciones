def merge(*dicts):
    resultado = {}
    for diccionario in dicts:
        for clave, valor in diccionario.items():
            if clave in resultado:
                resultado[clave].append(valor)
            else:
                resultado[clave] = [valor]
    return resultado